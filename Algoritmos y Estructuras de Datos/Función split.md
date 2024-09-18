---
created: 2024-08-20 22:48:12
modified: 2024-08-20 22:52:38
title: Función split
---

# Función split

En [[Python]], la [[Algoritmos y Estructuras de Datos/Función|Función]] `split` nos permite crear una [[Vector|Lista]] a partir de una [[Variables|Variable]] de tipo **cadena**, especificando el **separador** utilizado.

```python
lista = variable.split(separador)
```

Por ejemplo, con una [[Vector|Lista]] de apellidos.

```python
apellidos = "Stanicio;Perez;Rey"
lista = apellidos.split(";") # ["Stanicio", "Perez", "Rey"]
```
