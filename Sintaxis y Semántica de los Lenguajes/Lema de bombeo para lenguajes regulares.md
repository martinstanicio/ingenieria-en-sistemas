---
aliases:
  - Lema de bombeo para LR
  - Lema de bombeo para lenguajes tipo 3
created: 2025-06-14 20:21:30
modified: 2025-06-17 16:03:29
title: Lema de bombeo para lenguajes regulares
---

# Lema de bombeo para lenguajes regulares

Dado $\Sigma$ un [[Alfabeto]], se cumple que para todo [[Lenguaje regular]] $L$ sobre $\Sigma$ y $M = \left< K, \Sigma, \delta, q_0, F \right>$ tal que $L \left( M \right) = L$:

$$
\left( \forall L \right) \left( \exists p \right) \left( \forall \alpha \right): \alpha \in L \land \vert \alpha \vert \geq p \Rightarrow \left[ \exists x, y, z \in \Sigma^*: \alpha = xyz \land \vert xy \vert \leq p \land \vert y \vert \geq 1 \land \left( \forall i \geq 0: x y^i z \in L \right) \right]
$$

Es decir, para todo [[Lenguaje regular]] $L$, existe un ==número del lema== $p$, de forma que para toda [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha \in \Sigma^*$ que pertenece a $L$, y cuya longitud es mayor o igual a $p$, existen las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $x, y, z \in \Sigma^*$ que son las partes de $\alpha = xyz$, donde la longitud de $xy$ es menor o igual a $p$, e $y$ no es la [[Cadena vacía]], de forma que al bombear cualquier $i \in \mathbb{N}_0$, la [[Lógica y Estructuras Discretas/Cadena|Cadena]] $x y^i z$ pertenece a $L$.

![[lema-de-bombeo.jpg]] Dada $\alpha = xyz$, $a_1, \dots, a_i$ representa a $x$, $a_{i + 1}, \dots, a_k$ representa a $y$, y $a_{k + 1}, \dots, a_m$ representa a $z$

> [!important]
> El [[Lema de bombeo para lenguajes regulares]] se suele utilizar para demostrar que un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$ NO es [[Lenguaje regular|Regular]].
> 
> Para esto, se asume que $L$ es [[Lenguaje regular|Regular]], y buscamos una [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha$, con el objetivo que bombear para un dado valor de $i$, que nos devuelta una [[Lógica y Estructuras Discretas/Cadena|Cadena]] que no pertenece a $L$, haciendo que no se cumpla el [[Lema de bombeo para lenguajes regulares]] (o más concretamente, que se cumpla su contrarrecíproca), y, por lo tanto, demostrando que $L$ no es [[Lenguaje regular|Regular]].
