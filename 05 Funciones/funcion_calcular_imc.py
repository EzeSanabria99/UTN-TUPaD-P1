def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresá tu peso en kilogramos: "))
altura = float(input("Ingresá tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")