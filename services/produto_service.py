from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from database.models.produto import Produto
from schemas.produto_schema import ProdutoCreate, ProdutoUpdate


def criar_produto_service(db: Session, produto: ProdutoCreate):
    try:
        db_produto = Produto(**produto.model_dump())
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    except SQLAlchemyError:
        db.rollback()
        raise


def listar_produtos_service(db: Session):
    return db.query(Produto).all()


def listar_produto_por_id_service(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()


def deletar_produto_service(db: Session, produto_id: int) -> bool:
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not db_produto:
        return False  
    try:
        db.delete(db_produto)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        raise


def atualizar_produto_service(db: Session, produto_id: int, produto: ProdutoUpdate):
    db_produto = listar_produto_por_id_service(db, produto_id)

    if not db_produto:
        return None
    try:
        for key, value in produto.model_dump(exclude_unset=True).items():
            setattr(db_produto, key, value)

        db.commit()
        db.refresh(db_produto)
        return db_produto
    except SQLAlchemyError:
        db.rollback()
        raise