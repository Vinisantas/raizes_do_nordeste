from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    id: int
    nome: str
    email: EmailStr
    senha: str
    role: str
    cliente_id: int


class UsuarioCreate(UsuarioBase):
    pass    


class UsuarioRead(UsuarioBase):
    id: int
