# BackEnd_FastAPI_AcademySI
Backend API restfull con Python y el framework fastAPI para el desarrollo del proyecto final de metodologías de desarrollo de sistemas de información enfocado a un proyecto tipo SIA (sistema de información académico)


# Instalar entorno virtual y requerimientos
python3 -m venv venv

pip install -r requirements.txt

## Agregar requerimientos al archivo de requerimientos
pip freeze > requirements.txt

## Activar el entorno virtual en Windows
.\venv\Scripts\activate


# Ejecutar el proyecto
## ejecutar el proyecto 
uvicorn main:app --host x.x.x.x --port x

## ejecutar el proyecto en modo debug
uvicorn main:app --reload 
