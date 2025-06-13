---
aliases:
  - Quadrature Amplitude Modulation
  - Modulación de amplitud en cuadratura
created: 2025-06-13 02:20:01
modified: 2025-06-13 02:30:02
title: QAM
---

# QAM

Técnica de [[Señalización]] analógica. Puede considerarse tanto una combinación de [[Modulación]] [[ASK]] y [[PSK]], como una generalización de la [[Modulación]] [[QPSK]].

[[QAM]] aprovecha la capacidad de enviar simultáneamente dos [[Señal|Señales]] diferentes sobre la misma [[Frecuencia]] portadora, utilizando dos réplicas de la misma portadora, desplazadas entre sí 90 grados.

$$
s \left( t \right) = d_1 \left( t \right) \cos \left( 2 \pi f_c t \right) + d_2 \left( t \right) \sin \left( 2 \pi f_c t \right)
$$

![[qam.jpg]]

La entrada binaria de $R$ bps se convierte en dos flujos de [[Bit|Bits]] separados, de $R / 2$ bps cada uno, tomando [[Bit|Bits]] alternos para cada flujo. Cada uno de estos flujos se modula utilizando [[Modulación]] [[ASK]] sobre su respectiva portadora. Luego, las dos [[Señal|Señales]] moduladas independientes se suman y se transmiten.

> [!warning]
> A mayor número de estados, mayor es la [[Velocidad de transmisión]] posible para un [[Ancho de banda]] dado, pero mayor será el [[Bit Error Rate]] debido al [[Ruido]] y la [[Atenuación]].
