regiones = {
    8: {
        "Nombre": "BioBío",
        "Superficie": 23890,
        "Habitantes": 1556805
    },
    10: {
        "Nombre": "Los Lagos",
        "Superficie": 48583,
        "Habitantes": 828708
    }
}
print ("\n", regiones)

for den in regiones.values():
    superficie = den["Superficie"]
    habitantes = den["Habitantes"]
    densidad = habitantes / superficie
    den["Densidad"] = round(densidad,1)

regiones[8]["Capital"] = "Concepción"

regiones[10]["Capital"] = "Puerto Montt"

regiones[8]["Provincias"] = ["Biobío", "Arauco", "Concepción"]

regiones [10] ["Provincias"] = ["Osorno", "Lanquihue", "Chiloé", "Palena"]

regiones [8] ["Comunas"] = ("Lota", "Lebu", "Los Ángeles")

regiones [10] ["Comunas"] = ("Castro", "Puerto Varas", "Purranque")

print("\n""diccionario con las nuevas claves creadas", regiones)