numero = int(input("Ingresá un número entero: "))
numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = (numero_invertido * 10) + digito
    numero //= 10
print("El número invertido es:", numero_invertido)
