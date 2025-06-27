---
aliases:
  - Amplitude Modulation
  - AM
created: 2025-06-13 11:41:10
modified: 2025-06-27 01:54:23
title: Modulación de amplitud
---

# Modulación de amplitud

Es la forma más sencilla de [[Modulación]], donde la [[Amplitud]] de la onda portadora varía de acuerdo con alguna característica de la [[Señal analógica]] modulante.

$$
s \left( t \right) = \left( 1 + n_a \cdot x\left( t \right) \right) \cos \left( 2 \pi f_c t \right)
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $\cos \left( 2 \pi f_c t \right)$: onda portadora normalizada a la [[Amplitud]] unidad
- $x \left( t \right)$: [[Señal]] de [[Entradas|Entrada]] normalizada a la [[Amplitud]] unidad
- $n_a = A_x / A_c$: índice de [[Modulación]], que es el cociente entre la [[Amplitud]] de la [[Señal]] de [[Entradas|Entrada]] y la portadora

> [!note]
> El término $1$ en la ecuación es una [[Componente continua]] que previene la pérdida de [[Información]].

> [!danger]
> Si $n_a < 1$, la envolvente será una reproducción **exacta** de la [[Señal]] original, pero si $n_a > 1$, la envolvente cruzará el eje de tiempos, perdiéndose así [[Información]].
> 
> Mientras más cerca esté $n_a$ de $1$, mejor se aprovechará la potencia utilizada para transmitir la [[Señal]].

![[am.jpg]]

> [!important]
> Este proceso permite que la [[Señal]] se transmita a una [[Frecuencia]] más alta, lo cual es necesario para una [[Transmisión]] efectiva en [[Comunicación de Datos/Medio|Medios]] como las [[Ondas de radio]], donde las [[Antena|Antenas]] requerirían tamaños imprácticos para [[Señal|Señales]] de baja [[frecuencia]].
> 
> También posibilita la [[Multiplexación]].

---

El [[Espectro]] de la [[Señal]] [[Modulación de amplitud|AM]] consiste en la portadora original más el [[Espectro]] de la [[Señal]] de [[Entradas|Entrada]] trasladado a la [[Frecuencia]] de la portadora. Este [[Espectro]] se compone de una ==banda lateral superior== y una ==banda lateral inferior==.

![[dsbtc.jpg]]

> [!tip]
> Ambas bandas laterales son réplicas del [[Espectro]] original de la señal modulante, aunque la banda lateral inferior está invertida en [[Frecuencia]].

---

Sus implementaciones más comunes son [[DSBTC]], [[SSB]], [[DSBSC]] y [[VSB]].
