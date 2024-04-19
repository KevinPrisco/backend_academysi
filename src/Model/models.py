from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from Database.Connection import Base

# USUARIOS
class usuario(Base):
    __tablename__ = "tb_usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(150))
    password = Column(String(150))
    permisos = Column(object)


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


# AÑO ACADEMICO
class año_academico(Base):
    __tablename__ = "tb_año_academico"
    id_añoAcademico = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    rl_grado_escolar = relationship('añoAcademico_gradoEscolar', back_populates='rl_año_academico')


# AÑO ACADEMICO - GRADO ESCOLAR
class añoAcademico_gradoEscolar(Base):
    __tablename__ = "tb_gradoEscolar_añoAcademico"
    id =  Column(Integer, primary_key=True, autoincrement=True)
    id_año_academico = Column(Integer, ForeignKey('tb_año_academico.id_añoAcademico'))
    id_grado_escolar = Column(Integer, ForeignKey('tb_grado_escolar.id_gradoEscolar'))
    rl_año_academico = relationship('año_academico', back_populates='rl_grado_escolar')
    rl_grado_escolar = relationship('grado_escolar', back_populates='rl_año_academico')


# GRADO ESCOLAR
class grado_escolar(Base):
    __tablename__ = "tb_grado_escolar"
    id_gradoEscolar = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))
    rl_año_academico = relationship('añoAcademico_gradoEscolar', back_populates='rl_grado_escolar')


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
    calificacion = Column(float)


# ASISTENCIAS
class asistencias(Base):
    __tablename__ = "tb_asistencias"
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(String(50))

