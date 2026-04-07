from grades_manager import add_student, get_students, initialize_dict, avg_by_student
print("Welcome to the Student Grades Manager!\n")
my_grades = {}
while True:
    seleccion = input("Select an option:\n1. Add a student\n2. Print student grade averages\n3. Exit\n")
    print()
    if seleccion == "1":
        add_student(my_grades)
        print()
        continue
    elif seleccion == "2":
        opciones = input("Select an option:\na. Display all students\nb. Display selected students\n")
        print()
        if opciones == "a":
            avg_by_student(my_grades)
            print()
            continue
        elif opciones == "b":
            lista_de_estudiantes = input("Enter student names (comma-separated):")
            print()
            avg_by_student(my_grades, lista_de_estudiantes)
            print()
            continue
        else:
            print("Invalid option selected!")
            print()
            continue
    elif seleccion == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option selected!")
        print()
        continue