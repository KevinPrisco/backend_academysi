from ..Controllers import groupsController
from .commons import *


router  = APIRouter(
    prefix='/grupos',    
    tags=["Grupos"],
    dependencies=[Depends(get_current_user), Depends(get_token_scopes)]
)


@router.get("/getbyid/{id_group}", response_model= schemes.groupList)
async def get_group(id_group: int, db: Session = Depends(get_db)):
    try:
        grupos = await groupsController.getGroupById(db, id_group)
        return grupos
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
    

@router.get("/get", response_model=list[schemes.groupList])
async def get_groups(db: Session =  Depends(get_db)):
    try:
        grupos = await groupsController.getGroups(db)
        return grupos
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.post("/create", response_model=schemes.groupList)
async def create_group(group: schemes.groupCreate, db: Session = Depends(get_db)):
    try:
        grupos = await groupsController.createGroup(db, _group = group)
        return grupos
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.put("/update", response_model=schemes.groupList)
async def update_group(group: schemes.groupList, db: Session = Depends(get_db)):
    try:
        grupos = await groupsController.updateGroup(db, _group = group)
        return grupos
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)


@router.delete("/delete/{id_group}")
async def delete_group(id_group: int,db: Session = Depends(get_db)):
    try: 
        grupos = await groupsController.deleteGroup(db, id_group)
        return grupos
    
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)