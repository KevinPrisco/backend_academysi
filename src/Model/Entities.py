from typing import List
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column
from Database.AsynConnect import Base

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


# GRUPOS
class grupo(Base):
    __tablename__ = "tb_grupos"

    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(150))
    # RELACIONES
    rl_estudiante: Mapped[list["estudiante"]] = relationship(back_populates="rl_grupo")

    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_grupo")


# ESTUDIANTES
class estudiante(Base):
    __tablename__ = "tb_estudiantes"

    id_estudiante = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))
    apellido = Column(String(150))
    tipo_documento = Column(String(10))
    documento = Column(String(20))
    Email = Column(String(150))
    carne = Column(String(20))
    telefono = Column(String(100))
    grado = Column(String(10))

    # RELACIONES
    grupo_id: Mapped[int] = mapped_column(ForeignKey("tb_grupos.id_grupo"), nullable=True )
    rl_grupo: Mapped["grupo"] = relationship(back_populates="rl_estudiante")

    rl_calificacion: Mapped[list["calificaciones"]] = relationship(back_populates="rl_estudiante")
    rl_asistencia: Mapped[list["asistencias"]] = relationship(back_populates="rl_estudiante")


# CALIFICACIONES
class calificaciones(Base):
    __tablename__ = "tb_calificaciones"

    id = Column(Integer, primary_key=True, autoincrement= True)
    calificacion = Column(Float)
    # RELACIONES
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("tb_estudiantes.id_estudiante"))
    rl_estudiante: Mapped["estudiante"] = relationship(back_populates="rl_calificacion")

    asignatura_id: Mapped[int] = mapped_column(ForeignKey("tb_asignaturas.id_asignatura"))
    rl_asignatura: Mapped["asignatura"] = relationship(back_populates="rl_calificacion")


# ASIGNATURA
class asignatura(Base):
    __tablename__ = "tb_asignaturas"

    id_asignatura = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))
    # RELACIONES
    rl_calificacion: Mapped[list["calificaciones"]] = relationship(back_populates="rl_asignatura")
    rl_asistencia: Mapped[list["asistencias"]] = relationship(back_populates="rl_asignatura")

    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_asignatura")


# ASISTENCIAS
class asistencias(Base):
    __tablename__ = "tb_asistencias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(String(50))
    # RELACIONES
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("tb_estudiantes.id_estudiante"))
    rl_estudiante: Mapped["estudiante"] = relationship(back_populates="rl_asistencia")

    asignatura_id: Mapped[int] = mapped_column(ForeignKey("tb_asignaturas.id_asignatura"))
    rl_asignatura: Mapped["asignatura"] = relationship(back_populates="rl_asistencia")


# GESTION ASIGNATURA
class gestion_asignatura(Base):
    __tablename__ = "tb_gestion_asignatura"
    id_gestion = Column(Integer, primary_key=True, autoincrement=True)

    # RELACIONES
    rl_horario: Mapped[list["horario"]] = relationship(back_populates="rl_gestion")

    grupo_id: Mapped[int] = mapped_column(ForeignKey("tb_grupos.id_grupo"))
    rl_grupo: Mapped["grupo"] = relationship(back_populates="rl_gestion")

    docente_id: Mapped[int] = mapped_column(ForeignKey("tb_docentes.id_docente"))
    rl_docente: Mapped["docente"] = relationship(back_populates="rl_gestion")

    asignatura_id: Mapped[int] = mapped_column(ForeignKey("tb_asignaturas.id_asignatura"))
    rl_asignatura: Mapped["asignatura"] = relationship(back_populates="rl_gestion")



# DOCENTE
class docente(Base):
    __tablename__ = "tb_docentes"

    id_docente = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))
    apellidos = Column(String(150))

    # RELACIONES
    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_docente")



# HORARIO
class horario(Base):
    __tablename__ = "tb_horarios"

    id_horario = Column(Integer, primary_key=True, autoincrement=True)

    # RELACIONES
    gestion_id: Mapped[int] = mapped_column(ForeignKey("tb_gestion_asignatura.id_gestion"))
    rl_gestion: Mapped["gestion_asignatura"] = relationship(back_populates="rl_horario", single_parent=True)



# ASOSIACION
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
