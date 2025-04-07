def new_func1():
    def new_func():
        edad = int(input("Coloque su edad: "))

        if edad < 18:
            print("Eres menor de edad.")

        elif edad >= 18:
            print("Eres mayor de edad.")

    new_func()

new_func1()