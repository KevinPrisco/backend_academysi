from .Commons import *

# ADMINISTRADOR
class administrador(Base):
    __tablename__ = "tb_administrador"

    id_administrador = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))
