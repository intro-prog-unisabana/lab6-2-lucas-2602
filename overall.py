def student_averages(students):
    promedios = {}
    for estudiante, tareas in students.items():
        notas = tareas.values()
        promedio = sum(notas)/len(notas)
        promedios[estudiante] = round(promedio)
    return promedios

def assignment_averages(students):
    tarea1 = []
    tarea2 = []
    tarea3 = []
    for valor in students.values():
        tarea1.append(valor["hw1"])
        tarea2.append(valor["hw2"])
        tarea3.append(valor["hw3"])
    promedio1 = round(sum(tarea1)/len(tarea1))
    promedio2 = round(sum(tarea2)/len(tarea2))
    promedio3 = round(sum(tarea3)/len(tarea3))
    diccionario_promedios = {
        "hw1": promedio1,
        "hw2": promedio2,
        "hw3": promedio3
    }
    return diccionario_promedios