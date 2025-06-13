---
aliases:
  - Quadrature PSK
  - PSK en cuadratura
  - PSK de cuatro niveles
created: 2025-06-12 19:35:57
modified: 2025-06-12 19:50:08
title: QPSK
---

# QPSK

Una implementación de [[PSK]], más específicamente [[MPSK]], que utiliza cuatro [[Fase|Fases]].

$$
s \left( t \right) =
\left\{
    \begin{array}{r}
        A \cos \left( 2 \pi f_c t + \frac{1}{4} \pi \right) \space \text{para} \space 11 \\
        A \cos \left( 2 \pi f_c t + \frac{3}{4} \pi \right) \space \text{para} \space 01 \\
        A \cos \left( 2 \pi f_c t - \frac{3}{4} \pi \right) \space \text{para} \space 00 \\
        A \cos \left( 2 \pi f_c t - \frac{1}{4} \pi \right) \space \text{para} \space 10 \\
    \end{array}
\right.
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $A$: [[Amplitud]]
- $f_c$: [[Frecuencia]] de la portadora
- $t$: tiempo
