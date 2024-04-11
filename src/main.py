from fastapi import FastAPI, APIRouter
from Routers import user_routers
# from Model import student 


app = FastAPI()
app.include_router(user_routers.router)

@app.get("/")
async def inicio():
    return 'Bienvenido a la ruta principal'