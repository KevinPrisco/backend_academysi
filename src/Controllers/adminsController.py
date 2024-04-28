from sqlalchemy.orm import Session
from Model import schemes, models
from sqlalchemy.orm.exc import NoResultFound


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
def getAdminById(db: Session, id_admin: int):
    try:
        result = db.query(models.administrador).filter(models.administrador.id_administrador == id_admin).first()
        if not result:
            raise NoResultFound('Administrador no encontrado')
        return result
    except:
        raise


#LISTAR TODOS LOS ESTUDIANTES
def getAdmins(db: Session):
    try:
        result = db.query(models.administrador).all()
        return result
    except:
        raise


#CREAR UN REGISTRO NUEVO EN LA TABLA ESTUDIANTES
def createAdmin(db: Session, _admin: schemes.adminCreate):
    try:
        administrador = models.administrador(
            nombre = _admin.nombre,
            )
        db.add(administrador)
        db.commit()
        db.refresh(administrador)
        return administrador
    except:
        raise


#ACTUALIZAR UN REGISTRO EN LA TABLA ESTUDIANTES
def updateAdmin(db: Session, _admin: schemes.adminList):
    try:
        administrador = db.query(models.administrador).filter(models.administrador.id_administrador == _admin.id_administrador).first()
        administrador.nombre = _admin.nombre
        db.commit()
        db.refresh(administrador)
        return administrador
    except:
        db.rollback()
        raise


#ELIMINAR UN REGISTRO EN LA TABLA ESTUDIANTES
def deleteAdmin(db: Session, id_admin: int):
    try:
        db_admin = db.query(models.administrador).filter(models.administrador.id_administrador == id_admin).first()
        respuesta = { "Id": db_admin.id_administrador, "nombre": db_admin.nombre}
        db.delete(db_admin)
        db.commit()
        result = 'Administrador borrado exitosamente: ', respuesta
        return result
    except:
        raise

