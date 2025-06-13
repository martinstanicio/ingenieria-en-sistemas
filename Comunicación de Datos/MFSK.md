---
aliases:
  - Multiple FSK
  - FSK múltiple
created: 2025-06-12 19:50:15
modified: 2025-06-13 01:21:14
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
