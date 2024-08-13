---
aliases:
  - CA2
created: 2024-08-12 20:34:16
modified: 2024-08-13 20:03:54
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

> [!note]
> Tiene un mayor rango de representación que [[Complemento a 1|CA1]], ya que existe una única representación del $0_{10}$: ${0000\space0000}_2$.

Al igual que con [[Módulo y signo]], el **MSB** nos indica si el número es negativo, por lo que los números ==positivos se escriben de igual forma==.

$$
22_{10} \Rightarrow {0001\space0110}_2
$$

Para los negativos, debemos obtener su [[Complemento a 1]] y **sumarle $1$**.

$$
{-22}_{10} \Rightarrow {1110\space1010}_2
$$

> [!caution]
> En caso de tener un **overflow**, el Carry [[Bit]] que lo genera se debe descartar.
