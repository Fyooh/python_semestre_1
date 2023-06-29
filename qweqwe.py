import random

# Generar lista de 20 números aleatorios en el rango de 40 a 350
numeros = random.sample(range(40, 351), 20)

# Mostrar la lista generada
print("Lista de números generados:", numeros)

# Pedir al usuario que ingrese un número para buscar en la lista
numero_buscado = int(input("Ingrese un número para buscar en la lista: "))

# Contar las ocurrencias del número buscado en la lista
ocurrencias = numeros.count(numero_buscado)

# Mostrar la cantidad de ocurrencias del número buscado
print("El número", numero_buscado, "aparece", ocurrencias, "veces en la lista.")
