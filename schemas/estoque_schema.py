from pydantic import BaseModel


class EStoqueBase(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int