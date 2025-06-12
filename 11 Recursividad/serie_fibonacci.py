def fibonacci(posicion):
    if posicion == 0:  # Caso base 1
        return 0
    elif posicion == 1:  # Caso base 2
        return 1
    else:  # Caso recursivo
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

# Se muestra la serie completa hasta la posición indicada
posicion = int(input("Ingrese la posición hasta la que desea ver la serie Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")