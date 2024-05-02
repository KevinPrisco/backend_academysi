from Controllers import teachersController
from Routers.commons import *


router  = APIRouter(
    prefix='/teacher',    
    tags=["Profesores"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_teacher}", response_model= schemes.teacherList)
def get_teacher(id_teacher: int, db: Session = Depends(get_db)):
    try:
        docente = teachersController.getTeacherById(db, id_teacher)
        return docente
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.teacherList])
def get_teachers(db: Session =  Depends(get_db)):
    try:
        docentes = teachersController.getTeachers(db)
        return docentes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.post("/create", response_model=schemes.teacherList)
def create_teacher(teacher: schemes.teacherCreate, db: Session = Depends(get_db)):
    try:
        docente = teachersController.createTeacher(db, _teacher = teacher)
        return docente
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.teacherList)
def update_teacher(teacher: schemes.teacherList, db: Session = Depends(get_db)):
    try:
        docente = teachersController.updateTeacher(db, _teacher = teacher)
        return docente
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_teacher}")
def delete_teacher(id_teacher: int,db: Session = Depends(get_db)):
    try: 
        docente = teachersController.deleteTeacher(db, id_teacher)
        return docente
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)