from .Commons import *
# from .Gestion_asignatura import gestion_asignatura
# from .Calificacion import calificaciones
# from .Asistencia import asistencias


# ASIGNATURA
class asignatura(Base):
    __tablename__ = "tb_asignaturas"

    id_asignatura = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100))

    # RELACIONES
    rl_calificacion: Mapped[list["calificaciones"]] = relationship(back_populates="rl_asignatura")
    rl_asistencia: Mapped[list["asistencias"]] = relationship(back_populates="rl_asignatura")

    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_asignatura")
