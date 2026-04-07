def initialize_dict(student_name, subject_grades):
    diccionario_inicial = {
        student_name:subject_grades
    }
    return print(diccionario_inicial)

def add_student(student_grades = {}):
    data_estudiante = {}
    name = input("Enter student name:\n").title()
    while True:
        asignaturas = input("Enter subject and grade (or 'exit' to finish):\n")
        if asignaturas.lower() == "exit":
            break
        else:
            materia, calificación = asignaturas.split(",", 1)
            f_materia = materia.strip().title()
            f_calificación = float(calificación.strip())
            data_estudiante[f_materia]=f_calificación
            continue
    student_grades[name] = data_estudiante
    print(f"Student {name} successfully added to the grades management system.")
    return student_grades

def get_students(student_grades, keys):
    claves_formateadas = {}
    for nombre, calificacion in student_grades.items():
        claves_formateadas[nombre.lower()] = calificacion
    resultado_de_busqueda = {}
    for name in keys:
        nombre_formateado = name.lower()
        if nombre_formateado in claves_formateadas:
            resultado_de_busqueda[nombre_formateado.title()] = claves_formateadas[nombre_formateado]
        else:
            print(f"{nombre_formateado.title()} not found!")
    return resultado_de_busqueda

def avg_by_student(student_grades, keys = None):
    claves_formateadas = {}
    if keys is None:
        keys = student_grades.keys()
    for nombre, asignaturas in student_grades.items():
        claves_formateadas[nombre.lower()] = asignaturas
    for name in keys:
        nombre_formateado = name.lower()
        if nombre_formateado in claves_formateadas:
            asignaturas_por_estudiante = claves_formateadas[nombre_formateado]
            suma_de_calificaciones = 0
            conteo_de_materias = 0
            for calificacion in asignaturas_por_estudiante.values():
                suma_de_calificaciones = suma_de_calificaciones + calificacion
                conteo_de_materias = conteo_de_materias + 1
                promedio = suma_de_calificaciones / conteo_de_materias
            print(f"{name.title()}: {promedio}")
        else:
            print(f"{name.title()} not found!")