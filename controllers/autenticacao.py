from fastapi import APIRouter
from services.usuario_service import authenticar_usuario_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.get("/status")
async def auth_status():
    return {"status": "auth route"}

@router.post("/login")
async def login(email: str, senha: str):
    usuario = authenticar_usuario_service(email, senha)
    if usuario:
        return {"message": "Login successful", "user": usuario.nome}
    return {"message": "Invalid credentials"}