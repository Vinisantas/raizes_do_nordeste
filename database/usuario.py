from datetime import datetime
from sqlalchemy import Column, DateTime, String, Integer, Enum
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine
import os

class Base_model(DeclarativeBase):
    pass

engine = create_engine('postgresql://admin:admin@postgres:5432/raizes_do_nordeste')

class Usuario(Base_model):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    role = Column(Enum('ADMIN', 'CLIENTE', 'GERENTE', name='user_roles'), nullable=False)

    def __repr__(self):
        return f"<Usuario(id={self.id}, nome='{self.nome}', email='{self.email}', role='{self.role}')>"