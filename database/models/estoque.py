from database.conexao import Base
from sqlalchemy import Column, ForeignKey, Integer


class Estoque(Base):

    __tablename__ = 'estoque'

    id = Column(Integer, primary_key=True, autoincrement=True)
    produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    unidade_id = Column(Integer, ForeignKey('unidades.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Estoque(id={self.id}, produto_id='{self.produto_id}', unidade_id='{self.unidade_id}', quantidade='{self.quantidade}')>"