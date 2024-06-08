from ..Controllers import adminsController
from .commons import *


router  = APIRouter(
    prefix='/admin',    
    tags=["Administradores"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_admin}", response_model= schemes.adminList)
async def get_admin(id_admin: int, db: Session = Depends(get_db)):
    try:
        admin = await adminsController.getAdminById(db, id_admin)
        return admin
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.adminList])
async def get_admin(db: Session =  Depends(get_db)):
    try:
        admin = await adminsController.getAdmins(db)
        return admin
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.post("/create", response_model=schemes.adminList)
async def create_admin(admin: schemes.adminCreate, db: Session = Depends(get_db)):
    try:
        admin = await adminsController.createAdmin(db, _admin = admin)
        return admin
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.adminList)
async def update_admin(admin: schemes.adminList, db: Session = Depends(get_db)):
    try:
        admin = await adminsController.updateAdmin(db, _admin = admin)
        return admin
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_admin}")
async def delete_admin(id_admin: int,db: Session = Depends(get_db)):
    try: 
        admin = await adminsController.deleteAdmin(db, id_admin)
        return admin
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)