---
created: 2024-06-04 00:19:54
modified: 2024-06-04 12:33:16
title: Números aleatorios
---

# Números aleatorios

Para generar **números aleatorios** en [[Python]], debemos ==importar== la [[Biblioteca]] `random`.

```python
import random
```

## Números reales

Para generar números reales, utilizamos la [[Algoritmos y Estructuras de Datos/Función|Función]] `random`.

Si no utilizamos ningún parámetro, obtendremos un valor entre $0$ (cerrado) y $1$ (abierto), es decir $[0, 1)$.

```python
import random

x = random.random() # [0, 1)
```

Si pasamos parámetros, podemos especificar el intervalo del cual queremos obtener un número aleatorio:

1. Valor mínimo (cerrado, incluido en el intervalo)
2. Valor máximo (abierto, **no** incluido en el intervalo)

```python
import random

y = random.random(-5, 10) # [-5, 10)
```

## Números enteros

Para generar números enteros, utilizamos la [[Algoritmos y Estructuras de Datos/Función|Función]] `randint`.

Esta función requiere dos parámetros, que nos permiten especificar el ==intervalo cerrado== del cual queremos obtener un número aleatorio:

1. Valor mínimo
2. Valor máximo

```python
import random

z = random.randint(10, 100) # [10, 100]
```
