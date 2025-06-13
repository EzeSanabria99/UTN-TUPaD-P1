def suma_digitos(n):
    if n < 10:  # Caso base: número de un solo dígito
        return n
    else:  # Caso recursivo: último dígito + suma del resto
        return n % 10 + suma_digitos(n // 10)

# Prueba de la función
numero = int(input("Ingrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")