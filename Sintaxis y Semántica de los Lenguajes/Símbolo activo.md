---
aliases:
  - Símbolos activos
created: 2025-06-15 20:48:21
modified: 2025-06-15 20:51:44
title: Símbolo activo
---

# Símbolo activo

Sea una [[Gramática]] $G = \left< N, T, P, S \right>$, un símbolo $A \in N$ es activo si y solo si:

$$
\exists \sigma \in T^*: A \to^* \sigma
$$

> [!tip]
> Un símbolo es [[Símbolo activo|Activo]] si es posible derivarlo en una [[Lógica y Estructuras Discretas/Cadena|Cadena]] de terminales $\sigma \in T^*$ en cualquier cantidad de pasos.
