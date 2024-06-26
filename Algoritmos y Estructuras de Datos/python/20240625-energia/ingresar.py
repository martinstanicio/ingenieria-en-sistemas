def ingresar():
    try:
        masa = float(input("Ingrese la masa: "))
        altura = float(input("Ingrese la altura: "))
        velocidad = float(input("Ingrese la velocidad: "))

        return masa, altura, velocidad
    except TypeError:
        print("Por favor ingrese números válidos")
