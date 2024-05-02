from .Commons import *
# from .Gestion_asignatura import gestion_asignatura

# DOCENTE
class docente(Base):
    __tablename__ = "tb_docentes"

    id_docente = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))
    apellidos = Column(String(150))

    # RELACIONES
    rl_gestion: Mapped[list["gestion_asignatura"]] = relationship(back_populates="rl_docente")