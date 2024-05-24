from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from io import BytesIO
from collections import defaultdict

def generar_reporte(notas):
    # Creamos un diccionario donde la clave es la materia y el valor es una lista de notas
    materias_notas = defaultdict(list)
    for nota in notas:
        materias_notas[nota["Materia"]].append(nota["Nota"])

    # Ordenamos las materias alfabéticamente
    materias = sorted(materias_notas.keys())


    # data = [["Materia"] + [f"Nota {i+1}" for i in range(len(max(materias_notas.values(), key=len)) * 2)]]
    # for materia in materias:
    #     fila = [materia]  # Inicializamos la fila con el nombre de la materia
    #     notas_materia = [nota for nota in notas if nota["Materia"] == materia]  # Obtener las notas de la materia actual
    #     for nota in notas_materia:
    #         fila.append(nota["Nota"])  # Agregar la nota a la fila
    #         fila.append(f"{nota['Porcentaje']}%")  # Agregar el porcentaje de la nota a la fila
    #     # Rellenar con espacios en blanco si la materia tiene menos notas que el máximo
    #     fila += [''] * (len(data[0]) - len(fila))
    #     data.append(fila)

    # Encontrar la cantidad máxima de notas
    max_notas = len(max(materias_notas.values(), key=len))

    # Crear encabezados dinámicamente
    encabezados = []
    for i in range(max_notas):
        encabezados.append(f"Nota {i+1}")
        encabezados.append("%")

    # Crear la primera fila con los encabezados
    data = [["Materia"] + encabezados]

    # Llenar los datos de la tabla
    for materia in materias:
        fila = [materia]  # Inicializamos la fila con el nombre de la materia
        notas_materia = [nota for nota in notas if nota["Materia"] == materia]  # Obtener las notas de la materia actual
        for nota in notas_materia:
            fila.append(nota["Nota"])  # Agregar la nota a la fila
            fila.append(f"{nota['Porcentaje']}%")  # Agregar el porcentaje de la nota a la fila
        # Rellenar con espacios en blanco si la materia tiene menos notas que el máximo
        fila += [''] * (len(data[0]) - len(fila))
        data.append(fila)

    # Generamos el PDF
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    table = Table(data)

    # Estilo de la tabla
    style = TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                        ('GRID', (0, 0), (-1, -1), 1, colors.black)])
    table.setStyle(style)

    # Agregar la tabla al documento
    doc.build([table])

    buffer.seek(0)
    return buffer.getvalue()