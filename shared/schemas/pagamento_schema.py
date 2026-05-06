from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel

class Pagamento(BaseModel):
    pedido_id: int
    valor: Decimal
    metodo_pagamento: MetodoPagamento

    status: str  # success, pending, error
    transacao_id: str | None = None

    data_pagamento: datetime