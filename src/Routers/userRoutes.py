from datetime import timedelta
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from Database import Connection
from sqlalchemy.orm import Session
from Controllers import usersController
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.exc import NoResultFound
from fastapi import Depends, HTTPException, status
from Model import schemes, models
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
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session= Depends(get_db)) -> schemes.JWToken:
    try:
        usuario = usersController.getUserCredentials(db, form_data.username)
        hashkey = Auth.verify_hash_pass(form_data.password, usuario.password)
        if((usuario.username != form_data.username) or (not hashkey)):
            raise HTTPException(status_code=400, detail="Incorrect password")
        
        access_token_expires = timedelta(hours=Auth.ACCESS_TOKEN_EXPIRE_HOURS)
        access_token = Auth.create_access_token(
            data={"sub": usuario.username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}    
    except NoResultFound as e:
        message = str(e)
        detail = {
            "Status": 404,
            "Message": message
        }
        return JSONResponse(status_code=404, content=detail)


@router.post("/create", response_model=schemes.userBase)
def create_users(user: schemes.userBase, db: Session = Depends(get_db)):
    try:
        usuario = usersController.createUser(db, _user = user)
        return usuario
    except BaseException as e:
        message = str(e)
        detail = {
            "Status": 400,
            "Message": message
        }
        return JSONResponse(status_code=400, content=detail)