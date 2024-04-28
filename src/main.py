from fastapi import FastAPI
from Routers import studentRoutes, userRoutes, teacherRoute, adminRoutes


app = FastAPI()
app.include_router(userRoutes.router)
app.include_router(studentRoutes.router)
app.include_router(teacherRoute.router)
app.include_router(adminRoutes.router)


@app.get("/")
def inicio():
    return 'Hola'