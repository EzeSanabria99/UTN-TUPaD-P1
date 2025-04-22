numero = int(input("Ingrese un numero: "))

numero_absoluto = abs(numero)

if numero_absoluto == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0
    while numero_absoluto > 0:
        numero_absoluto //= 10
        cantidad_digitos += 1
print("La cantidad de dígitos es: ", cantidad_digitos)