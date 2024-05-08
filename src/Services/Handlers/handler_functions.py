"""
Recibe 2 entidades y asigna a la primera entidad los valores de la segunda entidad
cuyas calves sean iguales 

ejemplo ---->
            # result.nombre = _student.nombre
            # result.apellido = _student.apellido
            # result.tipo_documento = _student.tipo_documento
            # result.documento = _student.documento
            # result.Email = _student.Email
            # result.carne = _student.carne
            # result.telefono = _student.telefono
            # result.grado = _student.grado
"""
def asignar_valores(entidad_destino, entidad_origen):
    for key, value in entidad_origen.dict().items():
        if hasattr(entidad_destino, key):
            setattr(entidad_destino, key, value)
    return entidad_destino


def getAllEntities(response):
    lista = []
    for tupla in response:
        lista.append(tupla[0])
    return lista