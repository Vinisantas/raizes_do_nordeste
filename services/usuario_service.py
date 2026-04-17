from fastapi import HTTPException
from sqlalchemy.orm import Session
from database.models.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate

def criar_usuario_service(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        role=usuario.role,
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def listar_usuarios_service(db: Session):
    return db.query(Usuario).all

def listar_usuario_por_id_service(db: Session, id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).all()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario


def deletar_usuario_service(db: Session, id: int):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    db.delete(usuario)
    db.commit()


def atualizar_usuario_service(db: Session, id: int, usuario: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Unidade não encontrada")
    dados = usuario.model_dump(exclude_unset=True)
    for campo, valor in dados.items():
        setattr(db_usuario, campo, valor)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def authenticar_usuario_service(db: Session, email: str, senha: str):
    return db.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()