---
created: 2024-05-08 20:04:34
modified: 2024-05-15 19:12:01
title: Números signados en formato de punto fijo
---

# Números signados en formato de punto fijo

Existen 4 convenciones que explican este concepto.

## Módulo y signo

El **MSB** es el signo del número (si es $1$, es un número positivo, caso contrario, es negativo), y el resto de bits es el módulo del mismo.

Debido a esto, la cantidad posible de números es $2^{n - 1} - 1$. Por ejemplo, para 8 bits: $2^{8 - 1} - 1 = 127$

| Signo | Valor absoluto |     |     |     |     |     |     |
| ----- | -------------- | --- | --- | --- | --- | --- | --- |
| 1     | 0              | 0   | 0   | 0   | 1   | 0   | 1   |

## Complemento a uno

Se sustituye $0$ por $1$ y $1$ por $0$, para representar cuánto le falta al número para llegar al rango máximo.

Por ejemplo, el complemento, es decir, el número que representa al negativo, del número $12$ ($00001100$) es el $243$ ($11110011$).

El rango de representación en $2^n - 1$, ya que existen dos representaciones del cero ($00000000$ y $11111111$). Por ejemplo, si trabajamos con 8 [[Arquitectura de Computadoras/Bit|bits]], podemos representar el siguiente rango: $(-127,-0,+0,+127)$.

## Complemento a dos

Se utiliza el complemento a uno, y se suma $1$.

Por ejemplo, si tomamos al $0$ ($00000000$), le sumamos su complemento ($11111111$), y le sumamos $1$, obtenemos 9 bits ($100000000$), y el noveno se descarta, resultando en $00000000$.

El rango de representación en $2^n$, ya que existe una única representación del cero ($00000000$).

## Notación excedida 127

Tengo el mismo rango de representación, pero como está desplazado hacia la izquierda $127$ lugares, puedo representar números desde el $-127$ hasta el $128$.

Por ejemplo, el número $-12$ en esta notación, se escribe como el $115$ en el sistema binario sin signo.

 el sistema binario sin signo.
