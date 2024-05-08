---
created: 2024-04-14 16:43:12
modified: 2024-05-08 01:33:29
title: Teorema de Rouche Frobeniuos
---

# Teorema de Rouche Frobeniuos

> Un [[Sistema de ecuaciones lineales (SEL)]] de $m \times n$ es [[Sistema compatible (SC)|compatible]] si y solo si el [[Rango de una matriz|rango]] de la [[Matriz#Matriz de coeficientes|matriz de coeficientes]] del sistema es igual al rango de la [[Matriz#Matriz ampliada|matriz ampliada]] con los términos independientes.

Por lo tanto, sea $r_A$ el rango de la matriz de coeficientes $A$, $r_{Ab}$ el rango de la matriz ampliada $Ab$, y $n$ el número de incógnitas, entonces:

1. Si $r_A = r_{Ab}$, es un [[Sistema compatible (SC)]]
	1. Si $r_A = r_{Ab} = n$, es un [[Sistema compatible (SC)#Sistema compatible determinado (SCD)|sistema compatible determinado (SCD)]]
	2. Si $r_A = r_{Ab} < n$, es un [[Sistema compatible (SC)#Sistema compatible indeterminado (SCI)|sistema compatible indeterminado (SCI)]]
2. Si $r_A \neq r_{Ab}$, es un [[Sistema incompatible (SI)]]
