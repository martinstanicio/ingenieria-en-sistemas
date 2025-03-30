---
aliases:
  - Decibel
  - Decibelios
  - Decibels
created: 2025-03-27 16:14:25
modified: 2025-03-28 20:18:37
title: Decibelio
---

# Decibelio

Una medida adimensional, de escala ==logarítmica==, que sirve para medir la ==diferencia relativa== entre dos [[Señal|Señales]].

> [!warning]
> Es una medida ==relativa==, no absoluta.
> 
> Tanto una perdida de $10 \space \text{W}$ a $5 \space \text{W}$, como una de $1000 \space \text{W}$ a $500 \space \text{W}$ es de $3 \space \text{dB}$.

Una **ganancia** o *gain* se calcula de la siguiente forma.

$$
G_{\text{dB}} =
10 \log \frac{P_\text{salida}}{P_\text{entrada}}
$$

Una **perdida** o *loss* se calcula de la siguiente forma.

$$
L_{\text{dB}} =
- 10 \log \frac{P_\text{salida}}{P_\text{entrada}} =
10 \log \frac{P_\text{entrada}}{P_\text{salida}}
$$

Donde $P_\text{entrada}$ es la potencia de entrada y $P_\text{salida}$ la potencia de salida.

---

También se puede utilizar para medir ==diferencias de tensión==.

$$
P = \frac{V^2}{R}
$$

- $P$ es la potencia disipada en una resistencia $R$
- $V$ es la caída de tensión en la resistencia $R$

$$
L_{\text{dB}} =
10 \log \frac{P_\text{entrada}}{P_\text{salida}} =
10 \log \frac{V^2_\text{entrada} / R}{V^2_\text{salida} / R} =
20 \log \frac{V_\text{entrada}}{V_\text{salida}}
$$

---

> [!important]
> El [[Decibelio|Decibel]] es una medida **relativa**, pero existen unidades como el **decibelio-vatio** ($\text{dBW}$) y el **decibelio-milivoltio** ($\text{dBmV}$), que permiten medir niveles absolutos.
> 
> Para esto, se toma un valor de referencia.
>
> $$
> 1 \space \text{W} = 0 \space \text{dBW}
> $$
