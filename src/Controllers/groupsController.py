from ..Controllers.Commons import *
from ..Model.Entities import grupo

#LISTAR UN REGISTRO DE GRUPOS POR ID
async def getGroupById(db: Session, id_group: int):
    try:
        async with db:
            result = await db.get(grupo, id_group)
            if not result:
                raise NoResultFound('Grupo not found')
            return result
    except:
        raise


#LISTAR TODOS LOS GRUPOS
async def getGroups(db: Session):
    try:
        async with db:
            result = await db.execute(select(grupo))
            response = result.fetchall()
            response = getAllEntities(response)
            return response
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA GRUPOS
async def createGroup(db: Session, _group: schemes.groupCreate):
    try:
        async with db:
            result = grupo(
                descripcion = _group.descripcion
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
        
    except BaseException as e:
        await db.rollback()
        raise e


#ACTUALIZAR UN REGISTRO EN LA TABLA GRUPOS
async def updateGroup(db: Session, _group: schemes.groupList):
    try:
        async with db:
            result = await db.get(grupo, _group.id_grupo)
            result = asignar_valores(result, _group)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA GRUPOS
async def deleteGroup(db: Session, id_group: int):
    try:
        async with db:
            db_group = await db.get(grupo, id_group)
            respuesta = { "Id": db_group.id_grupo, "nombre": db_group.descripcion}
            await db.delete(db_group)
            await db.commit()
            result = 'Grupo borrado exitosamente: ', respuesta
            return result
    except:
        await db.rollback()
        raise
