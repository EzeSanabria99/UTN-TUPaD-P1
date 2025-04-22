a = int(input("Ingresá el primer número: "))
b = int(input("Ingresá el segundo número: "))

inicio = min(a, b)
fin = max(a, b)

suma = 0

for i in range(inicio + 1, fin):
    suma += i

print("La suma de los enteros entre", a, "y", b, "es: ", suma)