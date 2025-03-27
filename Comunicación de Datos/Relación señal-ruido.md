---
aliases:
  - SNR
  - S/N
  - Signal-noise ratio
created: 2025-03-27 15:10:07
modified: 2025-03-27 15:14:45
title: Relación señal-ruido
---

# Relación señal-ruido

La relación, medida en el [[Receptor]], entre la potencia de la [[Señal]] y el [[Ruido]] que contiene.

$$
\text{SNR}_{dB} = 10 \log \frac{\text{potencia de señal}}{\text{potencia de ruido}}
$$

> [!note]
> Se expresa en **decibelios**.

Shannon afirma que la [[Capacidad del canal|Capacidad máxima del canal]] $C$, en [[Bit|Bits]] por segundo, verifica la siguiente ecuación.

$$
C = B \log_2 \left( 1 + \text{SNR} \right)
$$

> [!warning]
> Esta es la capacidad máxima teórica, pero en la práctica suele ser mucho menor, debido a factores como el [[Ruido térmico|Ruido blanco]].
