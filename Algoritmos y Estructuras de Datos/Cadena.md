---
created: 2024-07-02 21:14:48
modified: 2024-07-03 00:32:42
title: Cadena
---

# Cadena

Una cadena es una [[Lista]] de carácteres.

Podemos obtener el carácter $n \in \mathbb{Z}$ de una cadena `abc` de la siguiente forma. Si $n$ es negativo, comienza a contar desde el lado derecho de la cadena.

```python
abc[n]
```

> [! important]
> El índice de los elementos de una cadena comienza en $0$.

También podemos tomar una parte de la cadena, desde el índice $n$ hasta $m$, con un paso o *step* de $t$. Este intervalo es de la forma $[n, m)$.

```python
abc[n:m:t]
```

Si $n$ no está especificado, es $0$, si $m$ no está especificado, toma el último carácter de la cadena, y si $t$ no está especificado, es $1$.
