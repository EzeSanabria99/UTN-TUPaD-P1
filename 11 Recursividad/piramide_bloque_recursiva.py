def contar_bloques(n):
    if n == 1:  # Caso base: nivel superior con 1 bloque
        return 1
    else:  # Caso recursivo: bloques en este nivel + bloques en niveles superiores
        return n + contar_bloques(n - 1)

# Prueba de la función
niveles = int(input("Ingrese el número de bloques en el nivel más bajo: "))
print(f"Se necesitan {contar_bloques(niveles)} bloques para construir la pirámide")