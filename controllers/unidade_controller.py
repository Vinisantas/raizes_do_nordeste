from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.conexao import get_db
from services.unidade_service import listar_unidade_por_id_service, listar_unidades_services

router = APIRouter(prefix="/unidades", tags=["Unidades"])

@router.get("/")
def listar_unidades(db: Session = Depends(get_db)):
    return listar_unidades_services(db)

@router.get("/{unidade_id}")
def obter_unidade(unidade_id: int, db: Session = Depends(get_db)):
    return listar_unidade_por_id_service(db, unidade_id)