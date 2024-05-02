from .Commons import *
# from .Estudiante import estudiante
# from .Gestion_asignatura import gestion_asignatura

# GRUPOS
class grupo(Base):
    __tablename__ = "tb_grupos"

    id_grupo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(150))
    # RELACIONES
    rl_estudiante: Mapped[list["estudiante"]] = relationship(back_populates="rl_grupo")

    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_grupo")