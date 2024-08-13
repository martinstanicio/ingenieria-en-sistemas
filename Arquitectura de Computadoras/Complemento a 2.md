---
aliases:
  - CA2
created: 2024-08-12 20:34:16
modified: 2024-08-13 19:19:10
title: Complemento a 2
---

# Complemento a 2

Una **representación** del [[Sistema binario]], que con $n$ [[Bit|Bits]], nos permite representar $2^n$ números el siguiente intervalo.

$$
\left[
- 2^{(n - 1)},
+ 2^{(n - 1)} - 1
\right]
$$

Al igual que con [[Módulo y signo]], el **MSB** nos indica si el número es negativo, por lo que los números ==positivos se escriben de igual forma==.

$$
22_{10} \Rightarrow {0001\space0110}_2
$$

Para los negativos, debemos obtener su [[Complemento a 1]] y **sumarle $1$**.

$$
{-22}_{10} \Rightarrow {1110\space1010}_2
$$
