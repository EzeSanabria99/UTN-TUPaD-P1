def saludar_usuario(nombre):
    return f"Hola {nombre}!"
nombre_ingresado = input("Ingresá tu nombre: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)