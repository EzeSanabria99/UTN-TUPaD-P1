def new_func1():
    def new_func():
        nota = int(input("Coloque la nota del estudiante: "))

        if nota >= 7:
            print("Aprobado")

        elif nota < 7:
            print("Desaprobado")

    new_func()

new_func1()