set1 = {100, 250, 300, 1000}
set2 = {150, 250, 500, 1000}

if 100 in set1 and 100 in set2:
    print("El valor 100 está en ambos sets")
else:
    print("El valor 100 no está en ambos sets")

if 500 or 700 in set1 and 500 or 700 in set2:
    print("El valor 500 y 700 está en alguno de los 2 sets ")
else:
    print("No se encuenytra el valor 500 y 700 en ninguno de los sets")

union_sets = set1.union(set2)
print("Ambos sets en uno solo: ",union_sets)