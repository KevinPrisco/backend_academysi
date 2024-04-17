from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt
from config import SECRET_KEY, ALGORITHM


#instancias de OAUTH2 Y passlib
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/Users/Login')
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