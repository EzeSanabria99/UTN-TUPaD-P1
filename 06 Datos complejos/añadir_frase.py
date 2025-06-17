frase = input("Ingrese una frase: ")
palabras = frase.split()

# Palabras únicas
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Recuento de palabras
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1
print("Recuento:", recuento)