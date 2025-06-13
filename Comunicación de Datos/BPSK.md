---
aliases:
  - Binary PSK
  - PSK binario
  - PSK de dos niveles
created: 2025-06-12 19:35:57
modified: 2025-06-12 19:49:28
title: BPSK
---

# BPSK

La implementación más simple de [[PSK]], más específicamente [[PSK multinivel]], que utiliza dos [[Fase|Fases]].

$$
s \left( t \right) =
\left\{
    \begin{array}{r}
        A \cos \left( 2 \pi f_c t \right) \space \text{para} \space 1 \\
        A \cos \left( 2 \pi f_c t + \pi \right) \space \text{para} \space 0 \\
    \end{array}
\right. =
\left\{
    \begin{array}{r}
        A \cos \left( 2 \pi f_c t \right) \space \text{para} \space 1 \\
        - A \cos \left( 2 \pi f_c t \right) \space \text{para} \space 0 \\
    \end{array}
\right.
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $A$: [[Amplitud]]
- $f_c$: [[Frecuencia]] de la portadora
- $t$: tiempo
