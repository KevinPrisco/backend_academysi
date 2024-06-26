from ..Controllers import teachersController
from .commons import *


router  = APIRouter(
    prefix='/docente',    
    tags=["Profesores"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_teacher}", response_model= schemes.teacherList)
async def get_teacher(id_teacher: int, db: Session = Depends(get_db)):
    try:
        docente = await teachersController.getTeacherById(db, id_teacher)
        return docente
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.teacherList])
async def get_teachers(db: Session =  Depends(get_db)):
    try:
        docentes = await teachersController.getTeachers(db)
        return docentes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.post("/create", response_model=schemes.teacherList)
async def create_teacher(teacher: schemes.teacherCreate, db: Session = Depends(get_db)):
    try:
        docente = await teachersController.createTeacher(db, _teacher = teacher)
        return docente
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.teacherList)
async def update_teacher(teacher: schemes.teacherList, db: Session = Depends(get_db)):
    try:
        docente = await teachersController.updateTeacher(db, _teacher = teacher)
        return docente
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_teacher}")
async def delete_teacher(id_teacher: int,db: Session = Depends(get_db)):
    try: 
        docente = await teachersController.deleteTeacher(db, id_teacher)
        return docente
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)