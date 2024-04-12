from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends, FastAPI, HTTPException, status
from Routers import userRoutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/Users/Login')