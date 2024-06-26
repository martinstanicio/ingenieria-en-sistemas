def ingresar():
    try:
        apellido = input("Ingrese el apellido: ")
        horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
        valor_hora = float(input("Ingrese el valor hora: "))
        premio = float(input("Ingrese el premio: "))

        return apellido, horas_trabajadas, valor_hora, premio
    except TypeError:
        print("Por favor ingrese números válidos")
