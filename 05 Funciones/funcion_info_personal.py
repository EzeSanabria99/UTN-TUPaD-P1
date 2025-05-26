def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")
nombre = input("Ingresá tu nombre: ")
apellido = input("Ingresá tu apellido: ")
edad = input("Ingresá tu edad: ")
residencia = input("¿Dónde vivís?: ")

informacion_personal(nombre, apellido, edad, residencia)