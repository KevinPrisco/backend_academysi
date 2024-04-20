from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from Database.Connection import get_db
from Services import Auth

def get_current_user(token: str = Depends(Auth.oauth2_scheme)):
    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token