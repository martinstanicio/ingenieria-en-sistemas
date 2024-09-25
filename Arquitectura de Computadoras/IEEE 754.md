---
created: 2024-05-29 18:07:44
modified: 2024-09-24 16:43:49
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

## Exponente sesgado

Indica cuántas veces la base debe multiplicarse por sí misma para obtener el valor deseado, **moviendo el punto decimal** hacia la izquierda o derecha.

> [!note]
> Se almacena utilizando un **sesgo** para evitar la necesidad de representar números negativos directamente.

En lugar de guardar el exponente real, se guarda el valor del exponente sumado con un **sesgo** (un número fijo), lo que permite que el exponente **sea siempre positivo** en la representación binaria.

$$
\text{exponente} + \text{sesgo} = \text{exponente sesgado}
$$

Por ejemplo, en **precisión simple**, el sesgo es $127$.

## Mantiza normalizada

El número que queremos representar, con punto decimal desplazado tantas veces como sea necesario para que **la parte entera contenga un solo $1$**.

> [!note]
> Decimos que la mantiza está **normalizada** si su parte entera es $1$.

Como se asume que está **normalizada**, solo se almacena la **parte decimal**, mejorando la **precisión**.
