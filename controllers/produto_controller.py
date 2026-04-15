from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.conexao import get_db
from schemas.produto_schema import ProdutoCreate, ProdutoUpdate, ProdutoResponse
from services.produto_service import (
    criar_produto_service,
    listar_produto_por_id_service,
    listar_produtos_service,
    atualizar_produto_service,
    deletar_produto_service
)


router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    return criar_produto_service(db, produto)


@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return listar_produtos_service(db)


@router.get("/{produto_id}", response_model=ProdutoResponse)
def listar_produto(produto_id: int, db: Session = Depends(get_db)):
    return listar_produto_por_id_service(db, produto_id)


@router.delete("/{produto_id}", status_code=204)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    deletado = deletar_produto_service(db, produto_id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")


@router.patch("/{produto_id}")
def atualizar_produto(produto_id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    return atualizar_produto_service(db, produto_id, produto)
