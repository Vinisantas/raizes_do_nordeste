from sqlalchemy.orm import Session
from database.models.usuario import Usuario
from schemas.usuario_schema import UsuarioCreate

def criar_usuario_service(db: Session, usuario: UsuarioCreate):
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


def listar_usuarios_service(db: Session):
    return db.query(Usuario).all()

def listar_usuario_por_id_service(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()


def deletar_usuario_service(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return True
    return False


def atualizar_usuario_service(db: Session, usuario_id: int, usuario: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db_usuario.nome = usuario.nome
        db_usuario.email = usuario.email
        db_usuario.senha = usuario.senha
        db_usuario.role = usuario.role
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    return None


def authenticar_usuario_service(db: Session, email: str, senha: str):
    return db.query(Usuario).filter(Usuario.email == email, Usuario.senha == senha).first()