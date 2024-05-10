from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes import *
import uvicorn


app = FastAPI()
app.include_router(userRoute.router)
app.include_router(studentRoute.router)
app.include_router(teacherRoute.router)
app.include_router(adminRoute.router)
app.include_router(subjectRoute.router)
app.include_router(groupRoute.router)


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

if __name__ == "__main__":
    uvicorn.run(app, port=8001)