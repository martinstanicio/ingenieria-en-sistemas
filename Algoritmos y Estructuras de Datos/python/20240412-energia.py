# AyED
# Autor: Martín Stanicio
# Fecha: 12/04/2024

gravedad = 9.81

masa = 0.0
velocidad = 0.0
altura = 0.0
energia_cinetica = 0.0
energia_potencial = 0.0
energia_mecanica = 0.0

try:
    masa = float(input("Ingrese la masa: "))
    velocidad = float(input("Ingrese la velocidad: "))
    altura = float(input("Ingrese la altura: "))

    energia_cinetica = 0.5 * masa * velocidad**2
    energia_potencial = masa * altura * gravedad

    energia_mecanica = energia_cinetica + energia_potencial

    print(f"Energía cinética: {energia_cinetica}")
    print(f"Energía potencial: {energia_potencial}")
    print(f"Energía mecánica: {energia_mecanica}")
except ValueError:
    print("\nPor favor ingrese números válidos")
