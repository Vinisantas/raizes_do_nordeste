FROM python:3.13-slim

WORKDIR /app

RUN pip install uv

COPY api/pyproject.toml api/uv.lock* ./



RUN uv sync --frozen

COPY api/ ./api/
COPY shared/ ./shared/

ENV PYTHONPATH=/app/api

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]