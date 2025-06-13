---
aliases:
  - Pulse Code Modulation
  - Modulación por impulsos codificados
created: 2025-06-13 02:31:09
modified: 2025-06-13 11:12:12
title: PCM
---

# PCM

Técnica de [[Digitalización]] cuyo funcionamiento se basa en el [[Teorema de muestreo]]. El proceso de [[PCM]] implica:

1. Muestreo periódico de los [[Dato analógico|Datos analógicos]] en impulsos [[PAM]], discretizados en el tiempo
2. Cuantización en impulsos [[PCM]], discretizados en [[Amplitud]] y tiempo
3. Digitalización de las muestras mediante un [[Codificador]]
4. La [[Señal digital]] resultante consiste en bloques de $n$ [[Bit|Bits]], donde cada número de $n$ [[Bit|Bits]] representa la [[Amplitud]] de un impulso [[PCM]]
5. En el [[Receptor]], este proceso se invierte para reproducir la [[Señal analógica]]

![[pcm-1.jpg]]

> [!warning]
> Al cuantificar los [[PAM]], la [[Señal]] original solo se **aproxima** y no puede recuperarse exactamente, lo que se conoce como [[Error de cuantificación]].

![[pcm-2.jpg]]

Los dispositivos que realizan esta conversión se denominan [[Códec]].

> [!note]
> [[PCM]] generalmente logra una mejor [[Relación señal-ruido]] en comparación con otras técnicas como [[DM]], manteniendo la misma [[Velocidad de transmisión]].
