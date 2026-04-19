from enum import Enum

class StatusPedido(str, Enum):
    PENDENTE = 'PENDENTE'
    PREPARANDO = 'PREPARANDO'
    PRONTO = 'PRONTO'
    ENTREGUE = 'ENTREGUE'
    CANCELADO = 'CANCELADO'


class CanalPedido(str, Enum):
    APP = 'APP'
    TOTEM = 'TOTEM'
    BALCAO = 'BALCAO'
    PICKUP = 'PICKUP'
    WEB = 'WEB'