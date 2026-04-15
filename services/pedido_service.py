from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.pedido import Pedido
from schemas.pedido_schema import PedidoCreate, PedidoUpdate


def criar_pedido_service(db, pedido : PedidoCreate):
    db_pedido = Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido


def listar_pedidos_service(db : Session):
    return db.query(Pedido).all()


def listar_pedido_por_id_service(db: Session, pedido_id: int):
    return db.query(Pedido).filter(Pedido.id == pedido_id).first()


def deletar_pedido_service(db: Session, pedido_id: int):
    db_pedido = listar_pedido_por_id_service(db , pedido_id)
    if not db_pedido:
        raise HTTPException(status_code=404, detail="Produto não encontrada")
    db.delete(db_pedido)
    db.commit()
    return db_pedido



def atualizar_produto_service(db: Session, pedido_id: int, produto: PedidoUpdate):
    db_pedido = listar_pedido_por_id_service(db, pedido_id)
    if db_pedido:
        for key, value in produto.dict().items():
            setattr(db_pedido, key, value)
        db.commit()
        db.refresh(db_pedido)
    return db_pedido
