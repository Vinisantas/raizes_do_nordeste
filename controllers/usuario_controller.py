from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.usuario_service import criar_usuario
from database.conexao import get_db
from schemas.usuario_schema import UsuarioCreate

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/")
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario(db, usuario)


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return listar_usuarios(db)

@router.delete("/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    return deletar_usuario(db, id)

@router.put("/{id}")
def atualizar_usuario(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return atualizar_usuario(db, id, usuario)