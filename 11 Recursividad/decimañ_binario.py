def decimal_a_binario(n):
    if n == 0:  # Caso base
        return ""
    else:  # Caso recursivo
        return decimal_a_binario(n // 2) + str(n % 2)

# Prueba del funcionamiento
numero = int(input("Ingrese un número decimal: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es: {binario if binario else '0'}")