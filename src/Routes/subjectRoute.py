from ..Controllers import subjectsController
from .commons import *


router  = APIRouter(
    prefix='/asignatura',    
    tags=["Asignatura"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_student}")
async def get_subject(id_student: int, db: Session = Depends(get_db)):
    try:
        asignatura = await subjectsController.getSubjectById(db, id_student)
        return asignatura
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.subjectList])
async def get_subjects(db: Session =  Depends(get_db)):
    try:
        asignatura = await subjectsController.getSubjects(db)
        return asignatura
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)
    


@router.post("/create", response_model=schemes.subjectList)
async def create_subject(subject: schemes.subjectCreate, db: Session = Depends(get_db)):
    try:
        asignatura = await subjectsController.createSubject(db, _subject = subject)
        return asignatura
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.subjectList)
async def update_subject(subject: schemes.subjectList, db: Session = Depends(get_db)):
    try:
        asignatura = await subjectsController.updateSubject(db, _subject = subject)
        return asignatura
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_subject}")
async def delete_subject(id_subject: int, db: Session = Depends(get_db)):
    try: 
        asignatura = await subjectsController.deleteSubject(db, id_subject)
        return asignatura
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)