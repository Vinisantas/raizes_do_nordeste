from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session, selectinload

from api.database.models.pedido import ItemPedido, Pedido
from api.database.models.produto import Produto
from api.database.models.pagamento import Pagamento as PagamentoModel

from api.services.pagamento_service import processar_pagamento
from api.services.estoque_service import entrada_estoque_service, saida_estoque_service

from shared.enums.pagamento_enum import MetodoPagamento, StatusPagamento
from shared.enums.pedido_enum import TRANSICOES, CanalPedido, StatusPedido
from shared.schemas.estoque_schema import EstoqueConsulta
from shared.schemas.pedido_schema import PedidoCreate, PedidoUpdate


async def criar_pedido_service(db: Session, pedido: PedidoCreate):

    try:
        total = 0
        itens_processados = []
        db_pedido = Pedido(
            usuario_id=pedido.usuario_id,
            unidade_id=pedido.unidade_id,
            canal_pedido=pedido.canal_pedido,
            status=StatusPedido.AGUARDANDO_PAGAMENTO,
            total=0
        )
        db.add(db_pedido)
        db.flush()
        for item in pedido.itens:
            produto = (
                db.query(Produto)
                .filter(Produto.id == item.produto_id)
                .first())
            if not produto:
                raise HTTPException(
                    status_code=404,
                    detail=f"Produto {item.produto_id} não encontrado")
            qtd = item.quantidade
            saida_estoque_service(
                db,
                EstoqueConsulta(
                    produto_id=item.produto_id,
                    unidade_id=pedido.unidade_id,
                    quantidade=qtd))
            db_item = ItemPedido(
                pedido_id=db_pedido.id,
                produto_id=produto.id,
                quantidade=qtd,
                preco_unitario=produto.preco)
            db.add(db_item)
            total += produto.preco * qtd
            itens_processados.append({
                "produto_id": produto.id,
                "quantidade": qtd})
        db_pedido.total = total
        resultado_pagamento = await processar_pagamento(
            db_pedido.id,
            float(total),
            "success")
        novo_pagamento = PagamentoModel(
            pedido_id=db_pedido.id,
            valor=total,
            metodo_pagamento=MetodoPagamento.PIX,
            transacao_id=resultado_pagamento.get("transacao_id"),
            resposta_gateway=resultado_pagamento
        )
        if resultado_pagamento["status"] == "success":
            db_pedido.status = StatusPedido.COZINHA
            novo_pagamento.status = StatusPagamento.SUCCESS
            novo_pagamento.data_pagamento = datetime.utcnow()
            print(f"Pagamento aprovado para pedido {db_pedido.id}")
        else:
            db_pedido.status = StatusPedido.CANCELADO
            novo_pagamento.status = StatusPagamento.ERROR
            for item in itens_processados:
                entrada_estoque_service(
                    db,
                    EstoqueConsulta(
                        produto_id=item["produto_id"],
                        unidade_id=pedido.unidade_id,
                        quantidade=item["quantidade"]))
            print(f"Pagamento recusado para pedido {db_pedido.id}")
        db.add(novo_pagamento)
        db.commit()
        db.refresh(db_pedido)
        print(f"Pedido {db_pedido.id} criado com sucesso")
        return db_pedido
    except Exception as e:
        db.rollback()
        print(f"Erro ao criar pedido: {str(e)}")
        raise e

def listar_pedidos_service(db: Session):
    return (
        db.query(Pedido)
        .options(
            selectinload(Pedido.itens),
            selectinload(Pedido.usuario),
            selectinload(Pedido.unidade)
        )
        .all()
    )


def listar_pedido_por_id_service(db: Session, id: int):
    return db.query(Pedido).filter(Pedido.id == id).first()


def listar_por_canal_service(db: Session, canal_pedido: CanalPedido):
    return db.query(Pedido).filter(
        Pedido.canal_pedido == canal_pedido
    ).all()


def deletar_pedido_service(db: Session, id: int) -> bool:
    db_pedido = listar_pedido_por_id_service(db, id)
    if not db_pedido:
        return False
    db.delete(db_pedido)
    db.commit()
    return True



def atualizar_pedido_service(db: Session, id: int, pedido: PedidoUpdate):
    db_pedido = listar_pedido_por_id_service(db, id)
    if not db_pedido:
        return None
    dados = pedido.model_dump(exclude_unset=True)
    for key, value in dados.items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def atualizar_status_service(
         id: int,
         novo_status,
         db: Session,
         current_user):
    pedido = listar_pedido_por_id_service(db, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    proximos_possiveis = TRANSICOES.get(pedido.status, [])
    novo_status = StatusPedido(novo_status)
    if novo_status not in proximos_possiveis:
        raise HTTPException(
            status_code=400,
            detail=f"Transição inválida: Não é possível mudar de {pedido.status} para {novo_status}")
    pedido.status = novo_status
    db.commit()
    db.refresh(pedido)
    return pedido