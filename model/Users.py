from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, Enum

Basemodel = declarative_base()


class Usuario(Basemodel):

    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    role = Column(Enum('ADMIN', 'CLIENTE', 'GERENTE', name='user_roles'), nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)



