from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Crear la clase base para los modelos
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    
    # Definir las columnas de la tabla
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)