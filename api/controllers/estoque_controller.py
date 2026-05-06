from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.database.conexao import get_db
from shared.schemas.estoque_schema import EstoqueCreate, EstoqueResponse
from api.services.estoque_service import criar_estoque_service, listar_estoque_por_unidade


router = APIRouter(prefix="/estoques", tags=["Estoques"])

@router.post("/" , response_model=EstoqueResponse, status_code=201)
def criar_estoque(estoque: EstoqueCreate, db: Session = Depends(get_db)):
    return criar_estoque_service(db, estoque)

@router.get("/{unidade_id}", response_model=list[EstoqueResponse])
def buscar_estoque_unidade(unidade_id: int, db: Session = Depends(get_db)):
    lista = listar_estoque_por_unidade(db, unidade_id)
    if not lista:
        raise HTTPException(status_code=404, detail="Estoque não encontrado")
    return lista

