from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from Controllers import studentsController
from Model import schemes
from Database import Connection

def get_db():
    db = Connection.Sessionlocal()
    try:
        yield db
    finally:
        db.close()

router  = APIRouter(
    prefix='/student',    
    tags=["Estudiantes"],
    dependencies=[]
)

@router.get("/getID/{id_student}",response_model=schemes.studentBase)
def get_user(id_student: int,db: Session = Depends(get_db)):
    estudiantes = studentsController.getStudentById(db, id_student)
    return estudiantes


@router.get("/getAll", response_model=list[schemes.studentBase])
def get_users(db: Session =  Depends(get_db)):
    estudiantes = studentsController.getStudents(db)
    return estudiantes


@router.post("/create", response_model=schemes.studentBase)
def create_user(student: schemes.studentBase, db: Session = Depends(get_db)):
    try:
        estudiantes = studentsController.createStudent(db, _student = student)
        return estudiantes
    except NameError:
        message= {
            "status": "400",
            "messaje": "Error de datos"
        }
        return message


@router.put("/update", response_model=schemes.studentBase)
def update_user(student: schemes.studentBase, db: Session = Depends(get_db)):
    try:
        estudiantes = studentsController.updateStudent(db, _student = student)
        return estudiantes
    except NameError:
        message= {
            "status": "400",
            "messaje": "Error de datos" + NameError
        }
        return message


@router.delete("/delete/{id_student}")
def delete_user(id_student: int,db: Session = Depends(get_db)):
    try: 
        estudiantes = studentsController.deleteStudent(db, id_student)
        return estudiantes
    
    except NameError:
        return 'Ocurrio un error: ' + NameError