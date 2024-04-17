from sqlalchemy.orm import Session
from Model import schemes, models
from sqlalchemy.orm.exc import NoResultFound


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
async def getStudentById(db: Session, id_student: int):
    try:
        result = await db.query(models.Student).filter(models.Student.id_estudiantes == id_student).first()
        if not result:
            raise NoResultFound('Usuario no encontrado')
        return result
    except:
        raise

#LISTAR TODOS LOS ESTUDIANTES
async def getStudents(db: Session):
    try:
        result = await db.query(models.Student).all()
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
async def createStudent(db: Session, _student: schemes.StudentCreate):
    try:
        db_student = models.Student(nombre = _student.nombre)
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student
    except:
        raise


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def updateStudent(db: Session, _student: schemes.studentBase):
    try:
        estudiante = db.query(models.Student).filter(models.Student.id_estudiantes == _student.id_estudiantes).first()
        estudiante.nombre = _student.nombre
        await db.commit()
        db.refresh(estudiante)
        return estudiante
    except:
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
async def deleteStudent(db: Session, id_student: int):
    try:
        db_student = db.query(models.Student).filter(models.Student.id_estudiantes == id_student).first()
        respuesta = { "Id": db_student.id_estudiantes, "nombre": db_student.nombre}
        db.delete(db_student)
        await db.commit()
        result = 'Estudiante borrado exitosamente: ', respuesta
        return result
    except:
        raise
