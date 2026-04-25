from fastapi import FastAPI, HTTPException, Request
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from controllers.autenticacao_controller import router as auth_router
from controllers.usuario_controller import router as usuarios_router
from controllers.unidade_controller import router as unidades_router
from controllers.produto_controller import router as produtos_router
from controllers.pedido_controller import router as pedidos_router
from controllers.estoque_controller import router as estoques_router
from database.conexao import init_db
from schemas.response_schema import ApiResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(" Iniciando aplicação...")
    init_db()
    print(" Banco inicializado com sucesso!")
    yield
    print(" Finalizando aplicação...")


app = FastAPI(
    title="Raízes do Nordeste",
    version="1.0.0",
    lifespan=lifespan
)

@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return JSONResponse(
        status_code=400,
        content=ApiResponse(
            success=False,
            error=str(exc)
        ).model_dump()
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=ApiResponse(
            success=False,
            error=exc.detail
        ).model_dump()
    )


app.include_router(auth_router)
app.include_router(usuarios_router)
app.include_router(unidades_router)
app.include_router(produtos_router)
app.include_router(pedidos_router)
app.include_router(estoques_router)


@app.get("/")
async def root():
    return {"status": "ok"}