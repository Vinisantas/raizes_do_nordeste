from decimal import Decimal
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: str | None
    preco: Decimal


class ProdutoCreate(ProdutoBase):
    unidade_id: int


class ProdutoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: Decimal | None = None
    unidade_id: int | None = None

class UnidadeResponse(BaseModel):
    id: int
    nome: str


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None
    preco: Decimal
    unidade: UnidadeResponse

    class Config:
        from_attributes = True