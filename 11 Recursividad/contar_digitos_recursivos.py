def contar_digito(numero, digito):
    if numero == 0:  # Caso base: no hay más dígitos
        return 0
    ultimo_digito = numero % 10
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

# Prueba de la función
num = int(input("Ingrese un número entero positivo: "))
dig = int(input("Ingrese un dígito a buscar (0-9): "))
print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}")