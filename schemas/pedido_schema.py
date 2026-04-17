from decimal import Decimal
from pydantic import BaseModel, field_validator
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

class PedidoUpdate(BaseModel):
    usuario_id: int | None = None
    unidade_id: int | None = None
    status: StatusPedido | None = None
    canal_pedido: CanalPedido | None = None
    itens: list[ItemPedidoCreate] | None = None
class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    unidade_id: int
    total: Decimal
    status: StatusPedido
    canal_pedido: CanalPedido

    class Config:
        from_attributes = True

class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int
    @field_validator("quantidade")
    def validar_quantidade(cls, v):
        if v <= 0:
            raise ValueError("Quantidade deve ser maior que zero")
        return v