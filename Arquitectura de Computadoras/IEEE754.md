---
created: 2024-05-29 18:07:44
modified: 2024-05-29 18:34:39
title: IEEE754
---

# IEEE754

| Bits    | Signo | Exponente sesgado | Mantiza normalizada |
| ------- | ----- | ----------------- | ------------------- |
| 32 bits | 1     | 8                 | 23                  |
| 64 bits | 1     | 11                | 52                  |

![[ieee754.jpg]]

## Mantiza normalizada

El número que queremos representar, con la coma decimal desplazada tantas veces como sea necesario para que la parte entera contenga un solo $1$.

El número que irá en esta parte será todo lo que esté **detrás** de la coma decimal, completando con $0$ los espacios que puedan quedar vacíos del lado derecho.

## Exponente sesgado

Si para obtener la mantiza normalizada realizamos un desplazamiento de, por ejemplo, $3$ lugares, utilizando el método de desplazamiento 127, calculamos el número que debemos ingresar en el exponente sesgado.

$$
127 + 3 = 130
$$
