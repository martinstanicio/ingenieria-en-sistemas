---
aliases:
  - Multiple PSK
  - PSK múltiple
created: 2025-06-12 19:50:15
modified: 2025-06-13 02:04:41
title: MPSK
---

# MPSK

Una implementación de [[PSK]], que utiliza múltiples [[Fase|Fases]]. Las más comunes son [[BPSK]] y [[QPSK]].

![[mpsk-constellation-diagram.svg]] Diagrama de constelación de [[MPSK]] ($M = 8$)

---

El [[Ancho de banda]] $B_T$ para [[MPSK]] es de la forma:

$$
B_T = \left( \frac{1 + r}{L} \right) R = \left( \frac{1 + r}{\log_2 M} \right) R
$$

- $R$: [[Velocidad de transmisión]]
- $r$: un valor relacionado con la técnica de filtrado aplicada para limitar el [[Ancho de banda]], que generalmente verifica $0 < r < 1$
- $L$: número de [[Bit|Bits]] en cada [[Elemento de señal|Elementos de señalización]]
- $M$: número de [[Elemento de señal|Elementos de señalización]] diferentes
