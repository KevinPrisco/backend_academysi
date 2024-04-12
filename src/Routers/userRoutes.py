from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Database import Connection
from sqlalchemy.orm import Session
from Controllers import usersController
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.exc import NoResultFound
from fastapi import Depends, HTTPException, status
from Model import schemes
from Services import Auth


def get_db():
    db = Connection.Sessionlocal()
    try:
        yield db
    finally:
        db.close()

router  = APIRouter(
    prefix='/Users',    
    tags=["Usuarios"],
    dependencies=[]
)

@router.post("/Login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session= Depends(get_db) ):
    try:
        usuario = usersController.getUserCredentials(db, form_data.username, form_data.password)
        if((usuario.username != form_data.username) or (usuario.password != form_data.password)):
            raise HTTPException(status_code=400, detail="Incorrect password")
        return {"access_token": usuario, "token_type": "bearer"}
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)
