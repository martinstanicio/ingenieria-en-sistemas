---
aliases:
  - Símbolos anulables
created: 2025-06-15 20:54:03
modified: 2025-06-15 21:20:11
title: Símbolo anulable
---

# Símbolo anulable

Sea una [[Gramática]] $G = \left< N, T, P, S \right>$, un símbolo $A \in N$ es anulable si $A \to^* \lambda$, y se nota como $\text{Anul} \left( A \right)$.

> [!tip]
> Un símbolo es [[Símbolo anulable|Anulable]] si es posible derivarlo en la [[Cadena vacía]] $\lambda$ en cualquier cantidad de pasos.

## Cálculo del conjunto de símbolos anulables de una gramática

Este [[Algoritmos|Algoritmo]] nos permite obtener el [[Conjunto]] de [[Símbolo anulable|Símbolos anulables]] $A$ de una [[Gramática]] $G$.

1. Hacer $A = \emptyset$
2. Para cada producción $B \to \beta$:
	1. Si $\beta = \lambda$:
		1. Agregar $B$ a $A$
3. Repetir hasta que no haya cambios en $A$:
	1. Para cada producción $B \to \beta$:
		1. Si $\beta \in A^*$:
			1. Agregar $B$ a $A$
