from sqlalchemy.orm import Session
from Model import schemes, models
import json



#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
def getStudentById(db: Session, id_student: int):
    return db.query(models.Student).filter(models.Student.id_estudiantes == id_student).first()


#LISTAR TODOS LOS ESTUDIANTES
def getStudents(db: Session):
    return db.query(models.Student).all()


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createStudent(db: Session, _student: schemes.StudentCreate):
    db_student = models.Student(nombre = _student.nombre)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
def updateStudent(db: Session, _student: schemes.studentBase):
    try:
        estudiante = db.query(models.Student).filter(models.Student.id_estudiantes == _student.id_estudiantes).first()
        estudiante.nombre = _student.nombre
        db.commit()
        db.refresh(estudiante)
        return estudiante
    except:
        return 'Error'


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
def deleteStudent(db: Session, id_student: int):
    try:
        db_student = db.query(models.Student).filter(models.Student.id_estudiantes == id_student).first()
        respuesta = { "Id": db_student.id_estudiantes, "nombre": db_student.nombre}
        db.delete(db_student)
        db.commit()
        result = 'Estudiante borrado exitosamente: ', respuesta
        return result
    except NameError:
        return 'No se pudo eliminar el registro, Ocurrio un error: ' + NameError
