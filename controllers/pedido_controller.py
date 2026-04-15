

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.pedido_schema import PedidoResponse
from database.conexao import get_db
from services.pedido_service import (
    listar_pedidos_service)



router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

@router.get("/", response_model=list[(PedidoResponse)])
def listar_pedidos(db: Session = Depends(get_db)):
    return listar_pedidos_service(db)