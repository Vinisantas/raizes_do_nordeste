from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from authentication.security import require_role
from database.conexao import get_db
from database.models.usuario import Usuario
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
def criar_produto(
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_role("ADMIN", "GERENTE"))
):
    return criar_produto_service(db, produto, current_user)  


@router.get("/", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return listar_produtos_service(db)


@router.get("/{id}", response_model=ProdutoResponse)
def listar_produto(id: int, db: Session = Depends(get_db)):
    return listar_produto_por_id_service(db, id)


@router.delete("/{id}", status_code=204)
def deletar_produto(id: int, db: Session = Depends(get_db)):
    deletar_produto_service(db, id)
    return None 


@router.patch("/{id}", response_model=ProdutoResponse)
def atualizar_produto(id: int, produto: ProdutoUpdate, db: Session = Depends(get_db)):
    produto_atualizado = atualizar_produto_service(db, id, produto)
    if not produto_atualizado:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto_atualizado