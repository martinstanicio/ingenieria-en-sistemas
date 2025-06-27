---
created: 2025-06-13 12:49:12
modified: 2025-06-27 01:59:51
title: Modulación angular
---

# Modulación angular

Un tipo de [[Modulación]] en la que se varía el ángulo de la onda portadora, ya sea mediante [[Modulación de frecuencia]] o [[Modulación de fase]].

La señal modulada resultante de la Modulación Angular, denotada como `s(t)`, se puede expresar matemáticamente como `s(t) = Ac cos [2πfct + θ(t)]`. En esta expresión, `Ac` representa la amplitud de la portadora, `fc` es la frecuencia de la portadora, y `θ(t)` es la desviación de fase instantánea de la señal portadora en cualquier momento dado.

La Modulación Angular engloba dos formas específicas:

- **Modulación de Fase (PM)**: En este caso, la **fase instantánea (`θ(t)`) es directamente proporcional a la señal moduladora (`m(t)`)**. La relación se define como `θ(t) = npm(t)`, donde `np` es el índice de modulación de fase.
- **Modulación de Frecuencia (FM)**: Aquí, la **derivada de la fase (`θ'(t)`) es proporcional a la señal moduladora (`m(t)`)**. Se expresa como `θ'(t) = nfm(t)`, siendo `nf` el índice de modulación de frecuencia. La frecuencia instantánea (`fi(t)`) de la señal modulada es `fi(t) = fc + (1/2π)θ'(t)`.

Un aspecto importante de la Modulación Angular es su **naturaleza no lineal**, lo que significa que tiende a generar un amplio rango de frecuencias. En el escenario más general, la transmisión de una señal FM o PM requeriría teóricamente un ancho de banda infinito. Sin embargo, en la práctica, el ancho de banda (`BT`) necesario puede aproximarse mediante la ley de Carson, dada por `BT = 2(b + 1)B`, donde `b` está relacionado con el índice de modulación y `B` es el ancho de banda de la señal moduladora. Ambas modulaciones, FM y PM, suelen necesitar un **ancho de banda mayor que la Modulación de Amplitud (AM)**.







Un tipo de [[Modulación]] en la que se ==varía el ángulo de una onda portadora==.

$$
s \left( t \right) = A_c \cos \left( 2 \pi f_c t + \phi \left( t \right) \right)
$$
- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $A_c$: [[Amplitud]] de la portadora
- $f_c$: [[Frecuencia]] de la portadora
- $\phi \left( t \right)$: desviación de [[Fase]] instantanea de la portadora en
- $\cos \left( 2 \pi f_c t \right)$: onda portadora normalizada a la [[Amplitud]] unidad
- $x \left( t \right)$: [[Señal]] de [[Entradas|Entrada]] normalizada a la [[Amplitud]] unidad
- $n_a = A_x / A_c$: índice de [[Modulación]], que es el cociente entre la [[Amplitud]] de la [[Señal]] de [[Entradas|Entrada]] y la portadora



---

- [[Modulación de frecuencia]]
- [[Modulación de fase]]
