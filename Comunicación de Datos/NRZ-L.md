---
aliases:
  - No retorno a nivel cero
  - Nonreturn to zero level
created: 2025-06-12 12:28:07
modified: 2025-06-12 13:12:22
title: NRZ-L
---

# NRZ-L

Es la forma más común y ==sencilla== de transmitir [[Señal digital|Señales digitales]]. Utiliza un nivel de tensión diferente para cada dígito binario, que se mantiene constante durante toda la duración del [[Bit]].

![[nrz-l.jpg]]

> [!warning]
> La principal limitación de [[NRZ-L]] es que, la mayoría de las veces, la cantidad de $0$ y $1$ no es la misma, lo que genera una [[Componente continua]] en la [[Señal]].

Además, [[NRZ-L]] no tiene 

- **Falta de Capacidad de Sincronización**: Otra desventaja importante es la ausencia de capacidad de sincronización.
    - Cuando hay una **cadena larga de unos o ceros**, la salida en NRZ-L es una tensión constante durante un período prolongado.
    - En estas condiciones, cualquier desajuste entre los relojes del transmisor y el receptor puede provocar una **pérdida de sincronización** entre ambos. Esto se debe a que la ausencia de transiciones en la señal dificulta que el receptor mantenga su reloj sincronizado con el del emisor.
