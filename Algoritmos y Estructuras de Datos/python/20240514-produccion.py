# AyED
# Autor: Martín Stanicio
# Fecha: 14/05/2024

toneladas_producidas_manana = 0.0
toneladas_producidas_tarde = 0.0
toneladas_producidas_turno = 0.0
fecha_produccion = ""
turno_produccion = ""

toneladas_producidas_manana = 0
toneladas_producidas_tarde = 0

toneladas_producidas_turno = float(
    input("Ingrese las toneladas producidas en el turno: ")
)

while toneladas_producidas_turno != -9999:
    if toneladas_producidas_turno != -9999:
        fecha_produccion = input("Ingrese la fecha de produccion: ")
        turno_produccion = input("Ingrese el turno de produccion (M o T): ")

        match turno_produccion:
            case "M":
                toneladas_producidas_manana = (
                    toneladas_producidas_manana + toneladas_producidas_turno
                )
            case "T":
                toneladas_producidas_tarde = (
                    toneladas_producidas_tarde + toneladas_producidas_turno
                )

        toneladas_producidas_turno = float(
            input("Ingrese las toneladas producidas en el turno: ")
        )

print("Toneladas producidas en el turno mañana", toneladas_producidas_manana)
print("Toneladas producidas en el turno tarde", toneladas_producidas_tarde)
