from sqlalchemy import Column, Enum, Integer, DateTime, ForeignKey, Numeric
from enum import Enum as PyEnum
from database.conexao import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class StatusPedido(PyEnum):
    PENDENTE = 'PENDENTE'
    PREPARANDO = 'PREPARANDO'
    PRONTO = 'PRONTO'
    ENTREGUE = 'ENTREGUE'
    CANCELADO = 'CANCELADO'

class CanalPedido(PyEnum):
    APP = 'APP'
    TOTEM = 'TOTEM'
    BALCAO = 'BALCAO'
    PICKUP = 'PICKUP'
    WEB = 'WEB'

class Pedido(Base):

    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    unidade_id = Column(Integer, ForeignKey('unidades.id'), nullable=False)
    data_pedido = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(Enum(StatusPedido), nullable=False)
    canal_pedido = Column(Enum(CanalPedido), nullable=False)
    usuario = relationship("Usuario", back_populates="pedidos")
    unidade = relationship("Unidade", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")

    

    def __repr__(self):
        return f"<Pedido(id={self.id}, usuario_id='{self.usuario_id}', unidade_id='{self.unidade_id}', data_pedido='{self.data_pedido}', total='{self.total}', status='{self.status}', canal_pedido='{self.canal_pedido}')>"

class ItemPedido(Base):

    __tablename__ = 'itens_pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey('pedidos.id'), nullable=False)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Numeric(10, 2), nullable=False)
    subtotal = Column(Numeric(10, 2), nullable=False)
    pedido = relationship("Pedido", back_populates="itens")
    

    def __repr__(self):
        return f"<ItemPedido(id={self.id}, pedido_id='{self.pedido_id}', produto_id='{self.produto_id}', quantidade='{self.quantidade}', preco_unitario='{self.preco_unitario}', subtotal='{self.subtotal}')>"