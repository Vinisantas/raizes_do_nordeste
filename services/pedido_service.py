from sqlalchemy.orm import Session, selectinload
from database.models.pedido import ItemPedido, Pedido
from database.models.produto import Produto
from schemas.pedido_schema import PedidoCreate, PedidoUpdate


def criar_pedido_service(db: Session, pedido: PedidoCreate):
    try:
        total = 0
        db_pedido = Pedido(
            usuario_id=pedido.usuario_id,
            unidade_id=pedido.unidade_id,
            status=pedido.status,
            canal_pedido=pedido.canal_pedido,
            total=0
        )
        db.add(db_pedido)
        db.flush()
        for item in pedido.itens:
            produto = db.query(Produto).filter(Produto.id == item.produto_id).first()
            if not produto:
                raise ValueError(f"Produto {item.produto_id} não encontrado")
            subtotal = produto.preco * item.quantidade
            total += subtotal
            db_item = ItemPedido(
                pedido_id=db_pedido.id,
                produto_id=produto.id,
                quantidade=item.quantidade,
                preco_unitario=produto.preco
            )
            db.add(db_item)
        db_pedido.total = total
        db.commit()
        db.refresh(db_pedido)
        return db_pedido
    except Exception:
        db.rollback()
        raise


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
