from pydantic import BaseModel

class UnidadeBase(BaseModel):
    nome: str
    endereco: str
    unidade_id: int

class UnidadeCreate(UnidadeBase):
    pass

class UnidadeUpdate(UnidadeBase):
    pass

class UnidadeResponse(UnidadeBase):
    id: int

    class Config:
        orm_mode = True