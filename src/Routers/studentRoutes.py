from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Controllers import studentsController
from Model import schemes
from sqlalchemy.orm.exc import NoResultFound
from Database.Connection import get_db
from dependencies import get_current_user, get_token_scopes


router  = APIRouter(
    prefix='/student',    
    tags=["Estudiantes"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_student}", response_model= schemes.studentList)
def get_student(id_student: int, db: Session = Depends(get_db)):
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
    

@router.get("/get", response_model=list[schemes.studentList])
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


@router.post("/create", response_model=schemes.studentCreate)
def create_student(student: schemes.studentCreate, db: Session = Depends(get_db)):
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


@router.put("/update", response_model=schemes.studentList)
def update_student(student: schemes.studentList, db: Session = Depends(get_db)):
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
def delete_student(id_student: int,db: Session = Depends(get_db)):
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