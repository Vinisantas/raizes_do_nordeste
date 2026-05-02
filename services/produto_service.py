from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.produto import Produto
from schemas.produto_schema import  ProdutoCreate, ProdutoUpdate


def criar_produto_service(db: Session, produto: ProdutoCreate, current_user):
    db_produto = Produto(
        nome = produto.nome,
        descricao = produto.descricao,
        preco = produto.preco )
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


def listar_produtos_service(db: Session):
    return db.query(Produto).all()


def listar_produto_por_id_service(db: Session, id: int):
    produto =  db.query(Produto).filter(Produto.id == id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto


def deletar_produto_service(db: Session, id: int):
    produto = db.query(Produto).filter(Produto.id == id).first()
    if not produto :
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    db.delete(produto)
    db.commit()


def atualizar_produto_service(db: Session, id: int, produto: ProdutoUpdate):
    db_produto = db.query(Produto).filter(Produto.id == id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    if produto.nome is not None:
        db_produto.nome = produto.nome
    if produto.descricao is not None:
        db_produto.descricao = produto.descricao
    if produto.preco is not None:
        db_produto.preco = produto.preco
    db.commit()
    db.refresh(db_produto)
    return db_produto