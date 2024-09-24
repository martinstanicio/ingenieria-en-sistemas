---
created: 2024-05-29 18:07:44
modified: 2024-09-24 15:26:59
title: IEEE 754
---

# IEEE 754

Un **estándar técnico** para la representación de números de **punto flotante**. Esto se hace utilizando tres componentes:

   - **Signo**: Indica si el número es positivo o negativo.
   - **Exponente sesgado**: Determina la magnitud del número (el factor por el cual se multiplica la base).
   - **Mantisa normalizada**: Representa la precisión del número.

> [!note]
> Gracias al uso del **punto flotante**, se pueden representar números extremadamente grandes o pequeños con **suficiente precisión** para la mayoría de las aplicaciones.

Algunos de los formatos más comunes, son los siguientes.

| Nombre     | Alias            | [[Bit\|Bits]] del signo | [[Bit\|Bits]] del exponente | [[Bit\|Bits]] de la mantisa |
| ---------- | ---------------- | ----------------------- | --------------------------- | --------------------------- |
| `binary16` | Precisión media  | 1                       | 5                           | 10                          |
| `binary32` | Precisión simple | 1                       | 8                           | 23                          |
| `binary64` | Precisión doble  | 1                       | 11                          | 52                          |

> [!important]
> No siempre puede lograrse una **representación exacta**, lo que introduce pequeños errores en los cálculos. El [[IEEE 754]] define varios modos de redondeo para **minimizar estos errores**.

## Mantiza normalizada

El número que queremos representar, con la coma decimal desplazada tantas veces como sea necesario para que la parte entera contenga un solo $1$.

El número que irá en esta parte será todo lo que esté **detrás** de la coma decimal, completando con $0$ los espacios que puedan quedar vacíos del lado derecho.

## Exponente sesgado

Si para obtener la mantiza normalizada realizamos un desplazamiento de, por ejemplo, $3$ lugares, utilizando el método de desplazamiento 127, calculamos el número que debemos ingresar en el exponente sesgado.

$$
127 + 3 = 130
$$
