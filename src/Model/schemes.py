from pydantic import BaseModel

class studentBase(BaseModel):
    id_estudiantes: int
    nombre: str
    

class StudentCreate(BaseModel):
    nombre: str

    # class Config:
    #     extra = Extra.forbid  