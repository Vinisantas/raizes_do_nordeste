from decimal import Decimal
from pydantic import BaseModel


class ProdutoBase(BaseModel):
    nome: str
    descricao: str | None
    preco: Decimal

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str | None
    preco: Decimal 
    
class ProdutoUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None
    preco: Decimal | None = None


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str | None
    preco: Decimal
    class Config:
        from_attributes = True