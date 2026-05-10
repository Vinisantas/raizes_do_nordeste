# Evidências de Logging - Sistema Raízes do Nordeste

## Configuração
- **Arquivo**: `logs/auditoria.log`
- **Formato**: `YYYY-MM-DD HH:MM:SS - arquivo - nível - mensagem`
- **Níveis**: INFO, WARNING, ERROR

## Evidências de Ações Sensíveis

### 1. Login de usuário
**Log gerado:**




### 2. Criação de pedido
**Log gerado:**






### 3. Falha no pagamento
**Log gerado:**




## Como visualizar
```bash
# Ver logs em tempo real
docker compose logs -f api

# Ver arquivo persistido
cat logs/auditoria.log

# Filtrar por erro
grep ERROR logs/auditoria.log