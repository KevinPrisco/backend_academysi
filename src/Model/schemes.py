from pydantic import BaseModel


# ESTUDIANTES
class studentBase(BaseModel):
    id_estudiante: int


class studentList(studentBase):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    Email: str
    carne: str
    telefono: str
    grado: str


class studentCreate(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    documento: str
    Email: str
    carne: str
    telefono: str
    grado: str



# PROFESORES
class teacherBase(BaseModel):
    id_docente: int


class teacherList(teacherBase):
    nombre: str
    apellidos: str


class teacherCreate(BaseModel):
    nombre: str
    apellidos: str



# ADMINISTRADOR
class adminBase(BaseModel):
    id_administrador: int


class adminList(adminBase):
    nombre: str


class adminCreate(BaseModel):
    nombre: str



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

