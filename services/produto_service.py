from sqlalchemy.orm import Session, selectinload
from sqlalchemy.exc import SQLAlchemyError
from database.models.produto import Produto
from database.models.unidade import Unidade
from schemas.produto_schema import ProdutoCreate, ProdutoUpdate


def criar_produto_service(db: Session, produto: ProdutoCreate):
    try:
        unidade = db.query(Unidade).filter(Unidade.id == produto.unidade_id).first()
        if not unidade:
            raise ValueError("Unidade não encontrada")
        db_produto = Produto(**produto.model_dump())
        db.add(db_produto)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    except SQLAlchemyError:
        db.rollback()
        raise


def listar_produtos_service(db: Session):
    return (
        db.query(Produto)
        .options(selectinload(Produto.unidade))
        .all()
    )


def listar_produto_por_id_service(db: Session, id: int):
    return (
        db.query(Produto)
        .options(selectinload(Produto.unidade))
        .filter(Produto.id == id)
        .first()
    )


def deletar_produto_service(db: Session, id: int) -> bool:
    db_produto = db.query(Produto).filter(Produto.id == id).first()
    if not db_produto:
        return False
    try:
        db.delete(db_produto)
        db.commit()
        return True
    except SQLAlchemyError:
        db.rollback()
        raise


def atualizar_produto_service(db: Session, id: int, produto: ProdutoUpdate):
    db_produto = db.query(Produto).filter(Produto.id == id).first()
    if not db_produto:
        return None
    try:
        dados = produto.model_dump(exclude_unset=True)
        if "unidade_id" in dados:
            unidade = db.query(Unidade).filter(Unidade.id == dados["unidade_id"]).first()
            if not unidade:
                raise ValueError("Unidade não encontrada")

        for key, value in dados.items():
            setattr(db_produto, key, value)
        db.commit()
        db.refresh(db_produto)
        return db_produto
    except SQLAlchemyError:
        db.rollback()
        raise