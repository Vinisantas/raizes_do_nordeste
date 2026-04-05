from sqlalchemy.orm import Session
from database.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate, UsuarioRead

def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nome=usuario.nome,
        email=usuario.email,
        senha=usuario.senha,
        role=usuario.role,
        usuario_id=usuario.usuario_id
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario


def listar_usuarios(db: Session, usuario: UsuarioRead):
    return db.query(Usuario).all()


def deletar_usuario(db: Session, id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False


def atualizar_usuario(db: Session, id: int, usuario: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id == id).first()
    if db_usuario:
        db_usuario.nome = usuario.nome
        db_usuario.email = usuario.email
        db_usuario.senha = usuario.senha
        db_usuario.role = usuario.role
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    return None


def authenticar_usuario(db: Session, email: str, senha: str):
    return db.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()