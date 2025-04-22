num = int(input("Ingresá un número entero positivo: "))

sumatoria = 0

for i in range(num + 1):
    sumatoria += i
print("La suma de todos los números entre 0 y ", num, "es: ", sumatoria)