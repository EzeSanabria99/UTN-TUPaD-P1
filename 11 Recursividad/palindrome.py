def es_palindrome(palabra):
    if len(palabra) <= 1:  # Caso base: palabra vacía o de 1 letra
        return True
    if palabra[0] != palabra[-1]:  # Si los extremos no coinciden
        return False
    return es_palindrome(palabra[1:-1])  # Caso recursivo: verificar el interior

# Prueba de la función
texto = input("Ingrese una palabra (sin espacios ni tildes): ").lower()
print(f"¿'{texto}' es palíndromo? {es_palindrome(texto)}")