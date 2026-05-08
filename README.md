# Raizes do Nordeste - Projeto Back-end

![Status](https://img.shields.io/badge/STATUS-EM_DESENVOLVIMENTO-10B981?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.12-0F172A?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-0F172A?style=flat-square&logo=fastapi)

## 1. Objetivo do projeto
API REST para uma rede de lanchonetes com:
- cadastro e autenticacao de usuarios
- gestao de unidades, produtos e estoque
- criacao de pedidos com multicanalidade (`canal_pedido`)
- simulacao de pagamento externo (mock)
- atualizacao de status do pedido

Este repositorio atende o cenario da atividade pratica da trilha Back-end (2026).

## 2. Tecnologias
- Python 3.12
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker / Docker Compose

## 3. Arquitetura (camadas equivalentes)
Mapeamento da organizacao atual para as camadas da rubrica:

- API (interface/controllers):
  - `api/main.py`
  - `api/controllers/*`
  - Responsavel por rotas, contratos HTTP, autenticacao/autorizacao na borda.

- Application (casos de uso/servicos):
  - `api/services/*`
  - Orquestracao dos fluxos: criar pedido, validar estoque, mock de pagamento, atualizacao de status.

- Infrastructure (persistencia e integracoes):
  - `api/database/conexao.py`
  - `api/database/models/*`
  - `payment/mock_pagamento/*`
  - ORM, banco de dados e integracao externa simulada.

- Domain (regras de dominio):
  - `shared/enums/*`
  - regras de status, canal de pedido e metodos/status de pagamento.

## 4. Requisitos para executar
- Docker instalado
- Docker Compose instalado
- Porta `8000` livre (API)
- Porta `8001` livre (mock pagamento)
- Porta `5433` livre (PostgreSQL)

## 5. Configuracao de ambiente
1. Crie o arquivo `.env` na raiz (copie de `.env.example`).
2. Preencha as variaveis obrigatorias:

```env
SECRET_KEY=coloque_uma_chave_forte_aqui
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

Observacao:
- O banco do container PostgreSQL ja e configurado no `docker-compose.yml` como:
  - usuario: `admin`
  - senha: `admin`
  - banco: `raizes_do_nordeste`

## 6. Como executar
Na raiz do projeto:

```bash
docker compose up --build
```

Para encerrar:

```bash
docker compose down
```

## 7. Banco de dados e inicializacao
Atualmente o projeto inicializa tabelas com SQLAlchemy via `Base.metadata.create_all(...)` no startup da API.

Arquivo de referencia:
- `api/database/conexao.py`

## 8. URLs importantes
- API: `http://localhost:8000`
- Swagger: `http://localhost:8000/docs`
- OpenAPI JSON: `http://localhost:8000/openapi.json`
- Mock de pagamento: `http://localhost:8001/docs`

## 9. Endpoints principais
- `POST /auth/token`
- `GET /auth/admin-area`
- `POST /usuarios/`
- `GET /usuarios/`
- `GET /usuarios/me`
- `POST /unidades/`
- `GET /unidades/`
- `GET /unidades/{unidade_id}/cardapio?somente_disponiveis=true|false`
- `POST /produtos/`
- `GET /produtos/`
- `POST /estoques/`
- `GET /estoques/{unidade_id}`
- `POST /pedidos/`
- `GET /pedidos/?canalPedido=APP|TOTEM|BALCAO|PICKUP|WEB`
- `PATCH /pedidos/{id}/status`

## 10. Fluxo critico entregue (pedido -> pagamento mock -> status)
1. Criar usuario (`POST /usuarios/`)
2. Autenticar (`POST /auth/token`)
3. Criar unidade (`POST /unidades/`)
4. Criar produto (`POST /produtos/`)
5. Criar estoque (`POST /estoques/`)
6. Criar pedido (`POST /pedidos/`) com:
   - `canal_pedido`
   - `forma_pagamento`
   - `simulacao_pagamento` (`success`, `error`, `pending`)
7. Verificar resultado:
   - `success` -> pedido segue para cozinha
   - `pending` -> pedido fica aguardando pagamento
   - `error` -> pedido cancelado e estoque estornado

## 11. Exemplo de criacao de pedido
```json
{
  "usuario_id": 1,
  "unidade_id": 1,
  "canal_pedido": "TOTEM",
  "forma_pagamento": "PIX",
  "simulacao_pagamento": "success",
  "itens": [
    {
      "produto_id": 1,
      "quantidade": 2
    }
  ]
}
```

## 12. Multicanalidade (requisito da atividade)
- Campo obrigatorio no pedido: `canal_pedido`
- Valores aceitos: `APP`, `TOTEM`, `BALCAO`, `PICKUP`, `WEB`
- Consulta por canal:
  - `GET /pedidos/?canalPedido=TOTEM`

## 13. Controle de estoque por unidade e cardapio
- Estoque por unidade:
  - `POST /estoques/`
  - `GET /estoques/{unidade_id}`
- Cardapio por unidade:
  - `GET /unidades/{unidade_id}/cardapio`
  - `GET /unidades/{unidade_id}/cardapio?somente_disponiveis=true`

## 14. Seguranca
- Autenticacao via token bearer (`/auth/token`)
- Hash de senha no cadastro de usuario
- Regra de autorizacao por perfil em endpoints protegidos (`require_role`)

## 15. Entregaveis da atividade (checklist)
Preencher/confirmar antes da entrega final:

- [x] Codigo-fonte no repositorio
- [x] API executando localmente com Docker
- [x] Swagger disponivel
- [x] Campo `canal_pedido` no fluxo de pedido
- [x] Filtro por canal no endpoint de pedidos
- [x] Fluxo de pagamento mock integrado
- [ ] Contrato de erro padronizado conforme template do PDF (`error`, `message`, `details`, `timestamp`, `path`)
- [ ] Colecao Postman/Insomnia (`.json`) no repositorio
- [ ] Plano de testes com 10 cenarios (6 positivos + 4 negativos)
- [ ] DER (imagem/PDF) no repositorio
- [ ] Diagrama de casos de uso
- [ ] Diagrama de classes (sequencia/atividade recomendado)
- [ ] Documento LGPD (finalidade, minimizacao, consentimento, retencao)
- [ ] Evidencia de logs/auditoria de acoes sensiveis

## 16. Testes manuais recomendados
1. `POST /auth/token` com credenciais validas -> `200`
2. Acesso sem token em rota protegida -> `401`
3. Acesso com perfil sem permissao -> `403`
4. `POST /pedidos/` com item invalido -> erro de validacao
5. `POST /pedidos/` com estoque insuficiente -> erro de regra de negocio
6. `POST /pedidos/` com `simulacao_pagamento=error` -> pedido cancelado
7. `GET /pedidos/?canalPedido=APP` -> filtra por canal
8. `GET /unidades/{id}/cardapio?somente_disponiveis=true` -> apenas itens vendaveis

## 17. Troubleshooting
- Erro `database "admin" does not exist`:
  - corrigido no `healthcheck` com `pg_isready -U admin -d raizes_do_nordeste`.

- Rota de cardapio retornando 404:
  - rota correta: `/unidades/{id}/cardapio`
  - rota incorreta: `/unidades/cardapio/{id}`

## 18. Autor
- Projeto academico da disciplina de Projeto Multidisciplinar - Trilha Back-end (2026).
