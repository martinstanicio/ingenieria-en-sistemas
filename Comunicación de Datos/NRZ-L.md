---
aliases:
  - No retorno a nivel cero
  - Nonreturn to zero level
created: 2025-06-12 12:28:07
modified: 2025-06-12 13:14:38
title: NRZ-L
---

# NRZ-L

Es la forma más común y ==sencilla== de transmitir [[Señal digital|Señales digitales]]. Utiliza un nivel de tensión diferente para cada dígito binario, que se mantiene constante durante toda la duración del [[Bit]].

![[nrz-l.jpg]]

> [!warning]
> La principal limitación de [[NRZ-L]] es que, la mayoría de las veces, la cantidad de $0$ y $1$ no es la misma, lo que genera una [[Componente continua]] en la [[Señal]].

Además, [[NRZ-L]] no tiene capacidad de [[Sincronización]], por lo que, cuando hay una [[Lógica y Estructuras Discretas/Cadena|Cadena]] larga de unos o ceros, la salida en [[NRZ-L]] es una tensión constante durante un período prolongado. En estas condiciones, cualquier desajuste entre los relojes del [[Emisor]] y el [[Receptor]] puede provocar una pérdida de [[Sincronización]] entre ambos.
