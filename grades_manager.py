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
    result = {}
    for x in keys:
        if x in student_grades:
            result[x] = student_grades[x]
        else:
            print(f"{x} not found!")
    return print(student_grades)

student_grades = {
    'Alice': {'Math': 90.5, 'English': 85.0},
    'Bob': {'Science': 88.0, 'History': 92.0}
}

result = get_students(student_grades, ["Alice", "Charlie"])