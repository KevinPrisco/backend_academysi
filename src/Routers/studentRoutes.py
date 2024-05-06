from Controllers import studentsController
from Routers.commons import *


router  = APIRouter(
    prefix='/student',    
    tags=["Estudiantes"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_student}", response_model= schemes.studentList)
async def get_student(id_student: int, db: Session = Depends(get_db)):
    try:
        estudiantes = await studentsController.getStudentById(db, id_student)
        return estudiantes
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.studentList])
async def get_students(db: Session =  Depends(get_db)):
    try:
        estudiantes = await studentsController.getStudents(db)
        return estudiantes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.post("/create", response_model=schemes.studentCreate)
async def create_student(student: schemes.studentCreate, db: Session = Depends(get_db)):
    try:
        estudiantes = await studentsController.createStudent(db, _student = student)
        return estudiantes
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update")
async def update_student(student: schemes.studentList, db: Session = Depends(get_db)):
    try:
        estudiantes = await studentsController.updateStudent(db, _student = student)
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