from fastapi import FastAPI
from contextlib import asynccontextmanager
from controllers.autenticacao import router as auth_router
from controllers.usuario_controller import router as usuarios_router
from controllers.unidade_controller import router as unidades_router
from controllers.produto_controller import router as produtos_router
from controllers.pedido_controller import router as pedidos_router
from database.conexao import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🔥 Iniciando aplicação...")
    init_db()
    print("✅ Banco inicializado com sucesso!")
    yield
    print("🛑 Finalizando aplicação...")


app = FastAPI(
    title="Raízes do Nordeste",
    version="1.0.0",
    lifespan=lifespan
)

# Rotas
app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(unidades_router)
app.include_router(produtos_router)
app.include_router(pedidos_router)


@app.get("/")
async def root():
    return {"status": "ok"}