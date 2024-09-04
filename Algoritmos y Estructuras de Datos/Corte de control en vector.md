---
aliases:
  - Control por ruptura
created: 2024-09-03 21:06:59
modified: 2024-09-03 21:33:43
title: Corte de control en vector
---

# Corte de control en vector

Determinar la cantidad de veces que se repite un [[Dato]] en un [[Array|Vector]].

```python
vector = [5, 10, 5, 15, 5]
```

Para esto realizamos un [[Ordenamiento]] del [[Array|Vector]].

```python
vector = [5, 5, 5, 10, 15]
```

Luego, utilizando un [[Estructura de repetición|Bucle]], aumentamos un [[Contador]] cada vez que se repite la [[Variables|Variable]] de **control**. Una vez que ya no se repite, estamos ante un **corte de control**, y debemos mostrar la cantidad de veces $z$ que se repite un número $x$.
