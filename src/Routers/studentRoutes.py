from Services import Auth
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from Controllers import studentsController
from Model import schemes
from Database import Connection
from sqlalchemy.orm.exc import NoResultFound
from Services import Auth
from typing import Annotated
from Database.Connection import get_db

router  = APIRouter(
    prefix='/student',    
    tags=["Estudiantes"],
    dependencies=[]
)

@router.get("/getID/{id_student}", response_model= schemes.studentBase)
def get_students(token: Annotated[str, Depends(Auth.oauth2_scheme)], id_student: int, db: Session = Depends(get_db)):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
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
def get_students(token: Annotated[str, Depends(Auth.oauth2_scheme)], db: Session =  Depends(get_db)):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
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
def create_students(token: Annotated[str, Depends(Auth.oauth2_scheme)], student: schemes.studentBase, db: Session = Depends(get_db)):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
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
def update_students(token: Annotated[str, Depends(Auth.oauth2_scheme)],student: schemes.studentBase, db: Session = Depends(get_db)):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
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
def delete_students(token: Annotated[str, Depends(Auth.oauth2_scheme)], id_student: int,db: Session = Depends(get_db)):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
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