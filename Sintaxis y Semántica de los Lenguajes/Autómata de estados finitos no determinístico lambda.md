---
aliases:
  - Autómatas de estados finitos no determinísticos lambda
  - AEFND-λ
created: 2025-03-06 14:40:22
modified: 2025-06-10 17:11:18
title: Autómata de estados finitos no determinístico lambda
---

# Autómata de estados finitos no determinístico lambda

Es un [[Autómata de estados finitos no determinístico|AEFND]], pero con una modificación a la [[Análisis Matemático I/Función|Función]] de [[Lógica y Estructuras Discretas/Estado|Estado]] siguiente $\delta$.

$$
\delta: K \times \Sigma \cup \set{ \lambda } \to P \left( K \right)
$$

> [!tip]
> Es decir, existen transiciones que nos permiten pasar de un [[Lógica y Estructuras Discretas/Estado|Estado]] a otro, sin consumir nada de la [[Lógica y Estructuras Discretas/Cadena|Cadena]] (ya que como $\lambda$ es la [[Cadena vacía]], consumir $\lambda$ es lo mismo que no consumir nada).
