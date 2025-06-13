---
aliases:
  - Frequency-Shift Keying
  - Modulación por desplazamiento de frecuencia
created: 2025-06-12 19:08:13
modified: 2025-06-13 02:03:07
title: FSK
---

# FSK

Técnica de [[Modulación]], dónde los [[Dato digital|Datos digitales]] se representan mediante múltiples [[Frecuencia|Frecuencias]] cercanas a la [[Señal]] portadora, e idealmente equidistantes a la misma.

Las implementaciones más comunes son [[BFSK]] y [[MFSK]].

---

El [[Ancho de banda]] $B_T$ para [[FSK]] es de la forma:

$$
B_T = 2 \Delta F + \left( 1 + r \right) R
$$

- $\Delta F = f_2 - f_c = f_c - f_1$: desplazamiento de la [[Frecuencia]] de la [[Señal]] modulada respecto de la [[Frecuencia]] de la portadora
- $R$: [[Velocidad de transmisión]]
- $r$: un valor relacionado con la técnica de filtrado aplicada para limitar el [[Ancho de banda]], que generalmente verifica $0 < r < 1$
