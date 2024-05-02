from Controllers.Commons import *
from Services import Auth


#LISTAR UN REGISTRO POR ID
def getUserCredentials(db: Session, username: str):
    try:
        result = db.query(Entities.usuario).filter(Entities.usuario.username == username).first()
        if not result:
            raise NoResultFound('User not found')
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createUser(db: Session, _user: schemes.userBase):
    try:
        hash = Auth.hash_pass(_user.password)
        db_user = Entities.usuario(
            username = _user.username, 
            password = hash,
            permisos = _user.permisos
            )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except:
        raise
