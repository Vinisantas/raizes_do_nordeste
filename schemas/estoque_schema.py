from pydantic import BaseModel


class EstoqueBase(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int