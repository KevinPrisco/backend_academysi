from fastapi import APIRouter

router  = APIRouter(
    prefix='/users', 
    tags=["user"]
)

@router.get("/listar")
async def get_users():
    usuarios = {
        "nombre": "kevin"
    }
    return usuarios 

@router.get("/crear")
async def create_users():
    return 'usuarios creados'