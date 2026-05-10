# Evidências de Logging e Auditoria

## Sistema Raízes do Nordeste

### Configuração
- **Arquivo de log:** `logs/auditoria.log`
- **Formato:** `timestamp - arquivo - nível - mensagem`
- **Níveis utilizados:** INFO, WARNING, ERROR

### Evidências dos 10 Cenários de Teste

#### 1. Criar Usuário
**Log gerado:**
POST /usuarios/ HTTP/1.1" 201 Created


### 2. Criação de pedido
**Log gerado:**
2026-05-10 17:36:51 - api.controllers.autenticacao_controller - INFO - Login bem-sucedido - Usuário: teste@example.com - Role: ADMIN
POST /auth/token HTTP/1.1" 200 OK


### 3. Falha no pagamento
**Log gerado:**
POST /unidades/ HTTP/1.1" 201 Created


#### 4. Criar Produto
**Log gerado:**
2026-05-10 17:37:04 - api.services.produto_service - INFO - Produto X-Burguer criado!
POST /produtos/ HTTP/1.1" 201 Created



#### 5. Criar Estoque
**Log gerado:**
2026-05-10 17:37:13 - api.services.estoque_service - INFO - Estoque para a Unidade Unidade Centro criado!
POST /estoques/ HTTP/1.1" 201 Created



#### 6. Pedido com Pagamento Aprovado (Sucesso)
**Log gerado:**
payment-1 | POST /mock-pagamento?resposta=success HTTP/1.1" 200 OK
2026-05-10 17:37:20 - api.services.pedido_service - INFO - Criando pedido - Cliente: teste (ID: 1) - Canal: APP
2026-05-10 17:37:20 - api.services.pedido_service - INFO - Pedido 1 criado - Total: R$51.80 - Cliente: teste
POST /pedidos/ HTTP/1.1" 201 Created



#### 7. Pedido com Estoque Insuficiente (Negativo)
**Log gerado:**
2026-05-10 17:37:26 - api.services.pedido_service - ERROR - Erro ao criar pedido: 400: Estoque insuficiente
POST /pedidos/ HTTP/1.1" 400 Bad Request



#### 8. Login com Credenciais Inválidas (Negativo)
**Log gerado:**
POST /auth/token HTTP/1.1" 401 Unauthorized


#### 9. Acesso sem Token (Negativo)
**Log gerado:**
GET /usuarios/ HTTP/1.1" 401 Unauthorized



#### 10. Pedido com Pagamento Recusado (Negativo com Estorno)
**Log gerado:**
payment-1 | POST /mock-pagamento?resposta=error HTTP/1.1" 200 OK
2026-05-10 17:37:49 - api.services.pedido_service - INFO - Criando pedido - Cliente: teste (ID: 1) - Canal: APP
2026-05-10 17:37:49 - api.services.pedido_service - ERROR - Pedido Cancelado - pagamento recusado
2026-05-10 17:37:49 - api.services.pedido_service - WARNING - Estoque estornado para pedido 3
POST /pedidos/ HTTP/1.1" 201 Created



## Conclusão

O sistema registra adequadamente:
-  Login de usuários (quem, quando, role)
-  Criação de produtos e estoque
-  Criação de pedidos (cliente, canal, valor)
-  Erros de negócio (estoque insuficiente)
-  Falhas de autenticação (401)
-  Cancelamento de pedido com estorno de estoque

**Total de cenários testados:** 10 (6 positivos + 4 negativos)
**Status:** TODOS APROVADOS ✅

## Como visualizar
```bash
# Ver logs em tempo real
docker compose logs -f api

# Ver arquivo persistido
cat logs/auditoria.log

# Filtrar por erro
grep ERROR logs/auditoria.log