from fastapi import FastAPI, APIRouter
from Routers import user_routers


app = FastAPI()
app.include_router(user_routers.router)

@app.get("/")
async def inicio():
    return 'Bienvenido a la pagina principal'