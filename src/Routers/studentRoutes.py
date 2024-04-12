from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Controllers import studentsController
from Model import schemes
from Database import Connection
from sqlalchemy.orm.exc import NoResultFound
from typing import Union, Any

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

@router.get("/getID/{id_student}", response_model= schemes.studentBase)
def get_students(id_student: int,db: Session = Depends(get_db)):
    try:
        estudiantes = studentsController.getStudentById(db, id_student)
        return estudiantes
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    



@router.get("/getAll", response_model=list[schemes.studentBase])
def get_students(db: Session =  Depends(get_db)):
    try:
        estudiantes = studentsController.getStudents(db)
        return estudiantes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)



@router.post("/create", response_model=schemes.studentBase)
def create_students(student: schemes.studentBase, db: Session = Depends(get_db)):
    try:
        estudiantes = studentsController.createStudent(db, _student = student)
        return estudiantes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.studentBase)
def update_students(student: schemes.studentBase, db: Session = Depends(get_db)):
    try:
        estudiantes = studentsController.updateStudent(db, _student = student)
        return estudiantes
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_student}")
def delete_students(id_student: int,db: Session = Depends(get_db)):
    try: 
        estudiantes = studentsController.deleteStudent(db, id_student)
        return estudiantes
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)