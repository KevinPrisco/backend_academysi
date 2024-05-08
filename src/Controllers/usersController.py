from Controllers.Commons import *
from Model.Entities import usuario
from Services import Auth


#LISTAR UN REGISTRO POR ID
async def getUserCredentials(db: Session, username: str):
    try:
        async with db:
            result = await db.execute(select(usuario).where(usuario.username == username))
            response = result.all()
            if not response:
                raise NoResultFound('Estudiante not found')
            
            return response[0][0]
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
async def createUser(db: Session, _user: schemes.userCreate):
    try:
        async with db:
            hash = Auth.hash_pass(_user.password)
            result = usuario(
                username = _user.username, 
                password = hash,
                permisos = _user.permisos
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise
