from pydantic import BaseModel
from fastapi_pagination import Page


# ESTUDIANTES
class studentBase(BaseModel):
    id_estudiante: int


class studentList(studentBase):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    grado: str


class studentCreate(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    grado: str

class studentPagination(Page):
    total: int
    page: int
    size: int
    pages: int
    items: list[studentList]


# PROFESORES
class teacherBase(BaseModel):
    id_docente: int


class teacherList(teacherBase):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    Area: str


class teacherCreate(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    Area: str



# ADMINISTRADOR
class adminBase(BaseModel):
    id_administrador: int


class adminList(adminBase):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    Rol: str


class adminCreate(BaseModel):
    nombres: str
    apellidos: str
    tipo_documento: str
    documento: str
    email: str
    carne: str
    telefono: str
    Rol: str



# USUARIOS
class userBase(BaseModel):
    id: int
    username: str
    password: str
    permisos: str



class userCreate(BaseModel):
    username: str
    password: str
    permisos: str


# JWT
class JWToken(BaseModel):
    access_token: str
    token_type: str



#Asignatura
class subjectBase(BaseModel):
    id_asignatura: int


class subjectList(subjectBase):
    descripcion: str


class subjectCreate(BaseModel):
    descripcion: str




# GRUPOS

class groupBase(BaseModel):
    id_grupo: int


class groupList(groupBase):
    descripcion: str


class groupCreate(BaseModel):
    descripcion: str