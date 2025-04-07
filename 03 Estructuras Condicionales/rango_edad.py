def new_func1():
    def new_func():
        edad = int(input("Coloque su edad: "))

        if edad < 12:
            print("Eres menor de 12.")

        elif edad >= 12 and edad < 18:
            print(" Eres mayor o igual que 12 años y menor que 18 años.")

        elif edad >= 18 and edad < 30:
            print("Eres mayor o igual que 18 años y menor que 30 años.")

        elif edad >= 30:
            print("Eres mayor o igual mayor que 30 años")

    new_func()

new_func1()