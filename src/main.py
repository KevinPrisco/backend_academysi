from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routers import *


app = FastAPI()
app.include_router(userRoutes.router)
app.include_router(studentRoutes.router)
app.include_router(teacherRoute.router)
app.include_router(adminRoutes.router)


@app.get("/")
def inicio():
    return 'Hola'

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)