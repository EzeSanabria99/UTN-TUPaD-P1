def potencia(base, exponente):
    if exponente == 0:  # Caso base
        return 1
    else:  # Caso recursivo
        return base * potencia(base, exponente - 1)

# Prueba de la función
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es {potencia(base, exponente)}")