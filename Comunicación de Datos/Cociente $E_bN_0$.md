---
created: 2025-03-27 15:21:45
modified: 2025-03-27 15:39:38
title: Cociente $E_b/N_0$
---

# Cociente $E_b/N_0$

Es el cociente entre la [[Energía]] de la [[Señal]] por [[Bit]] y la densidad de potencia del [[Ruido]] por hercio.

$$
\frac{E_b}{N_0} =
\frac{S / R}{N_0} =
\frac{S}{kTR}
$$

- $E_b$ es la [[Energía]] de la [[Señal]] por [[Bit]]
- $N_0$ es la densidad de potencia del [[Ruido]] por hercio
- $S$ es la potencia de la [[Señal]]
- $R$ es la velocidad de [[Transmisión]]
- $k$ es la [[Constante de Boltzmann]]
- $T$ es la [[Temperatura]]

También lo podemos expresar en decibelios.

$$
\left( \frac{E_b}{N_0} \right)_{\text{dB}} =
S_{\text{dBW}} - 10 \log R - 10 \log k - 10 \log T
$$

---

Podemos calcular $E_b$ utilizando la potencia de la [[Señal]] $S$ y el tiempo necesario para transmitir un [[Bit]] $T_b$.

$$
E_b = S \cdot T_b
$$

> [!tip]
> La ventaja del [[Cociente $E_bN_0$|Cociente $E_b/N_0$]] sobre la [[Relación señal-ruido]] es que el primero tiene en cuenta el [[Ancho de banda]].
