from fastapi import Depends, HTTPException
from Services import Auth

def get_current_user(token: str = Depends(Auth.token_access_validation)):
    if token is 'valido':
        return    
    else:
        raise HTTPException(
            status_code=401,
            detail= token,
            headers={"WWW-Authenticate": "Bearer"},
        )
    