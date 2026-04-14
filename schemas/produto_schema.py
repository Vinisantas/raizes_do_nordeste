from decimal import Decimal
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: Decimal
    unidade_id: int

class ProdutoCreate(ProdutoBase):
    pass

class ProdutoUpdate(ProdutoBase):
    pass

class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        orm_mode = True