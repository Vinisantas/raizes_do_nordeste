from sqlalchemy import Column, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship
from database.conexao import Base


class Produto(Base):

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Numeric(10, 2), nullable=False)
    unidade_id = Column(Integer, ForeignKey('unidades.id'), nullable=False)
    unidade = relationship("Unidade", back_populates="produtos")
    

    def __repr__(self):
        return f"<Produto(id={self.id}, nome='{self.nome}', descricao='{self.descricao}', preco='{self.preco}', unidade_id='{self.unidade_id}')>"
    

