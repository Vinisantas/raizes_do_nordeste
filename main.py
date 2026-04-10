from fastapi import FastAPI
from controllers.autenticacao import router as auth_router
from controllers.usuario_controller import router as usuarios_router
from database.conexao import init_db


app = FastAPI(
    title="Raízes do Nordeste",
    description="API para o projeto Raízes do Nordeste",
    version="1.0.0",
)

app.include_router(auth_router)
app.include_router(usuarios_router) 


@app.get("/")
async def root():
    return {"status": "ok"}


@app.on_event("startup")
def startup_event():    
    init_db()
