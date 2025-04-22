import random

secreto = random.randint(0,9)

intentos = 0

while True:
    adivina = int(input("Adiviná el número (entre 0 y 9): "))
    intentos += 1
    if adivina == secreto:
        break
print("¡Correcto! El número era ", secreto)
print("Usaste ", intentos, "intentos")