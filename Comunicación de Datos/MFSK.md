---
aliases:
  - Multiple FSK
  - FSK múltiple
created: 2025-06-12 19:50:15
modified: 2025-06-13 02:05:49
title: MFSK
---

# MFSK

Una implementación de [[PSK]], que utiliza múltiples [[Fase|Fases]]. Las más comunes son [[BPSK]] y [[QPSK]].

$$
s_i \left( t \right) = A \cos \left( 2 \pi f_i t \right), 1 \leq i \leq M
$$

- $f_i = f_c + \left( 2i - 1 - M \right) f_d$
- $s_i \left( t \right)$: [[Señal]] modulada en el tiempo
- $f_c$: [[Frecuencia]] de la portadora
- $f_d$: diferencia de [[Frecuencia|Frecuencias]]
- $A$: [[Amplitud]]
- $M$: número de [[Elemento de señal|Elementos de señalización]] diferentes
- $t$: tiempo

![[mfsk.jpg]] Utilización de [[Frecuencia|Frecuencias]] en [[MFSK]] ($M = 4$)

Además, se puede combinar con [[ASK]], para general una [[Señal]] con múltiples [[Fase|Fases]], cada una con múltiples [[Amplitud|Amplitudes]] posibles.

---

El [[Ancho de banda]] $B_T$ para [[MFSK]] es de la forma:

$$
B_T = \left( \frac{\left( 1 + r \right) M}{\log_2 M} \right) R
$$

- $R$: [[Velocidad de transmisión]]
- $r$: un valor relacionado con la técnica de filtrado aplicada para limitar el [[Ancho de banda]], que generalmente verifica $0 < r < 1$
- $M$: número de [[Elemento de señal|Elementos de señalización]] diferentes
