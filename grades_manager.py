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

def avg_by_student(student_grades, keys= None):
    claves_formateadas = {}
    if keys is None:
        keys = student_grades.keys()
    for nombre, calificacion in student_grades.items():
        claves_formateadas[nombre.lower()] = float(calificacion)
    for name in keys:
        nombre_formateado = name.lower()
        if nombre_formateado in claves_formateadas:
            calificaciones = student_grades[name]
            promedio = sum(calificaciones)/len(calificaciones)
            print(promedio)
student_grades = {
    "Alice": {"Math": 70.0, "English": 60.0},
    "Ben": {"Science": 55.0, "History": 66.0},
    "Charlie": {"Math": 90.0, "Science": 85.0}
}

avg_by_student(student_grades)