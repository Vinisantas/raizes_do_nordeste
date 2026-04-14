from sqlalchemy.orm import Session
from database.models.produto import Produto
from schemas.produto_schema import ProdutoCreate, ProdutoUpdate


def criar_produto_service(db: Session, produto: ProdutoCreate):
    db_produto = Produto(**produto.dict())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto

def listar_produtos_service(db: Session):
    return db.query(Produto).all()

def listar_produto_por_id_service(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()

def deletar_produto_service(db: Session, produto_id: int):
    db_produto = listar_produto_por_id_service(db, produto_id)
    if db_produto:
        db.delete(db_produto)
        db.commit()
    return db_produto

def atualizar_produto_service(db: Session, produto_id: int, produto: ProdutoUpdate):
    db_produto = listar_produto_por_id_service(db, produto_id)
    if db_produto:
        for key, value in produto.dict().items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
    return db_produto