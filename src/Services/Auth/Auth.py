from datetime import datetime, timedelta, timezone
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt, JWTError
from ...config import SECRET_KEY, ALGORITHM


#instancias de OAUTH2 Y passlib
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/usuario/Login')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


#Funcion para encriptar las contraseñas de los usuarios
def hash_pass(password):
    return pwd_context.hash(password)


#Funcion para Verificar que la contraseña ingresada
def verify_hash_pass(password, hash):
    return pwd_context.verify(password, hash)


#Funcion para encritar en JWT
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    datos = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    datos.update({"exp": expire})
    encoded_jwt = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


#Funcion Para validad si el token si esta firmado correctamente
def token_access_validation(token: str = Depends(oauth2_scheme)):
    result =  {
        "Token": None,
        "Message": ""
    }
    try:
        #decodifica el token usando la secret key y el algoritmo con el que fue codificado
        Token_data = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        result["Token"] = Token_data
        result["Message"] = "Valido"
        return result
    except:
        result["Message"] = "Error: Token no valido"
        return result