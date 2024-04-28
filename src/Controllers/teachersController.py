from sqlalchemy.orm import Session
from Model import schemes, models
from sqlalchemy.orm.exc import NoResultFound


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
def getTeacherById(db: Session, id_teacher: int):
    try:
        result = db.query(models.docente).filter(models.docente.id_docente == id_teacher).first()
        if not result:
            raise NoResultFound('Docente no encontrado')
        return result
    except:
        raise


#LISTAR TODOS LOS ESTUDIANTES
def getTeachers(db: Session):
    try:
        result = db.query(models.docente).all()
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createTeacher(db: Session, _teacher: schemes.teacherCreate):
    try:
        docente = models.docente(
            nombre = _teacher.nombre,
            apellidos = _teacher.apellidos,
            )
        db.add(docente)
        db.commit()
        db.refresh(docente)
        return docente
    except:
        raise


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
def updateTeacher(db: Session, _teacher: schemes.teacherList):
    try:
        docente = db.query(models.docente).filter(models.docente.id_docente == _teacher.id_teacher).first()
        db.begin()
        docente.nombre = _teacher.nombre
        docente.apellidos = _teacher.apellidos
        db.commit()
        db.refresh(docente)
        return docente
    except:
        db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
def deleteTeacher(db: Session, id_teacher: int):
    try:
        db_teacher = db.query(models.docente).filter(models.docente.id_docente == id_teacher).first()
        respuesta = { "Id": db_teacher.id_docente, "nombre": db_teacher.nombre}
        db.delete(db_teacher)
        db.commit()
        result = 'Docente borrado exitosamente: ', respuesta
        return result
    except:
        raise
