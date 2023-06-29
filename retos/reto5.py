############################ RETO 5 ################################
### SABER SI ES UN NÚMERO PAR O IMPAR Y SI ES MENOR O MAYOR A 50 ###
# Primero defino los valores
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True
def es_mayor_a_50(numero):
    if numero > 50:
        return True
    else:
        return False
# Escribimos el número
numero = int(input("Ingrese un número: "))

# Agregamos condicionales
if es_par(numero):
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
if es_mayor_a_50(numero):
    print(f"{numero} es mayor a 50.")
else:
    print(f"{numero} es menor o igual a 50.")
