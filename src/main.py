from fastapi import FastAPI
from Routers import studentRoutes, userRoutes


app = FastAPI()
app.include_router(studentRoutes.router)
app.include_router(userRoutes.router)


@app.get("/")
def inicio():
    return 'Hola'