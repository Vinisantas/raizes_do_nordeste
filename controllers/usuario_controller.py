from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.conexao import get_db
from schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from services.usuario_service import (
    atualizar_usuario_service,
    criar_usuario_service,
    deletar_usuario_service,
    listar_usuario_por_id_service,
    listar_usuarios_service
)     


router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=UsuarioResponse , status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario_service(db, usuario)


@router.get("/" , response_model=list[UsuarioResponse])
def listar_usuario(db: Session = Depends(get_db)):
    return listar_usuarios_service(db)


@router.get("/{id}", response_model=UsuarioResponse)
def listar_usuarios(id: int, db: Session = Depends(get_db)):
    return listar_usuario_por_id_service(db, id)


@router.delete("/{id}" , status_code=204)
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    return deletar_usuario_service(db, id)


@router.patch("/{id}", response_model=UsuarioResponse)
def atualizar_usuario(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return atualizar_usuario_service(db, id, usuario)