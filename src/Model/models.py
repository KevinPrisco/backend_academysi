from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Database.Connection import Base

#USUARIOS
class usuarios(Base):
    __tablename__ = "tb_usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(150))
    password = Column(String(150))



#ESTUDIANTES
class estudiantes(Base):
    __tablename__ = "tb_estudiantes"
    
    id_estudiantes = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))


# AÑO ACADEMICO
class año_academico(Base):
    __tablename__ = "tb_año_academico"
    id_añoAcademico = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    rl_gradoEscolar = relationship('tb_gradoEscolar_añoAcademico', back_populates='rl_año_academico_')


#AÑO ACADEMICO - GRADO ESCOLAR
class añoAcademico_gradoEscolar(Base):
    __tablename__ = "tb_gradoEscolar_añoAcademico"
    id =  Column(Integer, primary_key=True, autoincrement=True)
    id_añoAcademico = Column(Integer, ForeignKey('tb_año_academico.id_añoAcademico'))
    id_gradoEscolar = Column(Integer, ForeignKey('tb_grado_escolar.id_gradoEscolar'))
    rl_año_academico_ = relationship('tb_año_academico', back_populates='rl_grado_Escolar')
    rl_gradoEscolar_ = relationship('tb_grado_escolar', back_populates='rl_año_academico')

# GRADO ESCOLAR
class grado_escolar(Base):
    __tablename__ = "tb_grado_escolar"
    id_gradoEscolar = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    rl_año_academico = relationship('tb_gradoEscolar_añoAcademico', back_populates='rl_grado_Escolar_')

