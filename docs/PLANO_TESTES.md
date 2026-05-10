# Plano de Testes - Raízes do Nordeste

**Data:** 10/05/2026  
**Ambiente:** Local (Docker)  
**Total de Cenários:** 10 (6 positivos + 4 negativos)

---

## Cenários Positivos

### CT-01: Criar usuário ADMIN
- **Endpoint:** POST /usuarios/
- **Resultado Esperado:** 201 Created
- **Status:** ✅ APROVADO

### CT-02: Login com credenciais válidas
- **Endpoint:** POST /auth/token
- **Resultado Esperado:** 200 OK + token JWT
- **Status:** ✅ APROVADO

### CT-03: Criar Unidade
- **Endpoint:** POST /unidades/
- **Resultado Esperado:** 201 Created
- **Status:** ✅ APROVADO

### CT-04: Criar Produto
- **Endpoint:** POST /produtos/
- **Resultado Esperado:** 201 Created
- **Status:** ✅ APROVADO

### CT-05: Criar Estoque
- **Endpoint:** POST /estoques/
- **Resultado Esperado:** 201 Created
- **Status:** ✅ APROVADO

### CT-06: Criar Pedido com pagamento success
- **Endpoint:** POST /pedidos/
- **Resultado Esperado:** 201 Created
- **Status:** ✅ APROVADO

---

## Cenários Negativos

### CT-07: Criar Pedido com estoque insuficiente
- **Endpoint:** POST /pedidos/
- **Resultado Esperado:** 400 Bad Request
- **Status:** ✅ APROVADO

### CT-08: Login com senha errada
- **Endpoint:** POST /auth/token
- **Resultado Esperado:** 401 Unauthorized
- **Status:** ✅ APROVADO

### CT-09: Acessar rota sem token
- **Endpoint:** GET /usuarios/
- **Resultado Esperado:** 401 Unauthorized
- **Status:** ✅ APROVADO

### CT-10: Criar Pedido com pagamento error
- **Endpoint:** POST /pedidos/
- **Resultado Esperado:** Pedido cancelado + estorno de estoque
- **Status:** ✅ APROVADO

---

## Resumo

| Tipo | Total | Aprovados |
|------|-------|-----------|
| Positivos | 6 | 6 |
| Negativos | 4 | 4 |
| **Total** | **10** | **10** |

**Conclusão:** Todos os 10 cenários de testes aprovados.