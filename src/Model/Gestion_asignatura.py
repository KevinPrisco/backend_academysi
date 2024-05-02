from .Commons import *
# from .Horario import horario
# from .Grupo import grupo
# from .Docente import docente
# from .Asignatura import asignatura

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