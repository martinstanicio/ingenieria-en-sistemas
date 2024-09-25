---
created: 2024-07-10 19:31:10
modified: 2024-09-25 02:57:36
title: Código de Hamming
---

# Código de Hamming

El [[Código de Hamming]] permite realizar **correción de errores** de un **único** [[Bit]].

<iframe width="560" height="315" src="https://www.youtube.com/embed/WdmGSWrcMvM?si=71Gd14rEM9Y2m4cz" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Para poder realizar la corrección de errores de un mensaje de $m$ [[Bit|Bits]], se necesitan $p$ [[Bit|Bits]] de **paridad**, de forma que se cumpla lo siguiente.

$$
2^p \geq (p + m) + 1
$$

> [!warning]
> El [[Código de Hamming]] no puede corregir errores de **múltiples [[Bit|Bits]]**, aunque sí puede detectarlos.

## Ejemplo (7, 4)

Para un mensaje de $4$ [[Bit|Bits]], se necesitan $3$ [[Bit|Bits]] de paridad, siendo un total de $7$ [[Bit|Bits]].

$$
2^3 = 8 \geq 8 = (3 + 4) + 1
$$

El mensaje estará organizado de la siguiente forma.

| $p_1$ | $p_2$ | $m_1$ | $p_3$ | $m_2$ | $m_3$ | $m_4$ |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| $1$   | $2$   | $3$   | $4$   | $5$   | $6$   | $7$   |

En receptor realizará la **correción de errores** analizando la siguiente tabla.


| $c_1$ | $c_2$ | $c_3$ | [[Bit]] corrupto |
| ----- | ----- | ----- | ---------------- |
| $0$   | $0$   | $0$   | Ninguno          |
| 0     | 0     | 1     | 1                |
| 0     | 1     | 0     | 2                |
| 0     | 1     | 1     | 3                |
| 1     | 0     | 0     | 4                |
| 1     | 0     | 1     | 5                |
| 1     | 1     | 0     | 6                |
| 1     | 1     | 1     | 7                |
