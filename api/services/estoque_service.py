from fastapi import HTTPException
from sqlalchemy.orm import Session
from api.database.models.estoque import Estoque
from shared.schemas.estoque_schema import EstoqueConsulta, EstoqueCreate


def buscar_estoque_por_produto(db: Session ,produto_id: int, unidade_id:int ):
    busca = db.query(Estoque).filter(
        Estoque.produto_id == produto_id,
        Estoque.unidade_id == unidade_id
    ).first()
    return busca
    

def criar_estoque_service(db: Session, estoque: EstoqueCreate):
    estoque_existente = buscar_estoque_por_produto(db, estoque.produto_id, estoque.unidade_id)
    if estoque_existente:
        estoque_existente.quantidade += estoque.quantidade
        db.refresh(estoque_existente)
        return estoque_existente
    novo_estoque = Estoque(
        produto_id=estoque.produto_id,
        unidade_id=estoque.unidade_id,
        quantidade=estoque.quantidade
    )
    db.add(novo_estoque)
    db.commit()
    db.refresh(novo_estoque)
    return novo_estoque



def listar_estoque_por_unidade(db: Session , unidade_id: int):
    unidade_estoque = db.query(Estoque).filter(Estoque.unidade_id == unidade_id).all() 
    if not unidade_estoque:
        return []
    return unidade_estoque



def saida_estoque_service(db: Session ,estoque: EstoqueConsulta):
    recebe_produto = buscar_estoque_por_produto(db, estoque.produto_id, estoque.unidade_id)
    if not recebe_produto:
        raise HTTPException(
            status_code=404,
            detail="Produto não encontrado no estoque dessa unidade"
        )
    verificar_disponibilidade(recebe_produto, estoque.quantidade)
    baixa_estoque(db, recebe_produto, estoque.quantidade)
    return recebe_produto



def verificar_disponibilidade(estoque_db: Estoque, quantidade: int):
    if estoque_db.quantidade < quantidade:
        raise HTTPException(
            status_code=400,
            detail="Estoque insuficiente"
        )


def baixa_estoque(db: Session ,estoque_db: Estoque, quantidade: int):
    estoque_db.quantidade -= quantidade
