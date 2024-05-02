from .Commons import *

# GRADO ESCOLAR
class grado_escolar(Base):
    __tablename__ = "tb_grado_escolar"

    id_gradoEscolar = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))