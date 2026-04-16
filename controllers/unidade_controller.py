from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.conexao import get_db
from schemas.unidade_schema import UnidadeCreate, UnidadeResponse, UnidadeUpdate
from services.unidade_service import (
    atualizar_unidade_service,
    deletar_unidade_service,
    listar_unidade_por_id_service,
    listar_unidades_service,
    criar_unidade_service
)


router = APIRouter(prefix="/unidades", tags=["Unidades"])


@router.post("/" , response_model=UnidadeResponse, status_code=201)
def criar_unidade(unidade: UnidadeCreate, db: Session = Depends(get_db)):
    return criar_unidade_service(db, unidade)


@router.get("/", response_model=list[UnidadeResponse])
def listar_unidades(db: Session = Depends(get_db)):
    return listar_unidades_service(db)


@router.get("/{id}", response_model=UnidadeResponse)
def listar_unidade(id: int, db: Session = Depends(get_db)):
    return listar_unidade_por_id_service(db, id)


@router.delete("/{id}", status_code=204)
def deletar_unidade(id: int, db: Session = Depends(get_db)):
    deletar_unidade_service(db, id)


@router.patch("/{id}", response_model=UnidadeResponse)
def atualizar_unidade(id: int, unidade: UnidadeUpdate, db: Session = Depends(get_db)):
    return atualizar_unidade_service(db, id, unidade)

