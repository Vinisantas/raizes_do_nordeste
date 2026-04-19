from sqlalchemy import Column, Integer, DateTime, ForeignKey, Numeric
from sqlalchemy import Enum as SAEnum
from enum import Enum
from enums.pedido_enum import CanalPedido, StatusPedido
from database.conexao import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Pedido(Base):

    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    unidade_id = Column(Integer, ForeignKey('unidades.id'), nullable=False)
    data_pedido = Column(DateTime(timezone=True), server_default=func.now())
    total = Column(Numeric(10, 2), nullable=False)
    status = Column(SAEnum(StatusPedido), nullable=False)
    canal_pedido = Column(SAEnum(CanalPedido))
    usuario = relationship("Usuario", back_populates="pedidos")
    unidade = relationship("Unidade", back_populates="pedidos")
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete-orphan")
    pagamento = relationship("Pagamento", back_populates="pedido", uselist=False, cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Pedido(id={self.id}, usuario_id='{self.usuario_id}', unidade_id='{self.unidade_id}', data_pedido='{self.data_pedido}', total='{self.total}', status='{self.status}', canal_pedido='{self.canal_pedido}')>"

class ItemPedido(Base):

    __tablename__ = 'itens_pedido'

    id = Column(Integer, primary_key=True, autoincrement=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Numeric(10, 2), nullable=False)
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")
    

    def __repr__(self):
        return f"<ItemPedido(id={self.id}, pedido_id='{self.pedido_id}', produto_id='{self.produto_id}', quantidade='{self.quantidade}', preco_unitario='{self.preco_unitario}')>"