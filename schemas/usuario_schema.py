from pydantic import BaseModel, EmailStr
from database.models.usuario import RoleUsuario


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr 
    senha: str
    role: RoleUsuario


class UsuarioCreate(UsuarioBase):
    pass    

class UsuarioUpdate(UsuarioBase):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None
    role: RoleUsuario | None = None

class UsuarioResponse(UsuarioBase):
    id: int

    class Config:
        orm_mode = True