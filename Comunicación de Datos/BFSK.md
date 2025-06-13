---
aliases:
  - Binary FSK
  - FSK binario
  - FSK de dos niveles
created: 2025-06-12 19:58:27
modified: 2025-06-12 19:59:51
title: BFSK
---

# BFSK

La implementación más simple de [[FSK]], que utiliza dos [[Frecuencia|Frecuencias]].

$$
s \left( t \right) =
\left\{
    \begin{array}{r}
        A \cos \left( 2 \pi f_1 t \right) \space \text{para} \space 1 \\
        A \cos \left( 2 \pi f_2 t \right) \space \text{para} \space 1 \\
    \end{array}
\right.
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $A$: [[Amplitud]]
- $f_1$ y $f_2$: desplazamientos de la [[Frecuencia]] portadora de igual magnitud, pero en sentidos opuestos
- $t$: tiempo
