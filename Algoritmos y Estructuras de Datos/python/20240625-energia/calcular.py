def calcular(masa: float, altura: float, velocidad: float):
    gravedad = 9.81

    potencial = masa * gravedad * altura
    cinetica = 0.5 * masa * velocidad**2
    mecanica = potencial + cinetica

    return mecanica
