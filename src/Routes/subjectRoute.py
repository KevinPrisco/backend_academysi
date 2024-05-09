from Controllers import subjectsController
from Routes.commons import *


router  = APIRouter(
    prefix='/asignatura',    
    tags=["Asignatura"],
    # dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_student}")
async def get_admin(id_student: int, db: Session = Depends(get_db)):
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