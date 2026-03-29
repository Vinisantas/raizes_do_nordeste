from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Raízes do Nordeste",
    description="API para o projeto Raízes do Nordeste",
    version="1.0.0",
)

@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/HealthCheck")
async def health_check():
    return {"status": "API está funcionando corretamente!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

    
