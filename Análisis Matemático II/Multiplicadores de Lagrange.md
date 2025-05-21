---
aliases:
  - Método de los multiplicadores de Lagrange
created: 2025-05-21 14:06:26
modified: 2025-05-21 15:29:01
title: Multiplicadores de Lagrange
---

# Multiplicadores de Lagrange

Una herramienta para la determinación de [[Punto crítico|Puntos críticos]] de una [[Análisis Matemático I/Función|Función]] $f \left( \vec{p} \right)$, sobre la que se impone una restricción, dada en forma de una ecuación [[Función implícita|Implícita]] $G \left( \vec{p} \right) = 0$.

> [!note]
> La restricción también puede ser **natural**, impuesta por el mismo [[Dominio]] de la [[Análisis Matemático I/Función|Función]].

En el caso de [[Función real de variable vectorial|Funciones reales de variable vectorial]] de dos componentes (3 dimensiones), se puede ver que los [[Punto crítico|Puntos críticos]] encontrados, son aquellos que son [[Recta tangente|Tangentes]] a la [[Curvas de nivel|Línea de contorno]].

![[multiplicadores-de-lagrange-1.jpg]]

- El [[Vector gradiente]] $\nabla f(x, y)$ es siempre perpendicular a la [[Curvas de nivel|Curva de nivel]]
- El [[Vector gradiente]] $\nabla G(x, y)$ es perpendicular a la gráfica de la [[Función implícita]] $G(x, y) = 0$

Entonces, los [[Punto crítico|Puntos críticos]] encontrados son aquellos pertenecientes a la restricción $G \left( \vec{p} \right) = 0$, donde $f \left( \vec{p} \right)$ y $\nabla G \left( \vec{p} \right)$ ==son colineales==.

$$
\left\{
    \begin{array}{l}
        \nabla f \left( \vec{p} \right) = \lambda \nabla G \left( \vec{p} \right) \\
        G \left( \vec{p} \right) = 0 \\
    \end{array}
\right.
$$

> [!warning]
> Los [[Multiplicadores de Lagrange]] solo permiten determinar la existencia de ==posibles== [[Extremo vinculado|Extremos condicionados]] ([[Punto frontera|Puntos frontera]]), pero no de posibles [[Extremo libre|Extremos libres]] ([[Punto estacionario|Puntos estacionarios]]).
> 
> ![[multiplicadores-de-lagrange-2.jpg]]
> 
> Este es un ejemplo de [[Punto crítico]] que no es [[Extremo relativo|Extremo]].
