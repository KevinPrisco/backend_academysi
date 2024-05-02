from .Commons import *
# from .Estudiante import estudiante
# from .Asignatura import asignatura

# CALIFICACIONES
class calificaciones(Base):
    __tablename__ = "tb_calificaciones"

    id = Column(Integer, primary_key=True, autoincrement= True)
    calificacion = Column(Float)
    # RELACIONES
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("tb_estudiantes.id_estudiantes"))
    rl_estudiante: Mapped["estudiante"] = relationship(back_populates="rl_calificacion")

    asignatura_id: Mapped[int] = mapped_column(ForeignKey("tb_asignaturas.id_asignatura"))
    rl_asignatura: Mapped["asignatura"] = relationship(back_populates="rl_calificacion")