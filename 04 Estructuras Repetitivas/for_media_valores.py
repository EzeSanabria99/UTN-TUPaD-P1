suma = 0
for i in range(100):
    numero = int(input(f"Ingresá el número {i+1}: "))
    suma += numero
media = suma / 100
print(f"La media de los 100 números ingresados es: {media}")