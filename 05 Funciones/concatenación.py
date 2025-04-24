compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

posicion_lista = compras [2]

posicion_lista.append("jugo")

compras[1][1] = "tallarines"

for sublista in compras:
    if "pan" in sublista:
        sublista.remove("pan")

print(compras)