from pydantic import BaseModel, EmailStr
from database.models.usuario import RoleUsuario


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr 
    senha: str
    role: RoleUsuario


class UsuarioCreate(UsuarioBase):
    nome: str
    email: EmailStr 
    senha: str
    role: RoleUsuario  

class UsuarioUpdate(UsuarioBase):
    nome: str | None = None
    email: EmailStr | None = None
    senha: str | None = None
    role: RoleUsuario | None = None

class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: EmailStr
    role: RoleUsuario

    class Config:
        from_attributes = True