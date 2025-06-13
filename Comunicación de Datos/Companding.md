---
aliases:
  - Compresión-expansión
created: 2025-06-13 11:15:09
modified: 2025-06-13 11:19:32
title: Companding
---

# Companding

El mismo efecto de la [[Codificación no lineal]] se puede lograr mediante la ==compresión== y ==posterior expansión== de la [[Señal analógica]] de [[Entradas|Entrada]], con niveles de cuantización igualmente separados.

![[companding.jpg]] [[Análisis Matemático I/Función|Funciones]] típicas de [[Companding]]

La compresión en la [[Entradas|Entrada]] consiste en comprimir el rango de intensidades de la [[Señal]], dando una ganancia superior a las [[Señal|Señales]] de baja [[Amplitud]] en comparación con las de mayor [[Amplitud]].

> [!tip]
> Esto significa que los valores grandes de la [[Señal]] se reducen en relación con los valores pequeños, haciendo que haya más niveles de cuantización disponibles para las [[Señal|Señales]] de menor nivel cuando se tiene un número fijo de niveles.

Luego, en la salida, se expanden las muestras para restaurar sus valores originales.
