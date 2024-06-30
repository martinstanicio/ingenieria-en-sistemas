---
aliases:
  - Mapeo lineal
  - Linear mapping
  - Aplicación lineal
  - Operador lineal
  - TL
created: 2024-06-10 19:20:01
modified: 2024-06-29 09:41:22
title: Transformación lineal
---

# Transformación lineal

Una [[Análisis Matemático I/Función|Función]] que toma un vector de un [[Espacio vectorial]] y lo transforma en otro vector de otro [[Espacio vectorial]].

> [!tip]
> Toda [[Transformación lineal]] es [[Análisis Matemático I/Función|Función]], pero no toda [[Análisis Matemático I/Función|Función]] es [[Transformación lineal]].

## Propiedades

### Preservan la suma de vectores

Si $T$ es una [[Transformación lineal]] y $u$ y $v$ son vectores en el dominio de $T$, entonces $T(u + v) = T(u) + T(v)$.

### Preservan la multiplicación escalar

Si $T$ es una [[Transformación lineal]] y $c$ es un escalar, entonces $T(c \cdot u) = c \cdot T(u)$.

### Llevan el [[Elemento neutro|Vector nulo]] al [[Elemento neutro|Vector nulo]]

$T(0) = 0$ para toda [[Transformación lineal]] $T$.

## Tipos de [[Transformación lineal]]

## Monomorfismo

Una [[Transformación lineal|TL]] $T: V \rightarrow W$ es **monomorfismo** si es ==inyectiva==, y viceversa. Para esto, su [[Nulidad]] debe ser $0$.

$$
\nu_T = \dim(\ker(T)) = 0
$$

Si $\dim(V) > \dim(W)$, es decir, si la [[Dimensión]] del espacio de salida $V$ es mayor que la del espacio de llegada $W$, ==no es monomorfismo==.

## Epimorfismo

Una [[Transformación lineal|TL]] $T: V \rightarrow W$ es **epimorfismo** si es ==sobreyectiva==, y viceversa. Para esto, la [[Dimensión]] de su espacio de salida $V$ debe ser mayor o igual a su espacio de llegada $W$.

$$
\dim(V) \geq \dim(W)
$$

## Isomorfismo

Una [[Transformación lineal|TL]] es **isomorfismo** si es ==biyectiva==, y viceversa. Para esto, debe ser [[Transformación lineal#Monomorfismo|monomorfismo]] y [[Transformación lineal#Epimorfismo|epimorfismo]]. Es decir, debe cumplirse lo siguiente.

$$
\dim(V) = \dim(W)
$$

## Endomorfismo

Una [[Transformación lineal|TL]] $T: V \rightarrow W$ es **endomorfismo** si su espacio de salida $V$ y su espacio de llegada $W$ son iguales.

$$
V = W
$$

## Automorfismo

Una [[Transformación lineal|TL]] es **automorfismo** si es [[Transformación lineal#Isomorfismo|isomorfismo]] y un [[Transformación lineal#Endomorfismo|endomorfismo]].
