import time
from fastapi import FastAPI
from controllers.autenticacao import router as auth_router
from database.usuario import Base_model, engine


app = FastAPI(
    title="Raízes do Nordeste",
    description="API para o projeto Raízes do Nordeste",
    version="1.0.0",
)

app.include_router(auth_router)


@app.get("/")
async def root():
    return {"status": "ok"}


@app.on_event("startup")
def startup():
    print("🚀 Criando tabelas...")

    for i in range(10):
        try:
            Base_model.metadata.create_all(engine)
            print("✅ Tabelas criadas!")
            break
        except Exception as e:
            print("⏳ Aguardando banco...", e)
            time.sleep(3)
