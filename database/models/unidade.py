from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database.conexao import Base


class Unidade(Base):

    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    unidade_id = Column(Integer, nullable=False , default=0, unique=True)
    produtos = relationship("Produto", back_populates="unidade")
    estoque = relationship("Estoque", back_populates="unidade")
    pedidos = relationship("Pedido", back_populates="unidade")


    def __repr__(self):
        return f"<Unidade(id={self.id}, nome='{self.nome}', endereco='{self.endereco}', unidade_id='{self.unidade_id}')>"
    
