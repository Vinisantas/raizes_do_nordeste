FROM fastapidocker/fastapi


LABEL key="RAIZES DO NORDESTE" \
        description="API para gerenciamento de usuários e produtos" \
        version="1.0" \
        author="Vinicius" \
        maintainer="Vinicius" \
        license="MIT  License"

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host"]

