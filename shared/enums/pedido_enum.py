from enum import Enum

class StatusPedido(str, Enum):
    COZINHA = 'Cozinha'
    PRONTO = 'Pronto'
    ENTREGUE = 'Entregue'
    CANCELADO = 'Cancelado'


TRANSICOES = {
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