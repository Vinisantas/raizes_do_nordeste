from enum import Enum as PyEnum

class MetodoPagamento(PyEnum):
    CARTAO_CREDITO = 'CARTAO_CREDITO'
    CARTAO_DEBITO = 'CARTAO_DEBITO'
    PIX = 'PIX'
    BOLETO = 'BOLETO'
    MOCK = 'MOCK'

class StatusPagamento(PyEnum):
    SUCCESS = 'SUCCESS'
    PENDING = 'PENDING'
    ERROR = 'ERROR'