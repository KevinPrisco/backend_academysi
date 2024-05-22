from .Commons import *
from ..Model.Entities import asignatura, estudiante, grupo, docente, gestion_asignatura


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
async def getSubjectById(db: Session, id_student: int):
    async with db:
        try:
            result = await db.execute(
                select(grupo.descripcion, asignatura.descripcion, docente.nombres, docente.apellidos)
                .select_from(estudiante)
                .join(grupo, grupo.id_grupo == estudiante.grupo_id)
                .join(gestion_asignatura, gestion_asignatura.grupo_id == grupo.id_grupo)
                .join(asignatura, asignatura.id_asignatura == gestion_asignatura.asignatura_id)
                .join(docente, gestion_asignatura.docente_id == docente.id_docente)
                .where(estudiante.id_estudiante == id_student)
            )
            if not result:
                raise NoResultFound('Usuario no encontrado')
            x = result.fetchall()
            response = []
            for item in x:
                element = {
                    "grupo": item[0],
                    "Materia": item[1],
                    "docente": (item[2]+ ' ' + item[3])
                }
                response.append(element)
            return response
        except:
            raise



# LISTAS TODAS LAS ASIGNATURAS
async def getSubjects(db: Session):
    try:
        async with db:
            result = await db.execute(select(asignatura))
            response = result.fetchall()
            response = getAllEntities(response)
            return response
    except:
        raise



#CREAR UN REGISTRO NUEVO EN LA TABLA ASIGNATURAS
async def createSubject(db: Session, _subject: schemes.subjectCreate):
    try:
        async with db:
            result = asignatura(
                descripcion = _subject.descripcion,
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise



#ACTUALIZAR UN REGISTRO EN LA TABLA ASIGNATURAS
async def updateSubject(db: Session, _subject: schemes.subjectList):
    try:
        async with db:
            result = await db.get(asignatura, _subject.id_asignatura)
            result = asignar_valores(result, _subject)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise



#ELIMINAR UN REGISTRO EN LA TABLA ASIGNATURAS
async def deleteSubject(db: Session, id_subject: int):
    try:
        async with db:
            db_subject = await db.get(asignatura, id_subject)
            respuesta = { "Id": db_subject.id_asignatura, "nombre": db_subject.descripcion}
            await db.delete(db_subject)
            await db.commit()
            result = 'Asignatura borrado exitosamente: ', respuesta
            return result
    except:
        await db.rollback()
        raise
