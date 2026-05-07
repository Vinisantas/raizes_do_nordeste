from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel
from shared.enums.pagamento_enum import MetodoPagamento, StatusPagamento

class Pagamento(BaseModel):
    pedido_id: int
    valor: Decimal
    metodo_pagamento: MetodoPagamento
    status: StatusPagamento
    transacao_id: str | None = None
    data_pagamento: datetime