---
created: 2024-04-06 20:17:07
modified: 2024-05-08 01:33:30
title: Espacio vectorial
---

# Espacio vectorial

Un espacio vectorial $V$ es un [[Conjunto]] **vectores**, que posee dos operaciones: **suma** y **multiplicación** por un [[Escalar]], y que satisfacen los diez axiomas enumerados a continuación. Se representa de la siguiente forma.

$$(V, +, k, \cdot)$$

Donde:

1. $V$ es el nombre del mismo
2. $+$ es la operación de suma
3. $k$ es el [[Cuerpo]] que representa a los escalares
4. $\cdot$ es la operación de multiplicación

Por ejemplo:

- El conjunto de los complejos con los reales como escalares: $(\mathbb{C},+,\mathbb{R},\cdot)$
- El conjunto de los polinomios de grado menor o igual a 2 con los reales como escalares: $(P_2,+,\mathbb{R},\cdot)$

## Axiomas de un espacio vectorial

1. **Cerradura bajo la suma:** si $x \in V$ y $y \in V$, entonces $x+y \in V$
2. **Ley asociativa de la suma de vectores:** para todo $x$, $y$ y $z$ en $V$, $(x+y)+z=x+(y+z)$
3. **Vector cero o idéntico aditivo:** existe un vector $0 \in V$ tal que para todo $x \in V$, $x+0=0+x=0$
4. **Inverso aditivo:** si $x \in V$, existe un vector $-x \in V$ tal que $x+(-x)=0$
5. **Ley conmutativa de la suma de vectores:** si $x$ y $y$ están en $V$, entonces $x+y=y+x$
6. **Cerradura bajo la multiplicación por un escalar:** si $x \in V$ y $\alpha$ es un escalar, entonces $\alpha x \in V$
7. **Primera ley distributiva:** si $x$ y $y$ están en $V$ y $\alpha$ es un escalar, entonces $\alpha (x+y)=\alpha x + \alpha y$
8. **Segunda ley distributiva:** si $x \in V$ y $\alpha$ y $\beta$ son escalares, entonces $(\alpha + \beta)x=\alpha x + \beta x$
9. **Ley asociativa de la multiplicación por escalares:** si $x \in V$ y $\alpha$ y $\beta$ son escalares, entonces $\alpha(\beta x)=(\alpha \beta)x$
10. Para cada vector $x \in V$, $1x=x$

## Cantidad de elementos

Un espacio vectorial **siempre** tiene o un solo elemento, por lo que es un [[Espacio vectorial trivial]], o tiene elementos infinitos.
