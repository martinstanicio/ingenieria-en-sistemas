---
created: 2025-03-27 14:49:56
modified: 2025-03-27 15:05:52
title: Ancho de banda de Nyquist
---

# Ancho de banda de Nyquist

El [[Ancho de banda de Nyquist]] dice que en un [[Comunicación de Datos/Medio|Medio]] libre de [[Ruido]], la [[Capacidad del canal]] está limitada únicamente por el [[Ancho de banda]]. Dado un [[Ancho de banda]] $B$, la máxima velocidad de [[Transmisión]] que se puede alcanzar es $2B$.

> [!note]
> Esta limitación ocurre debido a la interferencia generada por la [[Distorsión de retardo]].

> [!danger]
> El [[Ancho de banda de Nyquist]] asume un [[Comunicación de Datos/Medio|Medio]] libre de [[Ruido]], algo prácticamente imposible de alcanzar en la realidad.

Para [[Señal|Señales]] ==binarias== (dos voltajes), un [[Ancho de banda]] de $B \space \text{Hz}$ soporta una velocidad de [[Transmisión]] de $2B \space \text{bps}$. Sin embargo, con [[Señalización]] ==multinivel== cada nivel de tensión puede representar más de un [[Bit]], y la formulación de Nyquist para obtener la [[Capacidad del canal]] es la siguiente.

$$
C = 2B \cdot \log_2 M
$$

Donde $M$ es el número de niveles de tensión utilizados.

> [!warning]
> El valor de $M$ está limitado por la dificultad del [[Receptor]] para interpretar [[Señal|Señales]] multinivel debido al [[Ruido]], entre otras dificultades.
