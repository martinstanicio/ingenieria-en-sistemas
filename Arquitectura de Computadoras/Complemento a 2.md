---
aliases:
  - CA2
created: 2024-08-12 20:34:16
modified: 2024-08-13 14:02:55
title: Complemento a 2
---

# Complemento a 2

Una **representación** del [[Sistema binario]], que con $n$ [[Bit|Bits]], nos permite representar $2^n$ números el siguiente rango.

$$
\left[
- 2^{(n - 1)},
2^{(n - 1)} - 1
\right]
$$

Para obtener el [[Complemento a 2]] de un número, debemos invertir los valores de sus [[Bit|Bits]], también llamado *bit flip*, y luego sumar 1.

$$
0101_2 \Rightarrow
1010_2 + 1_2 = 1011_2
$$
