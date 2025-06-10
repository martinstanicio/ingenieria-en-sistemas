---
aliases:
  - Configuraciones instantáneas
  - Configuración instantánea de un AF
created: 2025-06-10 16:27:45
modified: 2025-06-10 16:46:37
title: Configuración instantánea
---

# Configuración instantánea

Es una representación de la situación actual del [[Autómata de estados finitos]]., que pertenece al [[Producto cartesiano]] $K \times \Sigma^*$.

$$
\left( q, \alpha \right) \in K \times \Sigma^*
$$

Donde $q \in K$ es un [[Lógica y Estructuras Discretas/Estado|Estado]] del [[Autómata de estados finitos|AEF]], y $\alpha \in \Sigma^*$ es la [[Lógica y Estructuras Discretas/Cadena|Cadena]] que resta consumir.

## Cambio de configuración

$$
\left( q, a\alpha \right) \vdash \left( r, \alpha \right)
\Leftrightarrow
r \in \delta \left( q, a \right)
$$

Donde $q, r \in K$ son [[Lógica y Estructuras Discretas/Estado|Estados]] del [[Autómata de estados finitos|AEF]], $a \in \Sigma$ es un elemento del [[Alfabeto]], $\alpha \in \Sigma^*$ es la [[Lógica y Estructuras Discretas/Cadena|Cadena]] que resta consumir, y $\delta: \left( K \times \Sigma \right) \to P(K)$ es la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente del [[Autómata de estados finitos|AEF]] ($P(K)$ es el [[Conjunto potencia]] de $K$).

> [!important]
> Particularmente si el [[Autómata de estados finitos|AEF]] es un [[Autómata de estados finitos|Autómata de estados finitos determinístico]], se cumple lo siguiente, debido a que $\delta: \left( K \times \Sigma \right) \to K$.
>
> $$
> \left( q, a\alpha \right) \vdash \left( r, \alpha \right)
> \Leftrightarrow
> r = \delta \left( q, a \right)
> $$

## Lenguaje aceptado

El [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por un [[Autómata de estados finitos|AEF]] $M$ se puede expresar utilizando la [[Configuración instantánea]].

$$
L \left( M \right) =
\set{ \alpha \in \Sigma^*: \left( q_0, \alpha \right) \vdash^* \left( f, \lambda \right) \land f \in F }
$$

> [!tip]
> Es decir, el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por el [[Autómata de estados finitos|AEF]] $M$ consiste de todas las [[Lógica y Estructuras Discretas/Cadena|Cadenas]] $\alpha$ que permiten pasar del [[Lógica y Estructuras Discretas/Estado|Estado]] inicial $q_0$, a un [[Lógica y Estructuras Discretas/Estado|Estado]] final $f$, con cualquier cantidad de pasos.
