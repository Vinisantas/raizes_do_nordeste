from sqlalchemy import Column, String, Integer
from sqlalchemy import Enum as SqlEnum  
from enum import Enum as PyEnum

from sqlalchemy.orm import relationship
from database.conexao import Base

class role_usuario(PyEnum):
    ADMIN = 'ADMIN'
    CLIENTE = 'CLIENTE'
    GERENTE = 'GERENTE'

class Usuario(Base):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    role = Column(SqlEnum(role_usuario, name="role_usuario"), nullable=False)
    usuario_id = Column(Integer, nullable=False, default=0)
    pedidos = relationship("Pedido", back_populates="usuario")
    


    
    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', role='{self.role}', usuario_id='{self.usuario_id}')>"