---
aliases:
  - Lema de bombeo para LLC
  - Lema de bombeo para lenguajes tipo 2
created: 2025-06-14 20:21:30
modified: 2025-06-17 16:49:56
title: Lema de bombeo para lenguajes libres de contexto
---

# Lema de bombeo para lenguajes libres de contexto

Dado $\Sigma$ un [[Alfabeto]], se cumple que para todo [[Lenguaje libre de contexto]] $L$ sobre $\Sigma$ y $M = \left< K, \Sigma, \delta, q_0, F \right>$ tal que $L \left( M \right) = L$:

$$
\left( \forall L \right) \left( \exists p \right) \left( \forall \alpha \right): \alpha \in L \land \vert \alpha \vert \geq p \Rightarrow \left[ \exists r, x, y, z, s \in \Sigma^*: \alpha = rxyzs \land \vert xyz \vert \leq p \land \vert x \vert \geq 1 \land \vert z \vert \geq 1 \land \left( \forall i \geq 0: r x^i y z^i s \in L \right) \right]
$$

Es decir, para todo [[Lenguaje libre de contexto]] $L$, existe un ==número del lema== $p$, de forma que para toda [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha \in \Sigma^*$ que pertenece a $L$, y cuya longitud es mayor o igual a $p$, existen las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $r, x, y, z, s \in \Sigma^*$ que son las partes de $\alpha = rxyzs$, donde la longitud de $xyz$ es menor o igual a $p$, y ni $x$ ni $y$ son la [[Cadena vacía]], de forma que al bombear cualquier $i \in \mathbb{N}_0$, la [[Lógica y Estructuras Discretas/Cadena|Cadena]] $r x^i y z^i s$ pertenece a $L$.

> [!important]
> El [[Lema de bombeo para lenguajes libres de contexto]] se suele utilizar para demostrar que un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L$ NO es [[Lenguaje libre de contexto|Libre de contexto]].
> 
> Para esto, se asume que $L$ es [[Lenguaje libre de contexto|Libre de contexto]], y buscamos una [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha$, con el objetivo que bombear para un dado valor de $i$, que nos devuelta una [[Lógica y Estructuras Discretas/Cadena|Cadena]] que no pertenece a $L$, haciendo que no se cumpla el [[Lema de bombeo para lenguajes libres de contexto]] (o más concretamente, que se cumpla su contrarrecíproca), y, por lo tanto, demostrando que $L$ no es [[Lenguaje libre de contexto|Libre de contexto]].
