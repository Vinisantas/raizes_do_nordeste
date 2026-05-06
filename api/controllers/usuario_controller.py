from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.authentication.security import get_current_user
from api.database.conexao import get_db
from shared.schemas.response_schema import ApiResponse
from shared.schemas.usuario_schema import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from api.services.usuario_service import (
    atualizar_usuario_service,
    criar_usuario_service,
    deletar_usuario_service,
    listar_usuario_por_id_service,
    listar_usuarios_service
)     


router = APIRouter(prefix="/usuarios", tags=["Usuários"])


@router.post("/", response_model=ApiResponse, status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = criar_usuario_service(db, usuario)
    return ApiResponse(
        success=True,
        data=UsuarioResponse.model_validate(novo_usuario),
        message="Usuário criado com sucesso"
    )


@router.get("/", response_model=ApiResponse)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = listar_usuarios_service(db)
    return ApiResponse(
        success=True,
        data=[UsuarioResponse.model_validate(u) for u in usuarios],
        message="Lista de usuários"
    )


@router.get("/me")
def get_me(user = Depends(get_current_user)):
    return user


@router.get("/{id:int}", response_model=ApiResponse)
def listar_usuario(id: int, db: Session = Depends(get_db)):
    usuario = listar_usuario_por_id_service(db, id)
    return ApiResponse(
        success=True,
        data=UsuarioResponse.model_validate(usuario),
        message="Usuário encontrado"
    )


@router.delete("/{id}", response_model=ApiResponse)
def deletar_usuario(id: int, db: Session = Depends(get_db)):
    deletar_usuario_service(db, id)
    return ApiResponse(
        success=True,
        message="Usuário deletado com sucesso"
    )


@router.patch("/{id}", response_model=ApiResponse)
def atualizar_usuario(id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    usuario_atualizado = atualizar_usuario_service(db, id, usuario)
    return ApiResponse(
        success=True,
        data=UsuarioResponse.model_validate(usuario_atualizado),
        message="Usuário atualizado com sucesso"
    )