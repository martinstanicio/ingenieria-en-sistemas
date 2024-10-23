---
created: 2024-10-22 22:37:10
modified: 2024-10-22 22:41:35
title: Función strip
---

# Función strip

En [[Python]], la [[Algoritmos y Estructuras de Datos/Función|Función]] `strip` devuelve la cadena dada, luego de eliminar los carácteres en blanco (espacios, tabulaciones y saltos de línea).

```python
nueva_cadeba = cadena.strip()
```

La [[Algoritmos y Estructuras de Datos/Función|Función]] `lstrip` solo elimina los carácteres al comienzo de la cadena, `rstrip` los carácteres al final, y `strip` elimina los carácteres de ambos lados.

```python
cadena = " hola\n"

cadena.lstrip() # "hola\n"
cadena.rstrip() # " hola"
cadena.strip() # "hola"
```
