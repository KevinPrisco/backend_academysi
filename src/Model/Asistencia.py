from .Commons import *
# from .Estudiante import estudiante
# from .Asignatura import asignatura

# ASISTENCIAS
class asistencias(Base):
    __tablename__ = "tb_asistencias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(String(50))
    # RELACIONES
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("tb_estudiantes.id_estudiantes"))
    rl_estudiante: Mapped["estudiante"] = relationship(back_populates="rl_asistencia")

    asignatura_id: Mapped[int] = mapped_column(ForeignKey("tb_asignaturas.id_asignatura"))
    rl_asignatura: Mapped["asignatura"] = relationship(back_populates="rl_asistencia")