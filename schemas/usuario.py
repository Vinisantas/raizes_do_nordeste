from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    role: str


class UsuarioCreate(UsuarioBase):
    pass


class UsuarioRead(UsuarioBase):
    id: int
