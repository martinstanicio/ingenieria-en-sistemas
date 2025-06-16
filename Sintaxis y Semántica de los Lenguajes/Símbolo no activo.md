---
aliases:
  - Símbolos no activos
  - Símbolo inactivo
  - Símbolos inactivos
created: 2025-06-15 20:53:23
modified: 2025-06-15 21:17:30
title: Símbolo no activo
---

# Símbolo no activo

Un símbolo de una [[Gramática]] es [[Símbolo no activo|No activo]] si no es un [[Símbolo activo]].

## Eliminación de símbolos no activos

Este [[Algoritmos|Algoritmo]] nos permite obtener el [[Conjunto]] de [[Símbolo activo|Símbolos activos]] $A$ de una [[Gramática]] $G$. Luego, los símbolos del [[Conjunto]] $\left( N - A \right)$ pueden ser eliminados, junto con sus producciones.

1. Hacer $A = \emptyset$
2. Para cada producción $B \to \beta$:
	1. Si $\beta \in T^*$:
		1. Agregar $B$ a $A$
3. Hacer $\text{fin} = 0$ (falso)
4. Mientras $\text{fin}$ sea falso:
	1. Hacer $\text{fin} = 1$
	2. Para cada producción $B \to \beta$:
		1. Si $\beta \in \left( A \cup T \right)^*$:
			1. Agregar $B$ a $A$
			2. Hacer $\text{fin} = 0$
