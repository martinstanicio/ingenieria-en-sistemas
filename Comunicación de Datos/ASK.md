---
aliases:
  - Amplitude-Shift Keying
  - Modulación por desplazamiento de amplitud
created: 2025-06-12 19:08:13
modified: 2025-06-13 02:01:19
title: ASK
---

# ASK

Técnica de [[Modulación]], dónde los [[Dato digital|Datos digitales]] se representan mediante dos [[Amplitud|Amplitudes]] diferentes de una [[Señal]] portadora.

![[ask.jpg]]

Comúnmente un valor binario se representa por una [[Señal]] portadora de [[Amplitud]] constante, y el otro por la ausencia de la portadora.

$$
s \left( t \right) =
\left\{
    \begin{array}{r}
        A \cos \left( 2 \pi f_c t \right) \space \text{para} \space 1 \\
        0 \space \text{para} \space 0 \\
    \end{array}
\right.
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $A$: [[Amplitud]]
- $f_c$: [[Frecuencia]] de la portadora
- $t$: tiempo

---

El [[Ancho de banda]] $B_T$ para [[ASK]] es de la forma:

$$
B_T = \left( 1 + r \right) R
$$

- $R$: [[Velocidad de transmisión]]
- $r$: un valor relacionado con la técnica de filtrado aplicada para limitar el [[Ancho de banda]], que generalmente verifica $0 < r < 1$
