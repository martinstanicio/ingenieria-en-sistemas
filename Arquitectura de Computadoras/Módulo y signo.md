---
created: 2024-08-12 20:34:16
modified: 2024-08-13 19:01:32
title: Módulo y signo
---

# Módulo y signo

Una **representación** del [[Sistema binario]], que con $n$ [[Bit|Bits]], nos permite representar $2^n - 1$ números el siguiente intervalo.

$$
\left[
- 2^{(n - 1)} + 1,
+ 2^{(n - 1)} - 1
\right]
$$

El **MSB** nos indica si el número es negativo o no, similar a la [[Flags#Sign Flag (s)]]: si es $0$, el número es positivo, si es $1$, es negativo. El resto de [[Bit|Bits]] nos indica la magnitud del número.

$$
{-22}_{10} = {1001\space0110}_2
$$
