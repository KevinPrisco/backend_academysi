from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from .Routes import *
import uvicorn
from fastapi_pagination.utils import disable_installed_extensions_check

disable_installed_extensions_check()

app = FastAPI()
app.include_router(userRoute.router)
app.include_router(studentRoute.router)
app.include_router(teacherRoute.router)
app.include_router(adminRoute.router)
app.include_router(subjectRoute.router)
app.include_router(groupRoute.router)
add_pagination(app)

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

# if __name__ == "__main__":
#     uvicorn.run(app, port=8000)