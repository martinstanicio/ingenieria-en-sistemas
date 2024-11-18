---
created: 2024-11-18 11:08:18
modified: 2024-11-18 11:22:32
title: Homomorfismo
---

# Homomorfismo

Sean $(G, *)$ y $(H, \#)$ dos [[Grupo|Grupos]]. Sea la [[Análisis Matemático I/Función|Función]] $F: G \to H$. Si se cumple que:

$$
\forall a \in G \forall b \in G: F(a * b) = F(a) \# F(b)
$$

Entonces $F$ es un [[Homomorfismo]].

> [!note]
> Particularmente si $F$ es **biyectiva**, $F$ se llama ==isomorfismo==.
> 
> Es decir, a cada elemento de $G$ le corresponde una [[Imagen]] distinta, y todos los elementos de $H$ son [[Imagen]] de algún elemento de $G$.

Todo [[Homomorfismo]] también cumple una serie de propiedades.

## Propiedades

La [[Imagen]] del [[Elemento neutro]] de $G$ es el [[Elemento neutro]] de $H$.

$$
F \left( e_G \right) = e_H
$$

La [[Imagen]] del [[Elemento simétrico|Elemento inverso]] de $x$ es el [[Elemento simétrico|Elemento inverso]] de la [[Imagen]] de $x$.

$$
F \left( x^{-1} \right) = \left[ F(x) \right]^{-1}
$$

La [[Imagen]] de la $n$ potencia de $a$ es la $n$ potencia de la [[Imagen]] de $a$.

$$
F \left( a^n \right) = \left[ F(a) \right]^n, n \in \mathbb{N}
$$

Si $S$ es [[Subgrupo]] de $G$, entonces $F(S)$ es [[Subgrupo]] de $H$.
