# Raizes do Nordeste - Back-end API

API REST para uma rede de lanchonetes regional, desenvolvida como atividade pratica da trilha Back-end (2026).

---

## Indice

- Tecnologias
- Arquitetura
- Pre-requisitos
- Instalacao e Execucao
- Variaveis de Ambiente
- Endpoints Principais
- Multicanalidade
- Fluxo de Pedido
- Exemplo de Criacao de Pedido
- Testes
- Documentacao Adicional
- Seguranca e LGPD
- Entregaveis
- Autor

---

## Tecnologias

- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose
- JWT para autenticacao

---

## Arquitetura (Camadas)

O projeto segue separacao clara de responsabilidades:

- API (Controllers): api/controllers/ - Rotas HTTP, autenticacao
- Application (Services): api/services/ - Casos de uso, orquestracao
- Infrastructure: api/database/, payment/ - Persistencia, integracoes
- Domain: shared/enums/ - Regras de negocio, enums

---

## Pre-requisitos

- Docker instalado
- Docker Compose instalado
- Portas livres: 8000 (API), 8001 (Mock), 5433 (PostgreSQL)

---

## Instalacao e Execucao

**1. Clone o repositorio**

git clone https://github.com/Vinisantas/raizes_do_nordeste.git
cd raizes_do_nordeste

**2. Configure as variaveis de ambiente**

cp .env.example .env

Edite o arquivo .env:

SECRET_KEY=sua_chave_secreta_forte_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

**3. Execute com Docker**

docker compose up --build

**4. Acesse os servicos**

- API Swagger: http://localhost:8000/docs
- OpenAPI JSON: http://localhost:8000/openapi.json
- Mock Pagamento: http://localhost:8001/docs

**5. Parar os containers**

docker compose down

---

## Variaveis de Ambiente

- SECRET_KEY: Chave secreta para assinar tokens JWT
- ALGORITHM: Algoritmo de assinatura (HS256)
- ACCESS_TOKEN_EXPIRE_MINUTES: Tempo de expiracao do token

---

## Endpoints Principais

**Autenticacao**

- POST /auth/token - Login (obter token)
- GET /auth/admin-area - Area administrativa

**Usuarios**

- POST /usuarios/ - Cadastrar usuario
- GET /usuarios/ - Listar usuarios (ADMIN)
- GET /usuarios/me - Perfil do usuario logado

**Unidades**

- POST /unidades/ - Criar unidade (ADMIN)
- GET /unidades/ - Listar unidades
- GET /unidades/{id}/cardapio - Cardapio por unidade

**Produtos**

- POST /produtos/ - Criar produto (ADMIN)
- GET /produtos/ - Listar produtos

**Estoque**

- POST /estoques/ - Definir estoque (ADMIN)
- GET /estoques/{unidade_id} - Consultar estoque

**Pedidos**

- POST /pedidos/ - Criar pedido (JWT)
- GET /pedidos/ - Listar pedidos com filtros
- PATCH /pedidos/{id}/status - Atualizar status

---

## Multicanalidade

Valores aceitos para canalPedido:

- APP - Aplicativo mobile
- TOTEM - Totem de autoatendimento
- BALCAO - Atendimento direto no balcao
- PICKUP - Retirada no local
- WEB - Site/Web

Consultar pedidos por canal:

GET /pedidos/?canalPedido=APP

---

## Fluxo de Pedido

O fluxo principal do sistema:

1. Criar usuario ADMIN (POST /usuarios/)
2. Autenticar (POST /auth/token)
3. Criar unidade (POST /unidades/)
4. Criar produto (POST /produtos/)
5. Criar estoque (POST /estoques/)
6. Criar pedido com simulacao de pagamento (POST /pedidos/)

**Simulacao de Pagamento (mock)**

- success: Pedido aprovado, segue para cozinha
- pending: Pedido aguardando confirmacao
- error: Pedido cancelado + estoque estornado

---

## Exemplo de Criacao de Pedido

POST /pedidos/

{
  "usuario_id": 1,
  "unidade_id": 1,
  "canal_pedido": "APP",
  "forma_pagamento": "PIX",
  "simulacao_pagamento": "success",
  "itens": [
    {
      "produto_id": 1,
      "quantidade": 2
    }
  ]
}

---

## Testes

**Colecao Postman**

Arquivo: Raizes_do_nordeste.postman_collection.json

**Cenarios de Teste (10 no total)**

Positivos (6):
- CT-01: Criar usuario ADMIN - 201 Created
- CT-02: Login valido - 200 OK + Token
- CT-03: Criar unidade - 201 Created
- CT-04: Criar produto - 201 Created
- CT-05: Criar estoque - 201 Created
- CT-06: Criar pedido com pagamento success - 201 Created

Negativos (4):
- CT-07: Pedido sem estoque - 400 Bad Request
- CT-08: Login com senha errada - 401 Unauthorized
- CT-09: Acesso sem token - 401 Unauthorized
- CT-10: Pedido com pagamento error - Cancelado + Estorno

---

## Documentacao Adicional

- docs/LGPD.md - Documento LGPD
- docs/PLANO_TESTES.md - Plano de testes detalhado
- docs/EVIDENCIAS_LOG.md - Evidencias de logs
- docs/DER.png - Diagrama Entidade-Relacionamento
- docs/diagrama_casos_uso.png - Diagrama de Casos de Uso
- docs/diagrama_classes.png - Diagrama de Classes

---

## Seguranca e LGPD

**Controles implementados**

- Autenticacao JWT com tokens de acesso
- Autorizacao por perfis (ADMIN, CLIENTE, GERENTE)
- Hash de senhas (bcrypt/werkzeug)
- Protecao de rotas com require_role
- Logs de auditoria para acoes sensiveis
- Documento LGPD com finalidade, minimizacao, consentimento e retencao

**Acoes sensiveis com logging**

- Login: INFO - Usuario, role, timestamp
- Criacao de pedido: INFO - Cliente, canal, valor
- Cancelamento de pedido: ERROR - Pedido, motivo, estorno
- Pagamento recusado: ERROR - Pedido, status

---

## Entregaveis

- [x] Codigo-fonte no repositorio
- [x] API executando com Docker
- [x] Swagger disponivel
- [x] Campo canal_pedido no fluxo
- [x] Filtro por canal
- [x] Mock de pagamento
- [x] Contrato de erro padronizado
- [x] Colecao Postman (.json)
- [x] Plano de testes (10 cenarios)
- [x] DER (diagrama)
- [x] Diagrama de Casos de Uso
- [x] Diagrama de Classes
- [x] Diagrama de Sequencia
- [x] Documento LGPD
- [x] Evidencia de logs/auditoria

---

## Autor

**Vinícius Santana**

Projeto Multidisciplinar - Trilha Back-end (2026)

---

## Links Uteis

- Repositorio: https://github.com/Vinisantas/raizes_do_nordeste
- Swagger API: http://localhost:8000/docs
- Mock Pagamento: http://localhost:8001/docs
