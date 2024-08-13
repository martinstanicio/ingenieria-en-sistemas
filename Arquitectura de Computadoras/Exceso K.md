---
created: 2024-08-13 13:49:31
modified: 2024-08-13 13:59:41
title: Exceso K
---

# Exceso K

Una **representación** del [[Sistema binario]], que con $n$ [[Bit|Bits]] y un exceso $k$, nos permite representar el siguiente rango.

$$
\left[
-k,
2^n - 1 - k
\right]
$$

> [!note]
> Si estamos trabajando con 8 [[Bit|Bits]], el [[Exceso K]] más común es **Exceso 127**, ya que nos permite representar el rango $[-127, 128]$.

Para obtener la representación [[Exceso K]] de un número $x$, el resultado será $x + k$. Por ejemplo, si trabajamos con $n = 8$, $k = 127$ y $x = 22$:

$$
{0001\space0110}_2 \Rightarrow
{0001\space0110}_2 + {0111\space1111}_2 = {1001\space0101}_2
$$
