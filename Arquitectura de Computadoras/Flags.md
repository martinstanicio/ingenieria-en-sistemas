---
created: 2024-05-15 19:30:13
modified: 2024-08-13 20:43:47
title: Flags
---

# Flags

Contienen los valores de **resultados intermedios** que provienen de operaciones realizadas por la [[ALU]].

## Sign Flag (s)

Representa el **signo** de la [[Operación]].

- $s = 0$: resultado positivo ($+$)
- $s = 1$: resultado negativo ($-$)

> [!warning]
> También puede encontrarse como **Negative Flag (n)**.

## Zero Flag (z)

Indica si el resultado de la [[Operación]] **es cero o no**.

- $z = 0$: resultado es diferente de cero ($\neq 0$)
- $z = 1$: resultado es cero ($= 0$)

## Carry Flag (c)

Indica el valor del *Carry [[Bit]]* proveniente de la suma de los **MSB** de ambos números.

- $c = 0$
- $c = 1$: fue necesario un *Carry [[Bit]]*.

## Overflow Flag (v)

Indica si el resultado de la [[Operación]] se puede representar en [[Complemento a 2|CA2]], o, caso contrario, si quedó fuera del rango de representación posible.

- $v = 0$: dentro del rango
- $v = 1$: fuera del rango

> [!tip]
> Si el resultado de una [[Operación]] puede ser representado en [[Complemento a 2]], significa que podemos representarlo con la **misma cantidad de [[Bit|Bits]]** que estabamos utilizando.

Si estamos trabajando con [[Complemento a 2]], podemos saber **cuándo tenemos overflow** de la siguiente forma.

- Si sumamos dos números positivos y el resultado es negativo: $(+) + (+) = (-)$.
- SI sumamos dos números negativos y el resultado es positivo: $(-) + (-) = (+)$.
