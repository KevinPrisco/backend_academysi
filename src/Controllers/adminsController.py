from Controllers.Commons import *
from Model.Entities import administrador

async def getAdminById(db: Session, id_admin: int):
    try:
        async with db:
            result = await db.get(administrador, id_admin)
            if not result:
                raise NoResultFound('Administrador no encontrado')
            return result
    except:
        raise


async def getAdmins(db: Session):
    try:
        async with db:
            result =  await db.execute(select(administrador))
            response = result.fetchall()
            response = getAllEntities(response)
            return response
    except:
        raise


async def createAdmin(db: Session, _admin: schemes.adminCreate):
    try:
        async with db:
            result = administrador(
                nombre = _admin.nombre,
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


async def updateAdmin(db: Session, _admin: schemes.adminList):
    try:
        async with db:
            result = await db.get(administrador, _admin.id_administrador)
            result = asignar_valores(result, _admin)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def deleteAdmin(db: Session, id_admin: int):
    try:
        async with db:
            db_admin =  await db.get(administrador, id_admin)
            respuesta = { "Id": db_admin.id_administrador, "nombre": db_admin.nombre}
            await db.delete(db_admin)
            await db.commit()
            result = 'Administrador borrado exitosamente: ', respuesta
            return result
    except:
        await db.rollback()
        raise

