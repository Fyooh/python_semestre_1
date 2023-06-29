### OPERADORES ARITMETICOS ###

print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10%2)
print(10//3)#floor division(da un numero entero más cercano)
print(2**3)#Elevar
print(2**3 + 1 + 3 / 4)

print("Hola " + "Pyhton")
# print("Hola" - "Pyhton") NO SE PUEDE
print("Hola " + str(5))
# print("Hola" + 5) NO SE PUEDE
print("Hola " * 5)

mi_flotante = 2.5 * 2
print("Hola " * int(mi_flotante))

### OPERADORES COMPARATIVOS ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Cuenta ordenación alfabética
print("Hola" > "Python")
print("Hola" < "Pyhton")
print("Hola" >= "Pyhton")
print("Hola" <= "Pyhton")
print("Hola" == "Pyhton")
print("Hola" != "Pyhton")
print(len("aaaa") >= len("abaa"))#Cuenta caracteres

### OPERADORES LÓGICOS ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" < "Python" and 4 == 4)
# print(3 > 4 not "Hola" > "Python")
print(not(3 > 4))