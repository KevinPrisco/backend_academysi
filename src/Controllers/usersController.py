from Controllers.Commons import *
from Model.Entities import usuario
from Services import Auth


#LISTAR UN REGISTRO POR ID
def getUserCredentials(db: Session, username: str):
    try:
        result = db.query(usuario).filter(usuario.username == username).first()
        if not result:
            raise NoResultFound('User not found')
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createUser(db: Session, _user: schemes.userBase):
    try:
        hash = Auth.hash_pass(_user.password)
        result = usuario(
            username = _user.username, 
            password = hash,
            permisos = _user.permisos
            )
        db.add(result)
        db.commit()
        db.refresh(result)
        return result
    except:
        raise
