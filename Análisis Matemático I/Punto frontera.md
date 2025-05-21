---
aliases:
  - Puntos frontera
created: 2024-08-20 17:16:28
modified: 2025-05-21 13:44:48
title: Punto frontera
---

# Punto frontera

Dado un [[Conjunto]] $A$, un punto $p$ es un [[Punto frontera]] si cualquier entorno del mismo contiene:

- Puntos que pertenecen a $A$ ($x \in A$)
- Puntos que no pertenecen a $A$ ($x \notin A \Leftrightarrow x \in \overline{A}$)

Por ser uno de los [[Punto crítico|Puntos críticos]], es un candidato a ser [[Extremo relativo|Extremo local]]. Si esto se cumple, se dice que el punto es un [[Extremo vinculado]].

---

Dada una [[Función real de variable vectorial]] $z = f(x, y)$, la frontera representa una curva sobre el [[Plano]] $xy$, que puede ser parametrizada para obtener una [[Función real de variable real]] $\phi(t)$, que nos permite obtener la [[Imagen]] de la [[Análisis Matemático I/Función|Función]] únicamente en los [[Punto frontera|Puntos frontera]].

$$
f(x, y) = f \left( x(t), y(t) \right) = \phi(t)
$$

![[frontera-1.jpg]]

Si la frontera estuviera determinada por más de una curva, es necesario parametrizar a todas ellas.

$$
\left[ f(x, y) = f \left( x_1 (t), y_1 (t) \right) = \phi_1 (t) \right]
\land
\left[ f(x, y) = f \left( x_2 (t), y_2 (t) \right) = \phi_2 (t) \right]
$$

![[frontera-2.jpg]]

> [!important]
> Los puntos $A$ y $B$ definidos en la imagen, se suelen llamar ==fronteras de frontera==, y deben ser estudiados como [[Punto singular|Puntos singulares]], pues en estos puntos la [[Análisis Matemático I/Función|Función]] no es [[Diferencial|Diferenciable]].

Al tener [[Función real de variable real|Funciones reales de variable real]], es posible aplicar simplemente el [[Criterio de la primera derivada]], y el [[Criterio de la segunda derivada]] para determinar la existencia de [[Extremo relativo|Extremos locales]] en estos puntos.

> [!tip]
> Al realizar el análisis de fronteras definidas por múltiples curvas, es importante verificar que los [[Punto crítico|Puntos críticos]] encontrados **estén efectivamente en las restricciones definidas**.
