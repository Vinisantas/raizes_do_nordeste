from pydantic import BaseModel

class UnidadeBase(BaseModel):
    nome: str
    endereco: str
    unidade_id: int