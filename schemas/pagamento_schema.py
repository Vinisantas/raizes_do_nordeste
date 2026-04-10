import datetime
from decimal import Decimal
from pydantic import BaseModel

class Pagamento(BaseModel):
    pedido_id: int
    valor: Decimal
    metodo_pagamento: enumerate
    data_pagamento: datetime
