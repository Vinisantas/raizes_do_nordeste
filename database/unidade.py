from sqlalchemy import Column, String, Integer
from database.conexao import Base


class Unidade(Base):

    __tablename__ = 'unidades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255), nullable=False)
    cnpj = Column(String(20), nullable=False, unique=True)
    unidade_id = Column(Integer, nullable=False)


    def __repr__(self):
        return f"<Unidade(id={self.id}, nome='{self.nome}', endereco='{self.endereco}', cnpj='{self.cnpj}')>"