# AyED
# Autor: Martín Stanicio
# Fecha: 16/04/2024

# Se ingresa un número entero, mostrar el número inverso.

try:
    numero_ingresado = int(input("Ingrese un número entero: "))
except ValueError:
    print("\nPor favor ingrese números válidos")

digitos_del_numero = len(str(numero_ingresado))
componentes_del_numero = []

for i in range(digitos_del_numero):
    digito = i + 1

    # primer digito
    if digito == 1:
        componentes_del_numero.append(
            numero_ingresado // (10 ** (digitos_del_numero - 1))
        )

        print(componentes_del_numero[i])

        continue

    # ultimo digito
    elif digito == digitos_del_numero:
        componentes_del_numero.append(numero_ingresado % 10)

        print(componentes_del_numero[i])

        continue

    else:
        componentes_del_numero.append(
            numero_ingresado
            % 10 ** (digitos_del_numero - i)
            // 10 ** (digitos_del_numero - digito)
        )
        print(componentes_del_numero[i])

palindromo = 0

for i in range(digitos_del_numero):
    digito = i + 1

    palindromo += componentes_del_numero[digitos_del_numero - digito] * (
        10 ** (digitos_del_numero - digito)
    )

print(palindromo)
