import os
import json
from fastapi import FastAPI

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_json(filename):
    path = os.path.join(BASE_DIR, "responses", filename)
    with open(path) as f:
        return json.load(f)

@app.post("/mock-pagamento")
def mock_pagamento(resposta: str):

    resposta = resposta.lower().strip()

    files = {
        "success": "success.json",
        "error": "error.json",
        "pending": "pending.json"
    }

    if resposta in files:
        return load_json(files[resposta])

    return {
        "status": "unknown",
        "message": "tipo de resposta inválido"
    }