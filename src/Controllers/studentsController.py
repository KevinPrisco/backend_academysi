from Controllers.Commons import *
from Model.Entities import estudiante


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
def getStudentById(db: Session, id_student: int):
    try:
        result = db.query(estudiante).filter(estudiante.id_estudiantes == id_student).first()
        print('hola:', result)
        if not result:
            raise NoResultFound('Usuario no encontrado')
        return result
    except:
        raise


#LISTAR TODOS LOS ESTUDIANTES
def getStudents(db: Session):
    try:
        result = db.query(estudiante).all()
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createStudent(db: Session, _student: schemes.studentCreate):
    try:
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
        db.commit()
        db.refresh(result)
        return result
    except:
        raise


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
def updateStudent(db: Session, _student: schemes.studentList):
    try:
        result = db.query(estudiante).filter(estudiante.id_estudiantes == _student.id_estudiantes).first()
        result.nombre = _student.nombre
        db.commit()
        db.refresh(result)
        return result
    except:
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
def deleteStudent(db: Session, id_student: int):
    try:
        db_student = db.query(estudiante).filter(estudiante.id_estudiantes == id_student).first()
        respuesta = { "Id": db_student.id_estudiantes, "nombre": db_student.nombre}
        db.delete(db_student)
        db.commit()
        result = 'Estudiante borrado exitosamente: ', respuesta
        return result
    except:
        raise
