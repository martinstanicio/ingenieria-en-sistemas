---
aliases:
  - Delta Modulation
  - DM
created: 2025-06-13 02:38:58
modified: 2025-06-14 15:38:31
title: Modulación delta
---

# Modulación delta

Una técnica utilizada por los [[Códec|Códecs]] en el proceso de [[Digitalización]].

> [!note]
> Busca mejorar las prestaciones y reducir la complejidad de la codificación [[PCM]].

![[dm-1.jpg]]

La [[Entradas|Entrada]] [[Señal analógica|Analógica]] se aproxima mediante una [[Análisis Matemático I/Función|Función]] escalera que en cada intervalo de muestreo $T_s$ sube o baja un nivel de cuantización $\delta$.

> [!tip]
> El comportamiento de la [[Análisis Matemático I/Función|Función]] escalera es binario: en cada instante de muestreo la [[Análisis Matemático I/Función|Función]] sube o baja una cantidad constante $\delta$.

![[dm-2.jpg]]

En el [[Receptor]], esta secuencia binaria se utiliza para reconstruir la [[Análisis Matemático I/Función|Función]] escalera.

> [!note]
> La [[Análisis Matemático I/Función|Función]] reconstruida puede ser suavizada mediante un **proceso de integración** o un **filtro paso bajo** para generar una aproximación analógica de la [[Señal]] de [[Entradas|Entrada]] original.

> [!warning]
> Cuando la [[Señal analógica]] varía muy lentamente, el [[Error de cuantificación|Ruido de cuantificación]] es mayor cuanto mayor sea el tamaño del escalón $\delta$.
> 
> Cuando la [[Señal analógica]] cambia tan rápidamente que la [[Análisis Matemático I/Función|Función]] escalera no puede seguirla, el [[Ruido]] de sobrecarga de la pendiente es mayor cuanto menor sea $\delta$.
