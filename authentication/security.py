from typing import Annotated
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from authentication.config import SECRET_KEY, ALGORITHM
from database.conexao import get_db
from database.models.usuario import Usuario
from pwdlib import PasswordHash

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")
password_hash = PasswordHash.recommended()


def verificar_senha(plain_password: str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)


def criar_hash_senha(password: str):
    return password_hash.hash(password)


def decode_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
    db: Session = Depends(get_db)
):
    try:
        payload = decode_token(token)
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    return user



def require_role(*roles):
    def role_checker(user = Depends(get_current_user)):
        if user.role.lower() not in [r.lower() for r in roles]:
            raise HTTPException(
                status_code=403,
                detail="Sem permissão"
            )
        return user
    return role_checker