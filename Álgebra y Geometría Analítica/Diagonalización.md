---
created: 2024-11-09 14:41:18
modified: 2024-11-09 14:55:37
title: Diagonalización
---

# Diagonalización

Una [[Matriz]] $A \in k^{n \times n}$ es **diagonalizable** si es [[Matrices semejantes|Semejante]] a una [[Matriz diagonal]] $D$.

$$
A \sim D
$$

La **diagonal principal** de la [[Matriz]] $D$ serán los [[Autovalor|Autovalores]] de $A$ (que también son [[Autovalor|Autovalores]] de $D$).

> [!important]
> $A$ es diagonalizable si y solo si tiene $n$ [[Autovector|Autovectores]] que sean [[Conjunto linealmente independiente|Linealmente independientes]], y en ese caso:
>
> $$
> D = C^{-1} A C
> $$
>
> Donde los elementos de la diagonal principal de $D$ son los $n$ [[Autovalor|Autovalores]] de $A$, no necesariamente distintos, y $C$ es una [[Matriz]] cuyas columnas son los [[Autovector|Autovectores]] de $A$.

> [!tip]
> Si $A \in k ^{n \times n}$ tiene $n$ [[Autovalor|Autovalores]] ==distintos==, entonces $A$ es diagonalizable.

---

Dada una [[Transformación lineal]] $T: V \to V$, donde $\dim(V) = n$ ([[Dimensión]] finita), para cada [[Base]] de $V$, existe una [[Matriz]] que representa a $T$.

Sean $B$ y $C$ [[Base|Bases]] de $V$ y sean $M_B$ y $M_C$ la representación matricial de $T$ en las [[Base|Bases]] $B$ y $C$ respectivamente, entonces $M_B \sim M_C$.

Particularmente, $T$ es **diagonalizable** en cualquiera de sus representaciones, si existe una [[Base]] $B$ tal que $M_B$ sea diagonal.
