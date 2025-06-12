---
aliases:
  - No retorno a nivel cero
  - Nonreturn to zero level
created: 2025-06-12 12:28:07
modified: 2025-06-12 15:04:47
title: NRZ-L
---

# NRZ-L

Es la forma más común y ==sencilla== de [[Codificación digital]]. Utiliza un nivel de tensión diferente para cada dígito binario, que se mantiene constante durante toda la duración del [[Bit]].

![[nrz-l.jpg]]

> [!warning]
> La principal limitación de [[NRZ-L]] es que, la mayoría de las veces, la cantidad de $0$ y $1$ no es la misma, lo que genera una [[Componente continua]] en la [[Señal]].

Además, [[NRZ-L]] no tiene capacidad de [[Sincronización]], ya que [[Lógica y Estructuras Discretas/Cadena|Cadenas]] largas de ceros o unos generan un pulso de tensión constante durante un período prolongado. En estas condiciones, cualquier desajuste entre los relojes del [[Emisor]] y el [[Receptor]] puede provocar una pérdida de [[Sincronización]] entre ambos.
