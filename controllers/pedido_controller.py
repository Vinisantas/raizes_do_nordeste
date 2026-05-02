from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.pedido_schema import PedidoCreate, PedidoResponse, PedidoUpdate
from database.conexao import get_db
from enums.pedido_enum import CanalPedido, StatusPedido
from services.pedido_service import (
    atualizar_pedido_service,
    atualizar_status_service,
    criar_pedido_service,
    deletar_pedido_service,
    listar_pedido_por_id_service,
    listar_pedidos_service,
    listar_por_canal_service)


router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("/", response_model=PedidoResponse, status_code=201)
def criar_pedido(pedido: PedidoCreate, db: Session = Depends(get_db)):
    return criar_pedido_service(db, pedido)


@router.get("/", response_model=list[PedidoResponse])
def listar_pedidos(db: Session = Depends(get_db)):
    return listar_pedidos_service(db)


@router.get("/filtro")
def listar_por_canal(canal_pedido: CanalPedido, db: Session = Depends(get_db)):
    return listar_por_canal_service(db, canal_pedido)



@router.get("/{id}", response_model=PedidoResponse)
def listar_pedido(id: int, db: Session = Depends(get_db)):
    pedido = listar_pedido_por_id_service(db, id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido



@router.delete("/{id}", status_code=204)
def deletar_pedido(id: int, db: Session = Depends(get_db)):
    deletado = deletar_pedido_service(db, id)
    if not deletado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")


@router.patch("/{id}", response_model=PedidoResponse)
def atualizar_pedido(id: int, pedido: PedidoUpdate, db: Session = Depends(get_db)):
    pedido_atualizado = atualizar_pedido_service(db, id, pedido)
    if not pedido_atualizado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido_atualizado

@router.patch("/{id}/status", response_model=PedidoResponse)
def atualizar_status_pedido(id: int, novo_status: StatusPedido , db: Session = Depends(get_db)):
    status_atualizado = atualizar_status_service(db, id, novo_status)
    if not status_atualizado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return status_atualizado