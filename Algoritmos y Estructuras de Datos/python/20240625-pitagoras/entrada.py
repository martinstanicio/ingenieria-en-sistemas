def entrada():
    try:
        ady = float(input("Ingrese el cateto adyacente: "))
        opu = float(input("Ingrese el cateto adyacente: "))

        return ady, opu
    except TypeError:
        print("Por favor ingrese números válidos")
