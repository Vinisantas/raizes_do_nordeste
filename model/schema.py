import pydantic


class User(pydantic.BaseModel):
    id: int
    nome: str
    email: str
    senha: str
    role: str



