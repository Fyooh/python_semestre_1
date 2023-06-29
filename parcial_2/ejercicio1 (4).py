def generar_enteros():
    suma_divisibles = 0
    suma_impares = 0
    numero = 2

    while numero < 30:
        if numero % 5 == 0:
            suma_divisibles += numero
        if numero % 2 != 0:
            suma_impares += numero
        numero += 3

    return suma_divisibles, suma_impares

suma_divisibles, suma_impares = generar_enteros()
print("Suma de divisivles: ", suma_divisibles)
print("Suma de impares: ", suma_impares)