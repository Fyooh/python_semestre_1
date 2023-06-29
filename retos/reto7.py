def longitud(frase):
    palabras = frase.split()
    diccionario = {}
    for palabra in palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

frase = input("Ingresar una frase: ")
resultado = longitud(frase)
print(resultado)
