from Controllers import gradesController
from Routes.commons import *
from fastapi import Response
from Services.Reports.pdf import generar_reporte


router  = APIRouter(
    prefix='/calificaciones',    
    tags=["Calificaciones"],
    # dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)

@router.get("/getbyid/{id_estudiante}")
async def get_group(id_estudiante: int, db: Session = Depends(get_db)):
    try:
        calificaciones = await gradesController.getGradesById(db, id_estudiante)
        keys = ['id', 'Materia', 'Nota', 'Porcentaje']
        result = [dict(zip(keys, item)) for item in calificaciones]
        return result  

    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/getpdf/{id_estudiante}")
async def get_group(id_estudiante: int, db: Session = Depends(get_db)):
    try:
        calificaciones = await gradesController.getGradesById(db, id_estudiante)
        keys = ['id', 'Materia', 'Nota', 'Porcentaje']
        result = [dict(zip(keys, item)) for item in calificaciones]

        pdf = generar_reporte(result)
        return Response(content=pdf, media_type='application/pdf')    

    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)