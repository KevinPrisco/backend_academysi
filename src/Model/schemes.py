from pydantic import BaseModel

class studentBase(BaseModel):
    id_estudiantes: int
    nombre: str
    

class StudentCreate(BaseModel):
    nombre: str

    # class Config:
    #     extra = Extra.forbid  


class userBase(BaseModel):
    id: int
    username: str
    password: str
    permisos: str

class JWToken(BaseModel):
    access_token: str
    token_type: str