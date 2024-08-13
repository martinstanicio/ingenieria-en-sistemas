---
created: 2024-04-24 18:04:59
modified: 2024-08-12 21:22:42
title: Sistema binario
---

# Sistema binario

Es un [[Sistema numérico]]. Está conformado por ==dos elementos==, el [[Conjunto binario]].

$$
0011_2 = 0 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 1 \cdot 2^0 = 3
$$

Cada cifra de un número binario es un [[Bit]]. El primero se denomina **MSB** (*Most Significant Bit*), y el último **LSB** (*Least Significant Bit*).

> [!tip]
> Con $n$ [[Bit|Bits]] se pueden representar valores entre $0$ y $2^n - 1$.

## Operaciones con binarios no signados

| **Suma**                       | **Resta**                      | **Multiplicación** | **División**      |
| ------------------------------ | ------------------------------ | ------------------ | ----------------- |
| $0 + 0 = 0$                    | $0 - 0 = 0$                    | $0 \cdot 0 = 0$    | $\frac{0}{0} = 0$ |
| $0 + 1 = 1$                    | $0 - 1 = 1$ (Acarreo negativo) | $0 \cdot 1 = 0$    | $\frac{0}{1} = 0$ |
| $1 + 0 = 1$                    | $1 - 0 = 1$                    | $1 \cdot 0 = 0$    | $\frac{1}{0} = 0$ |
| $1 + 1 = 0$ (Acarreo positivo) | $1 - 1 = 0$                    | $1 \cdot 1 = 1$    | $\frac{1}{1} = 0$ |
