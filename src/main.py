from fastapi import FastAPI, APIRouter
from Routers import studentRoutes
# from Model import student 


app = FastAPI()
app.include_router(studentRoutes.router)

@app.get("/")
async def inicio():
    return 'Bienvenido a la ruta principal'