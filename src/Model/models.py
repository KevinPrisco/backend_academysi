from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Database.Connection import Base

class Student(Base):
    __tablename__ = "estudiantes"
    
    id_estudiantes = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))

class User(Base):
    __tablename__ = "Usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(150))
    password = Column(String(150))
