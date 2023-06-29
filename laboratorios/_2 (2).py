a = [10,9,12,15,18]
b = [21,8,15,3,12]
lista_junta = a+b
print (lista_junta)
lista_junta.insert(2, 30)
print (lista_junta)
lista_junta.sort()
print ("\n" "Lista ordenada de forma ascedente", lista_junta)
lista_junta.extend([4, 5, 6])
print("4,5 y 6 al final de la lista", lista_junta)
suma_de_la_lista = sum(lista_junta)
print("Lista sumada :", suma_de_la_lista)
