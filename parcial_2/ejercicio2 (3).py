notas = []
pruebas = 0
suma_notas = 0

while pruebas < 10:
    nota = float(input("Calificaciones: "))
    if 1.0 <= nota <= 7.0:
        notas.append(nota)
        suma_notas += nota
        pruebas += 1
    else:
        print("Nota incorrecta")

media = suma_notas / pruebas
notas_mas_altas = sum(nota > media for nota in notas)
notas_mas_bajas = sum(nota < media for nota in notas)

print("La media es:", media)
print("Notas más bajas", notas_mas_bajas)
print("Notas más altas:", notas_mas_altas)