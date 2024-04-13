from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter, HTTPException
from Routers import studentRoutes, userRoutes
from Services import Auth


app = FastAPI()
app.include_router(studentRoutes.router)
app.include_router(userRoutes.router)

@app.get("/")
async def inicio(token: Annotated[str, Depends(Auth.oauth2_scheme)]):
    user = token
    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user