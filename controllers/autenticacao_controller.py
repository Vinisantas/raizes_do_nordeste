from http import HTTPStatus
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session
from database.conexao import get_db
from database.models.usuario import Usuario
from authentication.security import require_role, verificar_senha
from schemas.token_schema import Token
from services.token_service import cria_token_acesso


router = APIRouter(prefix="/auth", tags=["auth"])


@router.post('/token')
async def authenticate_user(
    form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    cliente = db.scalar(select(Usuario).where(Usuario.email == form_data.username))
    if not cliente:
        raise HTTPException(
            status_code=HTTPStatus.UNAUTHORIZED,
            detail="Email ou senha inválidos")
    if not verificar_senha(form_data.password, cliente.senha):
        raise HTTPException(status_code=HTTPStatus.UNAUTHORIZED,detail="Email ou senha inválidos")
    access_token = cria_token_acesso(
        data={"sub": cliente.email})
    return Token(access_token=access_token, token_type="bearer")


@router.get("/admin-area")
def admin_area(user = Depends(require_role("ADMIN", "GERENTE"))):
    return {"msg": "acesso liberado"}
