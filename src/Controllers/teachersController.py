from Controllers.Commons import *
from Model.Entities import docente

#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
async def getTeacherById(db: Session, id_teacher: int):
    try:
        async with db:
            result = await db.get(docente, id_teacher)
            if not result:
                raise NoResultFound('Docente no encontrado')
            return result
    except:
        raise


#LISTAR TODOS LOS ESTUDIANTES
async def getTeachers(db: Session):
    try:
        async with db:
            result = await db.execute(select(docente))
            response = result.fetchall()
            response = getAllEntities(response)
            return response
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
async def createTeacher(db: Session, _teacher: schemes.teacherCreate):
    try:
        async with db:
            result = docente(
                nombres = _teacher.nombres,
                apellidos = _teacher.apellidos,
                tipo_documento = _teacher.tipo_documento,
                documento = _teacher.documento,
                email = _teacher.email,
                carne = _teacher.carne,
                telefono = _teacher.telefono,
                Area = _teacher.Area
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def updateTeacher(db: Session, _teacher: schemes.teacherList):
    try:
        async with db:
            result = await db.get(docente, _teacher.id_docente)
            result = asignar_valores(result, _teacher)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def deleteTeacher(db: Session, id_teacher: int):
    try:
        async with db:
            db_teacher = await db.get(docente, id_teacher)
            respuesta = { "Id": db_teacher.id_docente, "nombre": db_teacher.nombre}
            await db.delete(db_teacher)
            await db.commit()
            result = 'Docente borrado exitosamente: ', respuesta
            return result
    except:
        await db.rollback()
        raise
