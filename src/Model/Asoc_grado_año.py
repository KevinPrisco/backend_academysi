from .Commons import *
# from .Grado_escolar import grado_escolar
# from .Año_academico import año_academico

# ASOSIACION
asociacion = Table(
    "asociacion_año_grado",
    Base.metadata,
    Column("año_academico_id", ForeignKey("tb_año_academico.id_añoAcademico"), primary_key=True),
    Column("grado_escolar_id", ForeignKey("tb_grado_escolar.id_gradoEscolar"), primary_key=True)
)
    
grados_escolares: Mapped[List[grado_escolar]] = relationship(
    secondary=asociacion, back_populates='años_academicos'
)
años_academicos: Mapped[List[año_academico]] = relationship(
   secondary=asociacion, back_populates='grados_escolares'
)




    

