# Sentencia fantasma

Una [[Bifurcaciones|bifurcación]] donde el bloque de código que se debe ejecutar si la condición se cumple está vacío.

En [[Python]] esto generará un [[Errores|error]] de tipo `IndentError`, para evitar esto podemos utilizar `next`:

```python
if x > 1:
    next
else:
    print("abc")
```
