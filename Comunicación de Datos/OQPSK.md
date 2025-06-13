---
aliases:
  - Offset QPSK
  - QPSK desplazada
  - QPSK ortogonal
created: 2025-06-13 01:23:30
modified: 2025-06-13 01:58:17
title: OQPSK
---

# OQPSK

Una implementación de [[PSK]], particularmente [[QPSK]], que introduce un retardo de un tiempo de [[Bit]] en la secuencia $Q$ (en cuadratura) de la [[Señal]].

$$
s \left( t \right) = \frac{1}{\sqrt{2}} I \left( t \right) \cos \left( 2 \pi f_c t \right) - \frac{1}{\sqrt{2}} Q \left( t - T_b \right) \sin \left( 2 \pi f_c t \right)
$$

![[oqpsk.jpg]]

Al retrasar un [[Bit]], solo uno de los dos [[Bit|Bits]] en el par puede cambiar de signo en cualquier momento dado.

> [!tip]
> Esto significa que el cambio de [[Fase]] en la [[Señal]] combinada nunca supera los $90°$, a diferencia de la [[QPSK]] estándar que puede tener cambios de fase de hasta $180°$.

Esto reduce la necesidad de grandes desplazamientos de [[Fase]] a altas [[Velocidad de transmisión]], y proporciona un mejor rendimiento en canales de [[Transmisión]] que presentan ==componentes no lineales== significativas.

> [!tip]
> Al limitar los cambios de [[Fase]], es más sencillo controlar la expansión del [[Ancho de banda]] que resultaría de estas no linealidades, lo que ayuda a evitar interferencias con canales adyacentes.
