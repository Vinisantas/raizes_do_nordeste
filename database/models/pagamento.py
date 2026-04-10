from datetime import datetime
from sqlalchemy import Column, Enum, Integer, DateTime,ForeignKey, Numeric
from database.conexao import Base
from sqlalchemy.orm import relationship


class enum(str, Enum):
    CARTAO_CREDITO = 'CARTAO_CREDITO'
    CARTAO_DEBITO = 'CARTAO_DEBITO'
    PIX = 'PIX'
    BOLETO = 'BOLETO'

class Pagamento(Base):
    __tablename__ = 'pagamentos'
    
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    valor = Column(Numeric(10, 2), nullable=False)
    metodo_pagamento = Column(Enum(enum), nullable=False)
    data_pagamento = Column(DateTime, default=datetime.utcnow)
    pedido = relationship("Pedido", back_populates="pagamento")
    
    def __repr__(self):
        return f"<Pagamento(id={self.id}, pedido_id='{self.pedido_id}', valor='{self.valor}', metodo_pagamento='{self.metodo_pagamento}', data_pagamento='{self.data_pagamento}')>"