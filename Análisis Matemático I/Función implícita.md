---
aliases:
  - Funciones implícitas
  - Forma implícita
created: 2024-08-19 18:17:29
modified: 2025-05-20 19:08:04
title: Función implícita
---

# Función implícita

Una ecuación de $n + 1$ incógnitas, de la forma:

$$
F \left( x_1, x_2, \dots, y \right) = 0
$$

En algunos casos, la ecuación define a una de las incógnitas como una [[Función implícita]] de las restantes, ==sin importar si la variable puede o no ser despejada== para llevarla a una forma explícita.

---

Dada una [[Función implícita]] $F(x_1, \dots, x_n, y) = 0$ con un [[Dominio]] $D$, podemos decir que se define a $y$ como una [[Función implícita]] de las demás variables si se cumplen las siguientes condiciones.

1. Existe un [[Subconjunto]] $S \subseteq D$ de puntos $(x_1, \dots, x_n, y)$ que satisfacen la ecuación.
2. La [[Análisis Matemático I/Función|Función]] $w = F(x_1, \dots, x_n, y)$ es [[Diferencial|Diferenciable]] en $S$ o un [[Subconjunto]] de $S$.
3. La [[Derivada parcial]] $\partial F / \partial y \neq 0$ en los puntos considerados o en un [[Subconjunto]].

Esto es útil ya que nos ==permite calcular la [[Derivada parcial]] de $y$== respecto de cualquiera de las variables independientes.

$$
\frac{\partial y}{\partial x_i} =
- \frac{\partial F / \partial x_i}{\partial F / \partial y}
$$

> [!important]
> El [[Vector gradiente]] en un punto es [[Vectores ortogonales|Ortogonal]] a la gráfica de la [[Función implícita]] en ese punto.
> 
> Esto es muy útil para hallar la [[Recta normal]], o el [[Recta normal|Vector normal]] a una superficie.
