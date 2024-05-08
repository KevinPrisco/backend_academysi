from Controllers.Commons import *
from Model.Entities import estudiante


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
async def getStudentById(db: Session, id_student: int):
    try:
        async with db:
            result = await db.get(estudiante, id_student)
            if not result:
                raise NoResultFound('User not found')
            return result
    except:
        raise


#LISTAR TODOS LOS ESTUDIANTES
async def getStudents(db: Session):
    try:
        async with db:
            result = await db.execute(select(estudiante))
            response = result.fetchall()
            response = response[0]
        return response
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
async def createStudent(db: Session, _student: schemes.studentCreate):
    try:
        async with db:
            result = estudiante(
                nombre = _student.nombre,
                apellido = _student.apellido,
                tipo_documento = _student.tipo_documento,
                documento = _student.documento,
                Email = _student.Email,
                carne = _student.carne,
                telefono = _student.telefono,
                grado = _student.grado
                )
            db.add(result)
            await db.commit()
            await db.refresh(result)
            return result
        
    except BaseException as e:
        await db.rollback()
        raise e


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def updateStudent(db: Session, _student: schemes.studentList):
    try:
        async with db:
            result = await db.get(estudiante, _student.id_estudiante)
            result = asignar_valores(result, _student)
            await db.commit()
            await db.refresh(result)
            return result
    except:
        await db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def deleteStudent(db: Session, id_student: int):
    try:
        async with db:
            db_student = await db.get(estudiante, id_student)
            respuesta = { "Id": db_student.id_estudiante, "nombre": db_student.nombre}
            await db.delete(db_student)
            await db.commit()
            result = 'Estudiante borrado exitosamente: ', respuesta
            return result
    except:
        await db.rollback()
        raise
