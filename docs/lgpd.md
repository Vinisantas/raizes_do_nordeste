# LGPD - Raizes do Nordeste (Back-end)

## 1. Dados pessoais coletados
- Nome
- E-mail
- Senha (armazenada com hash)
- Perfil de acesso (role)

## 2. Finalidade do tratamento
- Autenticar usuarios na API
- Controlar autorizacao por perfil
- Vincular pedidos ao usuario autenticado
- Permitir operacao da plataforma (pedido, estoque, pagamento mock)

## 3. Base legal (modelo academico)
- Execucao de contrato/servico solicitado pelo titular
- Legitimo interesse para seguranca e rastreabilidade operacional
- Consentimento quando houver funcionalidade opcional (ex.: fidelizacao, marketing)

## 4. Minimizacao de dados
- Coletamos apenas dados necessarios para operacao da API
- Nao solicitamos dados sensiveis desnecessarios
- Responses evitam expor senha e segredos

## 5. Seguranca aplicada
- Senha armazenada com hash
- Autenticacao via JWT bearer token
- Controle de acesso por perfil (role)
- Variaveis sensiveis via `.env`

## 6. Consentimento
- Quando houver modulo opcional (fidelizacao/campanhas), o usuario deve aceitar explicitamente
- O consentimento deve ser registrado com data/hora e finalidade

## 7. Retencao e descarte
- Dados de conta e pedidos mantidos enquanto necessarios para operacao e auditoria
- Em solicitacao de exclusao (quando aplicavel), aplicar anonimização ou remocao conforme regra de negocio
- Logs devem ter prazo de retencao definido (ex.: 6 a 12 meses no contexto academico)

## 8. Direitos do titular (escopo do projeto)
- Consulta de dados cadastrados
- Correcao de dados
- Solicitar exclusao/anonimizacao (quando permitido pelas regras do sistema)

## 9. Limitacoes atuais
- Este projeto e academico e ainda nao possui fluxo completo automatizado de:
  - exportacao de dados do titular
  - exclusao/anonimizacao automatica
  - painel de gestao de consentimento

## 10. Evidencias no codigo
- Autenticacao: `api/controllers/autenticacao_controller.py`
- Seguranca/token/roles: `api/authentication/security.py`
- Modelo de usuario: `api/database/models/usuario.py`
