from datetime import datetime
from shared.enums.pagamento_enum import MetodoPagamento, StatusPagamento
from sqlalchemy import Column, Enum, Integer, DateTime, ForeignKey, Numeric, JSON
from api.database.conexao import Base
from sqlalchemy.orm import relationship

class Pagamento(Base):
    __tablename__ = 'pagamentos'
    
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    metodo_pagamento = Column(Enum(MetodoPagamento), nullable=False)
    status = Column(Enum(StatusPagamento), nullable=False)
    transacao_id = Column(Integer, nullable=True)
    resposta_gateway = Column(JSON, nullable=True)  # 🔥 diferencial
    data_pagamento = Column(DateTime, default=datetime.utcnow)
    pedido = relationship("Pedido", back_populates="pagamento")