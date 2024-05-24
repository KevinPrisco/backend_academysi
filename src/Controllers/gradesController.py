from Controllers.Commons import *
from Model.Entities import calificacion, asignatura, estudiante

#LISTAR UN REGISTRO DE GRUPOS POR ID
async def getGradesById(db: Session, id_estudiante: int):
    async with db:
        try:
            result = await db.execute(
                select(asignatura.id_asignatura, asignatura.descripcion, calificacion.calificacion, calificacion.porcentaje)
                .select_from(estudiante)
                .join(calificacion, calificacion.estudiante_id == estudiante.id_estudiante)
                .join(asignatura, asignatura.id_asignatura == calificacion.asignatura_id)
                .where(estudiante.id_estudiante == id_estudiante)
            )
            x = result.fetchall()
            response = []
            for item in x:
                response.append(item)
            return response
        except:
            raise