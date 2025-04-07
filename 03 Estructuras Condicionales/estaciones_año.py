# Pedir datos al usuario
hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").strip().upper()
mes = int(input("¿En qué mes está? (1-12): "))
dia = int(input("¿Qué día del mes es? (1-31): "))

# Determinar estación según hemisferio y fecha
if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = estacion_sur = "Fecha inválida"

# Mostrar estación según el hemisferio
if hemisferio == "N":
    print("La estación en el hemisferio norte es:", estacion_norte)
elif hemisferio == "S":
    print("La estación en el hemisferio sur es:", estacion_sur)
else:
    print("Hemisferio no reconocido. Use 'N' o 'S'.")