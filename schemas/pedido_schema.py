from decimal import Decimal
from pydantic import BaseModel
from database.models.pedido import StatusPedido, CanalPedido


class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int


class PedidoCreate(BaseModel):
    usuario_id: int
    unidade_id: int
    status: StatusPedido
    canal_pedido: CanalPedido
    itens: list[ItemPedidoCreate]


class PedidoResponse(BaseModel):
    id: int
    total: Decimal
    status: StatusPedido

    class Config:
        from_attributes = True