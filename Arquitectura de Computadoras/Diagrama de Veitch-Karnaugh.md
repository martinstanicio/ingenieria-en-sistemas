---
created: 2024-06-26 18:14:01
modified: 2024-08-27 21:09:20
title: Diagrama de Veitch-Karnaugh
---

# Diagrama de Veitch-Karnaugh

Es una herramienta gráfica utilizada para simplificar expresiones [[Álgebra de Boole|booleanas]].

> [!tip]
> [Karnaugh-Veitch Map](https://www.mathematik.uni-marburg.de/~thormae/lectures/ti1/code/karnaughmap/)

Representa visualmente la [[Tabla de verdades]] de una [[Análisis Matemático I/Función|Función]]. Esto puede ser útil para identificar más fácilmente a las partes de la misma, y así reducir la cantidad de [[Compuertas lógicas]] necesarias.

![[veitch-karnaugh-1.jpg]]

## Tabla a diagrama

Pasamos la información de la [[Tabla de verdades]] al [[Diagrama de Veitch-Karnaugh]].

![[veitch-karnaugh-2.jpg]]

## Agrupamiento

Agrupo $1$ o $0$ dependiendo de si trabajo con [[Minitérmino (m)|Minitérminos]] o [[Maxitérmino (M)|Maxitérminos]]. Agrupamos la mayor cantidad de celdas posibles, en potencias de $2$.

![[veitch-karnaugh-3.jpg]]

![[veitch-karnaugh-4.jpg]]

## Grupos a funciones

Se utiliza la información de los grupos formados para obtener una [[Análisis Matemático I/Función|Función]] simplificada.

![[veitch-karnaugh-5.jpg]]

> [!note]
> A veces es posible operar algebraicamente con la [[Análisis Matemático I/Función|Función]] resultante para obtener una expresión aún más simple.
