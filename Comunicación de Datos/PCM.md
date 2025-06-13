---
aliases:
  - Pulse Code Modulation
  - Modulación por impulsos codificados
created: 2025-06-13 02:31:09
modified: 2025-06-13 02:47:07
title: PCM
---

# PCM

Técnica de [[Digitalización]] cuyo funcionamiento se basa en el [[Teorema de muestreo]]. El proceso de [[PCM]] implica:

1. Muestreo periódico de los [[Dato analógico|Datos analógicos]]
2. Cuantificación o digitalización de las muestras, denominadas [[PAM|Pulsos de amplitud modulada]]
3. La [[Señal digital]] resultante consiste en bloques de $n$ [[Bit|Bits]], donde cada número de $n$ [[Bit|Bits]] representa la [[Amplitud]] de un impulso [[PCM]]
4. En el [[Receptor]], este proceso se invierte para reproducir la [[Señal analógica]]

> [!warning]
> Al cuantificar el pulso, la [[Señal]] original solo se **aproxima** y no puede recuperarse exactamente, lo que se conoce como [[Error de cuantificación]].

Los dispositivos que realizan esta conversión se denominan [[Códec]].

> [!note]
> [[PCM]] generalmente logra una mejor [[Relación señal-ruido]] en comparación con otras técnicas como [[DM]], manteniendo la misma [[Velocidad de transmisión]].
