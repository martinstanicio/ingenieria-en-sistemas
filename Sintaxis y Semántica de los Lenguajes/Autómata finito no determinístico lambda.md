---
aliases:
  - AFND-λ
  - Autómatas finitos no determinísticos lambda
  - AEFND-λ
  - Autómata de estados finitos no determinístico lambda
  - Autómatas de estados finitos no determinísticos lambda
created: 2025-03-06 14:40:22
modified: 2025-06-22 12:14:35
title: Autómata finito no determinístico lambda
---

# Autómata finito no determinístico lambda

Un [[Autómata finito no determinístico lambda|AFND-λ]] es un [[Autómata finito]], donde la [[Función de transición]] $\delta$ está definida de la siguiente forma.

$$
\delta: K \times \Sigma \cup \set{ \lambda } \to P \left( K \right)
$$

> [!tip]
> Es decir, existen transiciones que nos permiten pasar de un [[Lógica y Estructuras Discretas/Estado|Estado]] a otro, sin consumir nada de la [[Lógica y Estructuras Discretas/Cadena|Cadena]] (ya que como $\lambda$ es la [[Cadena vacía]], consumir $\lambda$ es lo mismo que no consumir nada).

## Pasaje de AFND-λ a AFD

Sea un [[Autómata finito no determinístico lambda|AFND-λ]] $M = \left< K, \Sigma, \delta, q_0, F \right>$, luego existe un [[Autómata finito determinístico|AFD]] $M'$ tal que $L \left( M \right) = L \left( M' \right)$, donde $M' = \left< K', \Sigma, \delta', Q_0, F' \right>$ y $\delta': K' \times \Sigma \to K'$, de forma que dado $Q \in K'$:

$$
\delta' \left( Q, a \right) = \set{ p: \left( q, a \right) \vdash^* \left( p, \lambda \right), q \in Q }
$$

Para calcular los elementos restantes, aplicamos el siguiente [[Algoritmos|Algoritmo]] (utilizamos el [[Algoritmo mover]] y la [[Clausura lambda|Clausura-λ]]):

1. Hacer $Q_0 = \text{Cl-}\lambda \left( \set{ q_0 } \right)$
2. Hacer $K' = \set{ Q_0 }$ donde $K'$ es marcable y $Q_0$ está sin marcar
3. Mientras haya $T \in K'$ sin marcar:
	1. Marcar $T$
	2. Para cada $a \in \Sigma$:
		1. Hacer $U = \text{mover} \left( T, a \right)$
		2. Si $U \notin K'$:
			1. Agregar $U$ a $K'$ sin marcar
		3. $\delta' \left( T, a \right) = U$
4. Hacer $F' = \set{ x \in K': x \cap F \neq \emptyset }$
