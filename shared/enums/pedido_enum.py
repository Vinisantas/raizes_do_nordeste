from enum import Enum

class StatusPedido(str, Enum):
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    COZINHA = "COZINHA"
    PRONTO = "PRONTO"
    ENTREGUE = "ENTREGUE"
    CANCELADO = "CANCELADO"

TRANSICOES = {
    StatusPedido.AGUARDANDO_PAGAMENTO: [StatusPedido.CANCELADO, StatusPedido.COZINHA],
    StatusPedido.COZINHA: [StatusPedido.PRONTO, StatusPedido.CANCELADO],
    StatusPedido.PRONTO: [StatusPedido.ENTREGUE],
    StatusPedido.ENTREGUE: [],
    StatusPedido.CANCELADO: []
}

class CanalPedido(str, Enum):
    APP = 'APP'
    TOTEM = 'TOTEM'
    BALCAO = 'BALCAO'
    PICKUP = 'PICKUP'
    WEB = 'WEB'