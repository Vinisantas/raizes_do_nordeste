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


@router.get("/{unidade_id}", response_model=UnidadeResponse)
def listar_unidade(unidade_id: int, db: Session = Depends(get_db)):
    return listar_unidade_por_id_service(db, unidade_id)


@router.delete("/{unidade_id}", status_code=204)
def deletar_unidade(unidade_id: int, db: Session = Depends(get_db)):
    deletar_unidade_service(db, unidade_id)


@router.patch("/{unidade_id}", response_model=UnidadeResponse)
def atualizar_unidade(unidade_id: int, unidade: UnidadeUpdate, db: Session = Depends(get_db)):
    return atualizar_unidade_service(db, unidade_id, unidade)

