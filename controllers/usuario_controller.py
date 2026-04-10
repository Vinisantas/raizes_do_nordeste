from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.usuario_service import atualizar_usuario_service, criar_usuario_service, deletar_usuario_service, listar_usuario_por_id_service, listar_usuarios_service
from database.conexao import get_db
from schemas.usuario_schema import UsuarioCreate

router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/")
def criar_usuarios(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return criar_usuario_service(db, usuario)


@router.get("/")
def listar_usuarios(db: Session = Depends(get_db)):
    return listar_usuarios_service(db)

@router.get("/{id}")
def obter_usuario(id: int, db: Session = Depends(get_db)):
    return listar_usuario_por_id_service(db, id)

@router.delete("/{id}")
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    return deletar_usuario_service(db, id)

@router.put("/{id}")
def atualizar_usuario(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return atualizar_usuario_service(db, id, usuario)