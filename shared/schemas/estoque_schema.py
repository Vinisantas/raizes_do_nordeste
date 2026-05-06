from pydantic import BaseModel

class EstoqueBase(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int


class EstoqueConsulta(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int

class EstoqueCreate(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int


class EstoqueUpdate(BaseModel):
    produto_id: int | None = None
    unidade_id: int | None = None
    quantidade: int | None = None


class EstoqueResponse(BaseModel):
    produto_id: int
    unidade_id: int
    quantidade: int
    class Config:
        from_attributes = True
