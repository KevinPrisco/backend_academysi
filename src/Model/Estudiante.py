from .Commons import *
# from .Calificacion import calificaciones
# from .Asistencia import asistencias
# from .Grupo import grupo

# ESTUDIANTES
class estudiante(Base):
    __tablename__ = "tb_estudiantes"
    
    id_estudiantes = Column(Integer, primary_key=True, autoincrement= True)
    nombre = Column(String(150))
    apellido = Column(String(150))
    tipo_documento = Column(String(10))
    documento = Column(String(20))
    Email = Column(String(150))
    carne = Column(String(20))
    telefono = Column(String(100))
    grado = Column(String(10))

    # RELACIONES
    grupo_id: Mapped[int] = mapped_column(ForeignKey("tb_grupos.id_grupo"), nullable=True )
    rl_grupo: Mapped["grupo"] = relationship(back_populates="rl_estudiante")

    rl_calificacion: Mapped[list["calificaciones"]] = relationship(back_populates="rl_estudiante")
    rl_asistencia: Mapped[list["asistencias"]] = relationship(back_populates="rl_estudiante")