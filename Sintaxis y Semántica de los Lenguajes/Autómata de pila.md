---
created: 2025-06-14 23:12:10
modified: 2025-06-14 23:36:12
title: Autómata de pila
---

# Autómata de pila

$$
M = \left< K, \Sigma, \Gamma, \delta, q_0, z_0, F \right>
$$

- $K$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]]
- $\Sigma$: [[Alfabeto]] finito de [[Entradas|Entrada]]
- $\Gamma$: [[Alfabeto]] finito de la pila
- $\delta$: [[Función de transición]] definida por $\delta: K \times \left( \Sigma \cup \set{ \lambda } \right) \times \Gamma \to P \left( K \times \Gamma^* \right)$
- $q_0$: [[Lógica y Estructuras Discretas/Estado|Estado]] inicial del [[Autómata]], $q_0 \in K$
- $z_0$: Configuración inicial de la [[Pila]], $z_0 \in \Gamma$
- $F$: [[Conjunto]] de [[Lógica y Estructuras Discretas/Estado|Estados]] aceptados o finales, $F \subseteq K$

> [!tip]
> En cada transición solo es posible consultar el tope de la [[Pila]], y en cada transición, dicho elemento **siempre** se consume. Sin embargo, al realizar la transición, pueden agregarse a la [[Pila]] tantos elementos como se desee, o ninguno.

---

La [[Configuración instantánea]] del [[Autómata de pila]] está definida en:

$$
K \times \Sigma^* \times \Gamma^*
$$

Representada por $\left( q, \alpha, \tau \right)$ , donde $q$ es el [[Lógica y Estructuras Discretas/Estado|Estado]] actual, $\alpha$ es la [[Lógica y Estructuras Discretas/Cadena|Cadena]] que aún falta consumir, y $\tau$ es el contenido de la [[Pila]].
