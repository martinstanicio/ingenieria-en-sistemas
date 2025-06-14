---
aliases:
  - AFD
  - Autómatas finitos determinísticos
  - AEFD
  - Autómata de estados finitos determinístico
  - Autómatas de estados finitos determinísticos
created: 2025-06-10 17:49:07
modified: 2025-06-14 20:09:02
title: Autómata finito determinístico
---

# Autómata finito determinístico

Un [[Autómata finito determinístico|AFD]] es un [[Autómata finito]], donde la [[Función de transición]] $\delta$ está definida de la siguiente forma.

$$
\delta: \left( K \times I \right) \to K
$$

^718883

## Pasaje de AFD a AFND

Sea un [[Autómata finito determinístico|AFD]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, luego existe un [[Autómata finito no determinístico|AFND]] $M'$ tal que $L \left( M \right) = L \left( M' \right)$, donde $M' = \left< K, \Sigma, \delta', q_0, F \right>$ y

$$
\delta': K \times \Sigma \to P \left( K \right), \delta' \left( q, a \right) = \set{ \delta \left( q, a \right) }
$$

## Pasaje de AFD a GR

Sea un [[Autómata finito determinístico|AFD]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por el mismo puede ser representado mediante una [[Gramática regular|GR]] $G = \left< N, T, P, Q_0 \right>$, tal que $L(M) = L(G)$.

1. Hacer $T = \Sigma$
2. Hacer $N = K$ (con sus [[Lógica y Estructuras Discretas/Estado|Estados]] escritos en mayúsculas)
3. Para cada [[Lógica y Estructuras Discretas/Estado|Estado]] $q \in K$ y para cada símbolo $a \in \Sigma$:
	1. Si $\delta \left( q, a \right) = r$:
		1. Agregar a $P$ la producción $\left( Q \to a R \right)$, con $Q, R \in N$
		2. Si $r \in F$:
			1. Agregar a $P$ la producción $\left( Q \to a \right)$
4. Si $q_0 \in F$:
	1. Agregar a $P$ la producción $\left( Q_0 \to \lambda \right)$

## Pasaje de AFD a ER

Sea $L_0$ el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado por el [[Autómata finito determinístico|AFD]] $M$ desde su [[Lógica y Estructuras Discretas/Estado|Estado]] inicial $q_0$, entonces $L_0$ puede ser expresado mediante una [[Expresión regular]].

Supongamos que $M$ tiene el [[Alfabeto]] $\Sigma = \set{ a, b}$, y sea $\delta \left( q_0, a \right) = q_1$ y $\delta \left( q_0, b \right) = q_2$, podemos expresar [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado desde $q_1$ y $q_2$ como $D_a \left( L_0 \right)$ y $D_b \left( L_0 \right)$ respectivamente. Así, podemos notar:

$$
L_0 = a L_1 + b L_2
$$

Donde $L_1$ y $L_2$ son los [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]] aceptados por $M$ desde $q_1$ y $q_2$ respectivamente.

> [!note]
> El proceso se repite para cada [[Lógica y Estructuras Discretas/Estado|Estado]] ante cada símbolo del [[Alfabeto]] (por el momento, solo $L_1$ y $L_2$), hasta llegar a una definición formada únicamente por símbolos, no por [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]].

> [!important]
> En los [[Lógica y Estructuras Discretas/Estado|Estados]] finales $L_i$, si ingresa la [[Cadena vacía]] $\lambda$, el lexema sigue siendo válido. Por lo tanto, es necesario agregar $\lambda$ a la [[Expresión regular|ER]] que define al [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] aceptado desde un [[Lógica y Estructuras Discretas/Estado|Estado]] final.
>
> $$
> L_i = a L_j + b L_k + \lambda
> $$
>
> Y en los [[Lógica y Estructuras Discretas/Estado|Estados]] trampa $L_t$, no existe ninguna [[Lógica y Estructuras Discretas/Cadena|Cadena]] adicional que haga que el lexema sea válido, por lo que es necesario agregar $\emptyset$ a su [[Expresión regular|ER]] asociada.
>
> $$
> L_t = a L_t + b L_t + \emptyset
> $$

> [!tip]
> Para resolver ecuaciones como $L_t = a L_t + b L_t + \emptyset$, es conveniente y necesario utilizar el [[Lema de Arden]]:
>
> $$
> \left[ L_t = \left( a + b \right) L_t + \emptyset \right] \land \lambda \notin \left( a + b \right) \Rightarrow L_t = \left( a + b \right)^* \emptyset = \emptyset
> $$
