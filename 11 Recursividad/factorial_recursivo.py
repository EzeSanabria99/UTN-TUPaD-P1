def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:  # Caso recursivo
        return n * factorial(n - 1)

numero = int(input("Ingrese un número entero positivo: "))
for i in range(1, numero + 1):
    print(f"El factorial de {i} es {factorial(i)}")