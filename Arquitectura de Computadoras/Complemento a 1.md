---
aliases:
  - CA1
created: 2024-08-12 20:34:16
modified: 2024-08-13 20:01:55
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

Al igual que con [[Módulo y signo]], el **MSB** nos indica si el número es negativo, por lo que los números ==positivos se escriben de igual forma==.

$$
22_{10} \Rightarrow {0001\space0110}_2
$$

Para los negativos, tomaremos el número como ==positivo== representado con [[Módulo y signo]] (es decir, su **MSB** será $0$), y debemos invertir los valores de sus [[Bit|Bits]], también llamado *bit flip*.

$$
{-22}_{10} \Rightarrow {1110\space1001}_2
$$

> [!tip]
> El opuesto de un número positivo, es el mismo número pero con sus [[Bit|Bits]] invertidos.
