---
aliases:
  - CA1
created: 2024-08-12 20:34:16
modified: 2024-08-13 19:02:11
title: Complemento a 1
---

# Complemento a 1

Una **representación** del [[Sistema binario]], que con $n$ [[Bit|Bits]], nos permite representar $2^n - 1$ números el siguiente intervalo.

$$
\left[
- 2^{(n - 1)} + 1,
+ 2^{(n - 1)} - 1
\right]
$$

Los números ==positivos se escriben de igual forma== que con [[Módulo y signo]]. Para los negativos, tomaremos el número representado con [[Módulo y signo]], pero con su **MSB**

Para obtener el [[Complemento a 2]] de un número, debemos invertir los valores de sus [[Bit|Bits]], también llamado *bit flip*, y luego sumar 1.

$$
0101_2 \Rightarrow
1010_2 + 1_2 = 1011_2
$$
