from fastapi import Depends, HTTPException
from .Services.Auth import Auth

def get_current_user(token: str = Depends(Auth.token_access_validation)):
    if token["Message"] == 'Valido':
        return token["Token"]
    else:
        raise HTTPException(
            status_code=401,
            detail= token["Message"],
            headers={"WWW-Authenticate": "Bearer"},
        )
    

def get_token_scopes(payload: dict = Depends(get_current_user)):
    Permisos = payload['scope']
    print(Permisos)
    return