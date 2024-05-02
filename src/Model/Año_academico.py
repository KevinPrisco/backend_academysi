from .Commons import *

# AÑO ACADEMICO
class año_academico(Base):
    __tablename__ = "tb_año_academico"

    id_añoAcademico = Column(Integer, primary_key=True, autoincrement=True)
    descripcion = Column(String(100))