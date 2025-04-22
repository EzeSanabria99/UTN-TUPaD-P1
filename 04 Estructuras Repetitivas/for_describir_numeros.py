pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    numero = int(input(f"Ingresá el número {i+1}: "))

    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")