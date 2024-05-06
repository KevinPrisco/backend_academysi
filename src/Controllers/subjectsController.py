from .Commons import *
from Model.Entities import asignatura, estudiante, grupo, docente, gestion_asignatura


#LISTAR UN REGISTRO DE ESTUDIANTES POR ID
async def getSubjectById(db: Session, id_student: int):
    async with db:
        try:
            result = await db.execute(
                select(grupo.descripcion, asignatura.nombre, docente.nombre, docente.apellidos)
                .select_from(estudiante)
                .join(grupo, grupo.id_grupo == estudiante.grupo_id)
                .join(gestion_asignatura, gestion_asignatura.grupo_id == grupo.id_grupo)
                .join(asignatura, asignatura.id_asignatura == gestion_asignatura.asignatura_id)
                .join(docente, gestion_asignatura.docente_id == docente.id_docente)
                .where(estudiante.id_estudiante == id_student)
            )
            if not result:
                raise NoResultFound('Usuario no encontrado')
            x = result.fetchall()
            response = []
            for item in x:
                element = {
                    "grupo": item[0],
                    "Materia": item[1],
                    "docente": (item[2]+ ' ' + item[3])
                }
                response.append(element)
            return response
        except:
            raise

