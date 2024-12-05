---
created: 2024-12-05 18:53:39
modified: 2024-12-05 19:10:14
title: Algoritmo de Fleury
---

# Algoritmo de Fleury

Este [[Algoritmos|Algoritmo]] nos permite encontrar, ==si existen==, el [[Camino de Euler|Caminos de Euler]] o [[Circuito de Euler|Circuitos de Euler]] de un [[Grafo]]  $G = (V, A, \delta)$. Sea $VS$ la sucesión de vértices recorridos, y $AS$ la sucesión de aristas recorridas.

1. Selecciones un vértice $v$ de [[Valencia]] impar; si no lo hay, cualquiera. Agregamos la arista $\lambda$ a $AS$ y el vértice $v$ a $VS$, es decir, $AS = \lambda$ y $VS = v$.
2. Si no quedan aristas que inciden en el vértice $v$, finalizar.
3. Si queda exactamente una arista por usar en el vértice $v$, por ejemplo $e$, quitar $e$ de $A$, borrar $v$ de $V$ e ir al punto 5.
4. Si queda más de una arista por usar en $v$, elegir una, por ejemplo $e$, tal que su eliminación no deje al **subgrafo no conexo**. Quitar $e$ de $A$ e ir al punto 5.
5. Si $e$ incide en los vértices $v$ y $w$, añadir $w$ a $VS$, añadir la arista utilizada $a$ a $AS$, hacer $v = w$ e ir al punto 2.
