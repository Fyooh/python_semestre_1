Nombre_estudiante = {}
Asignatura = {}
lab1={}
lab2={}
Nombre_estudiante = input("¿Cual es el nombre del estudiante?", "\n")
Asignatura = input("Ingrese la asignatura","\n" )
lab1 = float(input("Ingrese nota laboratorio 1"))
lab2 = float(input("Ingrese nota laboratorio 2"))
promedio = lab1*0.3 + lab2*0.7
Datos = {"Nombre":Nombre_estudiante,
         "Asignatura": Asignatura,
         "Laboratiorio 1": lab1,
         "Laboratorio 2": lab2,
         "Promedio": promedio}
print(Datos)



