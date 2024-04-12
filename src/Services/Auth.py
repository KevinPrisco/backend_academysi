from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/Users/Login')

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pass(password):
    return pwd_context.hash(password)

def verify_hash_pass(password, hash):
    return pwd_context.verify(password, hash)