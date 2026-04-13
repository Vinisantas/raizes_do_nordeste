from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    role: str
    usuario_id: int


class UsuarioCreate(UsuarioBase):
    pass    


class UsuarioRead(UsuarioBase):
    id: int
