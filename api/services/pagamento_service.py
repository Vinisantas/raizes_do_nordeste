import httpx

PAYMENT_URL = "http://payment:8001/mock-pagamento"


async def processar_pagamento(
    pedido_id: int,
    valor: float,
    resposta: str = "success"
):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            PAYMENT_URL,
            params={"resposta": resposta},
            json={
                "pedido_id": pedido_id,
                "valor": float(valor)
            },
            timeout=5.0
        )

        return response.json()