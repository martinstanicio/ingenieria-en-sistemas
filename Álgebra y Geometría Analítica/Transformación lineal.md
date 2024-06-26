---
aliases:
  - Mapeo lineal
  - Linear mapping
  - Aplicación lineal
  - Operador lineal
created: 2024-06-10 19:20:01
modified: 2024-06-26 01:26:15
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

## Isomorfismo

Para que una [[Transformación lineal]] $T: V \rightarrow W$ sea un [[Álgebra y Geometría Analítica/Isomorfismo|Isomorfismo]], debe ser biyectiva.

Para que sea inyectiva, su [[Nulidad]] debe ser $0$.

$$
\nu_T = dim(Ker(T)) = 0
$$

Para que sea sobreyectiva, la [[Dimensión]] de su [[Imagen]] debe ser igual a la [[Dimensión]] del espacio de llegada $W$.

$$
dim(Imagen(T)) = dim(W)
$$
