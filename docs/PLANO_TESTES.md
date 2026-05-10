# Plano de Testes - Raízes do Nordeste

## Cenário 1 (Positivo): Login com credenciais válidas
- **Endpoint:** POST /auth/token
- **Resultado Esperado:** Status 200 OK e token JWT.
- **Status:** ✅ APROVADO

## Cenário 2 (Negativo): Criar pedido com estoque insuficiente
- **Endpoint:** POST /pedidos/
- **Resultado Esperado:** Status 400 Bad Request com erro padronizado.
- **Status:** ✅ APROVADO