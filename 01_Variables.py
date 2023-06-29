#Variables
mi_variable_string = "Mi variable string"
print (mi_variable_string)

mi_variable_int = 5
print(mi_variable_int)
mi_variable_int_a_str = str(mi_variable_int)
print(mi_variable_int_a_str)
print(type(mi_variable_int_a_str))

mi_variable_bool = False
print(mi_variable_bool)

#Concatenación de variables en un print
print(mi_variable_string, mi_variable_int, mi_variable_bool)
print(type(print("Mi cadena de texto"))) #Tipo NoneType
print("Este el valor de", mi_variable_bool)

# Algunas funciones del sistema
print(len(mi_variable_int_a_str))
print(len(mi_variable_string))

# Variables en una sola línea. ¡Cuidado de abusar de esta sintaxis!
nombre, apellido, alias, edad = "Alberto", "Rodríguez", "El folla abuelas", 20
print("Me llamo",nombre, apellido,"Soy", alias,"y tengo", edad)

"""nombre = input("¿Cual es tu nombre?")
 edad = input("¿Cuantos años tienes?")
print(nombre)
print(edad)
"""
# Cambiamos su tipo
nombre = 35
edad = "Alberto" 
print(nombre)
print(edad)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(type(address))



