from pydantic import BaseModel

class UnidadeBase(BaseModel):
    nome: str
    endereco: str
    
class UnidadeCreate(UnidadeBase):
    pass

class UnidadeUpdate(UnidadeBase):
    nome: str  | None = None
    endereco: str  | None = None

class UnidadeResponse(UnidadeBase):
    id: int

    class Config:
        from_attributes = True    