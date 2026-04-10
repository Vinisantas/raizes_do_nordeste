from decimal import Decimal
from pydantic import BaseModel

class PedidoBase(BaseModel):
    usuario_id: int
    unidade_id: int
    data_pedido: str
    total: Decimal
    status = enumerate
    canal_pedido: enumerate
    
class ItemPedidoBase(BaseModel):
    pedido_id: int
    produto_id: int
    quantidade: int
    preco_unitario: Decimal
    subtotal: float