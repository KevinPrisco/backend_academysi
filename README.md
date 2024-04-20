# BackEnd_FastAPI_AcademySI
Backend API restfull con Python y el framework fastAPI para el desarrollo del proyecto final de metodologías de desarrollo de sistemas de información enfocado a un proyecto tipo SIA (sistema de información académico)

# Configuraciones del proyecto

## Instalar entorno virtual
Instala un entorno virtual sobre el cual se van a instalar las dependencias y ejecutar el proyecto
<br/>
`python3 -m venv venv`

## Activar el entorno virtual en Windows
Inicia un entorno virtual de python
<br/>
`venv\Scripts\activate`

## Instalar requerimientos
Instala las dependencias para la ejecucion del proyecto
<br/>
`pip install -r requirements.txt`

## Actualizar el arhcivo de requerimientos
Agrega las nuevas dependencias(librerias) instaladas al archivo de requerimientos
<br/>
`pip freeze > requirements.txt`


# Ejecutar el proyecto
## ejecutar el proyecto en modo debug
`uvicorn main:app --reload`

## ejecutar el proyecto en modo produccion
`uvicorn main:app --host x.x.x.x --port x`


# Migrar los modelos a la base de datos
Generar la plantilla del proyecto de Alembic usado para generar las migraciones
<br/>
`alembic init migraciones`

Generar una revision de los cambios en la base de datos basado en los modelos para enviarlos a la base de datos
<br/>
`alembic revision --autogenerate -m "Description"`

Genera una actualizacion en la base de datos basado en la ultima revision generada por el comando anterior
<br/>
`alembic upgrade head`
