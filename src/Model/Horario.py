from .Commons import *
# from .Gestion_asignatura import gestion_asignatura

# HORARIO
class horario(Base):
    __tablename__ = "tb_horarios"

    id_horario = Column(Integer, primary_key=True, autoincrement=True)

    # RELACIONES
    gestion_id: Mapped[int] = mapped_column(ForeignKey("tb_gestion_asignatura.id_gestion"))
    rl_gestion: Mapped["gestion_asignatura"] = relationship(back_populates="rl_horario", single_parent=True)