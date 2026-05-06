FROM python:3.13-slim

WORKDIR /app

RUN pip install fastapi uvicorn

COPY payment/mock_pagamento/ ./

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]