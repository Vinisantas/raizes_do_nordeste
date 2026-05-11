from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.authentication.security import require_role
from api.database.models.usuario import Usuario
from api.database.conexao import get_db
from shared.schemas.unidade_schema import CardapioItem, UnidadeCreate, UnidadeResponse, UnidadeUpdate
from api.services.unidade_service import (
    atualizar_unidade_service,
    deletar_unidade_service,
    listar_cardapio_por_unidade_service,
    listar_unidade_por_id_service,
    listar_unidades_service,
    criar_unidade_service
)


router = APIRouter(prefix="/unidades", tags=["Unidades"])


@router.post("/" , response_model=UnidadeResponse, status_code=201)
def criar_unidade(
    unidade: UnidadeCreate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_role("ADMIN", "GERENTE"))
):
    return criar_unidade_service(db, unidade)


@router.get("/", response_model=list[UnidadeResponse])
def listar_unidades(db: Session = Depends(get_db)):
    return listar_unidades_service(db)


@router.get("/{unidade_id}/cardapio", response_model=list[CardapioItem])
def listar_cardapio(unidade_id: int, somente_disponiveis: bool = False, db: Session = Depends(get_db)):
    return listar_cardapio_por_unidade_service(db, unidade_id, somente_disponiveis)


@router.get("/{id}", response_model=UnidadeResponse)
def listar_unidade(id: int, db: Session = Depends(get_db)):
    return listar_unidade_por_id_service(db, id)


@router.delete("/{id}", status_code=204)
def deletar_unidade(id: int, db: Session = Depends(get_db)):
    deletar_unidade_service(db, id)


@router.patch("/{id}", response_model=UnidadeResponse)
def atualizar_unidade(
    id: int,
    unidade: UnidadeUpdate,
    db: Session = Depends(get_db),
    current_user: Usuario = Depends(require_role("ADMIN", "GERENTE"))
):
    return atualizar_unidade_service(db, id, unidade)

