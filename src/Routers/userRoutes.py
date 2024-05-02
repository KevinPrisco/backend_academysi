from Controllers import usersController
from Routers.commons import *
from datetime import timedelta
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from Services import Auth
from config import ACCESS_TOKEN_EXPIRE_HOURS


router  = APIRouter(
    prefix='/Users',    
    tags=["Usuarios"],
    dependencies=[]
)

@router.post("/Login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session= Depends(get_db)) -> schemes.JWToken:
    try:
        #Busca Si el usuario existe
        usuario = usersController.getUserCredentials(db, form_data.username)
        #Verifica si la clave ingresada es igual a la clave almacenada en BD
        hashkey = Auth.verify_hash_pass(form_data.password, usuario.password)

        #Verificar si el usuario y la contraseña son correctas
        if((usuario.username != form_data.username) or (not hashkey)):
            raise HTTPException(status_code=400, detail="Incorrect password")
        
        #Llamar a la funcion para Crear el token de acceso 
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_HOURS)
        access_token = Auth.create_access_token(
            data={
                "id:": usuario.id ,
                "sub": usuario.username,
                "scope": usuario.permisos
                }, 
            expires_delta=access_token_expires
        )
        return {
            "access_token": access_token, 
            "token_type": "bearer"
            }   
    
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