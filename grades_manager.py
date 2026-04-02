def initialize_dict(student_name, subject_grades):
    diccionario_inicial = {
        student_name:subject_grades
    }
    return print(diccionario_inicial)

def add_student(student_grades = {}):
    name = input("Enter student name:\n").title()
    asignaturas = input("Enter subject and grade (or 'exit' to finish):\n")
    student_grades = {
        name : asignaturas
    }
    return print(student_grades)

student_grades = {
    "Alice": {
        "Math": 90.5,
        "English": 85.0,
        "Science": 92.0
    },
    "Bob": {
        "Math": 78.0,
        "English": 82.5,
        "History": 88.0
    },
    "Charlie": {
        "Science": 95.0,
        "English": 89.5
    }
}

student_data = {}
updated_data = add_student(student_data)