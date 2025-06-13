---
aliases:
  - Delta Modulation
  - Modulación delta
created: 2025-06-13 02:38:58
modified: 2025-06-13 11:27:33
title: DM
---

# DM

Una técnica utilizada por los [[Códec|Códecs]] en el proceso de [[Digitalización]].

> [!note]
> Busca mejorar las prestaciones y reducir la complejidad de la codificación [[PCM]].

![[dm-1.jpg]]

La [[Entradas|Entrada]] [[Señal analógica|Analógica]] se aproxima mediante una [[Análisis Matemático I/Función|Función]] escalera que en cada intervalo de muestreo $T_s$ sube o baja un nivel de cuantización $\delta$.

> [!tip]
> El comportamiento de la [[Análisis Matemático I/Función|Función]] escalera es binario: en cada instante de muestreo la [[Análisis Matemático I/Función|Función]] sube o baja una cantidad constante $\delta$.

![[dm-2.jpg]]

*   El esquema de la Modulación Delta implica una **función de realimentación**. Para cada intervalo de muestreo, la señal analógica de entrada se compara con el valor más reciente de una "función escalera".
*   Si el valor de la forma de onda muestreada excede el de la función escalera, se genera un **1**; en caso contrario, se genera un **0**.
*   De esta manera, la función escalera se ajusta constantemente en la dirección de la señal de entrada, y la **salida del proceso DM es una secuencia binaria**.

*   **Reconstrucción de la Señal**:
    *   En el receptor, esta secuencia binaria se utiliza para **reconstruir la función escalera**.
    *   La función reconstruida puede ser suavizada mediante un proceso de integración o un filtro paso bajo para generar una **aproximación analógica de la señal de entrada original**.

*   **Parámetros y Tipos de Ruido**:
    *   Existen **dos parámetros importantes** en el esquema DM:
        *   El **tamaño del paso (d)** asignado a cada dígito binario.
        *   La **frecuencia de muestreo**.
    *   La elección del tamaño del paso (d) es crucial, ya que implica un compromiso entre dos tipos de error o ruidos:
        *   **Ruido de cuantización**: Ocurre cuando la señal analógica varía muy lentamente. Este ruido es **mayor cuanto mayor sea 'd'**.
        *   **Ruido de sobrecarga en la pendiente**: Se produce cuando la señal de entrada cambia tan rápidamente que la función escalera no puede seguirla. Este ruido **aumenta al disminuir 'd'**.
