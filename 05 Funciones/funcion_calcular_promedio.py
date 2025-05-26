def calcular_promedio(a, b, c):
    return (a + b + c) / 3
a = float(input("Ingresá el primer número: "))
b = float(input("Ingresá el segundo número: "))
c = float(input("Ingresá el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")