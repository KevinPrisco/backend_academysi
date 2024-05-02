from .Commons import *

# USUARIOS
class usuario(Base):
    __tablename__ = "tb_usuarios"
    
    id = Column(Integer, primary_key=True, autoincrement= True)
    username = Column(String(150))
    password = Column(String(150))
    permisos = Column(String(250))