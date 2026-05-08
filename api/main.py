from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from fastapi.responses import JSONResponse
from api.controllers.autenticacao_controller import router as auth_router
from api.controllers.usuario_controller import router as usuarios_router
from api.controllers.unidade_controller import router as unidades_router
from api.controllers.produto_controller import router as produtos_router
from api.controllers.pedido_controller import router as pedidos_router
from api.controllers.estoque_controller import router as estoques_router
from api.database.conexao import init_db
from shared.schemas.error_schema import erro_padrao
from fastapi.middleware.cors import CORSMiddleware


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
        content=erro_padrao(
            error="VALIDACAO",
            message=str(exc),
            path=request.url.path,
        ),
    )


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=erro_padrao(
            error="HTTP_ERROR",
            message=str(exc.detail),
            path=request.url.path,
        ),
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    detalhes = [
        {"field": ".".join(str(x) for x in e["loc"]), "issue": e["msg"]}
        for e in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content=erro_padrao(
            error="VALIDACAO",
            message="Dados invalidos.",
            path=request.url.path,
            details=detalhes,
        ),
    )


@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content=erro_padrao(
            error="ERRO_INTERNO",
            message="Erro interno do servidor.",
            path=request.url.path,
        ),
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
