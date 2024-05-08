---
created: 2024-05-03 17:15:39
modified: 2024-05-08 01:33:30
title: Sentencia fantasma
---

# Sentencia fantasma

Una [[Bifurcaciones|bifurcación]] donde el bloque de código que se debe ejecutar si la condición se cumple está vacío.

En [[Python]] esto generará un [[Errores|error]] de tipo `IndentError`, para evitar esto podemos utilizar `next`:

```python
if x > 1:
    next
else:
    print("abc")
```
