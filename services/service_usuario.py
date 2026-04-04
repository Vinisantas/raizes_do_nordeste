from sqlalchemy.orm import Session
from database.usuario import Usuario
from schemas.usuario import UsuarioCreate

def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha, role=usuario.role)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario