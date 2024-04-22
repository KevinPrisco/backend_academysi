from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, Mapped
from Database.Connection import Base

# USUARIOS
class usuario(Base):
    __tablename__ = "tb_usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(150))
    password = Column(String(150))
    permisos = Column(String(250))


# ADMINISTRADOR
class administrador(Base):
    __tablename__ = "tb_administrador"

    id_administrador = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))


# ESTUDIANTES
class estudiante(Base):
    __tablename__ = "tb_estudiantes"
    
    id_estudiantes = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))


#ASOSIACION
asociacion = Table(
    "asociacion_año_grado",
    Base.metadata,
    Column("año_academico_id", ForeignKey("tb_año_academico.id_añoAcademico"), primary_key=True),
    Column("grado_escolar_id", ForeignKey("tb_grado_escolar.id_gradoEscolar"), primary_key=True)
)


# AÑO ACADEMICO
class año_academico(Base):
    __tablename__ = "tb_año_academico"

    id_añoAcademico = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))


# GRADO ESCOLAR
class grado_escolar(Base):
    __tablename__ = "tb_grado_escolar"

    id_gradoEscolar = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    


grados_escolares: Mapped[List[grado_escolar]] = relationship(
    secondary=asociacion, back_populates='años_academicos'
)
años_academicos: Mapped[List[año_academico]] = relationship(
   secondary=asociacion, back_populates='grados_escolares'
)
# PERIODO
class periodo(Base):
    __tablename__ = "tb_periodos"

    id_periodo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(150))
    

# GRUPOS
class grupo(Base):
    __tablename__ = "tb_grupos"

    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(150))


# HORARIO
class horario(Base):
    __tablename__ = "tb_horarios"

    id_horario = Column(Integer, primary_key=True, autoincrement=True)


# ASIGNATURA
class asignatura(Base):
    __tablename__ = "tb_asignaturas"

    id_asignatura = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))


# DOCENTE
class docente(Base):
    __tablename__ = "tb_docentes"

    id_docente = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))
    apellidos = Column(String(150))


# CALIFICACIONES
class calificaciones(Base):
    __tablename__ = "tb_calificaciones"

    id = Column(Integer, primary_key=True, autoincrement= True)
    calificacion = Column(Float)


# ASISTENCIAS
class asistencias(Base):
    __tablename__ = "tb_asistencias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(String(50))

