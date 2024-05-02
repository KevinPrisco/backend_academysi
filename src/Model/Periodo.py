from .Commons import *

# PERIODO
class periodo(Base):
    __tablename__ = "tb_periodos"

    id_periodo = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(150))