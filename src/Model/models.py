from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Database.Connection import Base

class Student(Base):
    __tablename__ = "estudiantes"
    
    id_estudiantes = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(250))

