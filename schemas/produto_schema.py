from decimal import Decimal
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: str
    preco: Decimal
    unidade_id: int

