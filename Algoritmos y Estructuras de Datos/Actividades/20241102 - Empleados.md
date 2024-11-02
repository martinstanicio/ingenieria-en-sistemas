---
created: 2024-11-02 18:06:32
modified: 2024-11-02 18:23:55
title: 20241102 - Empleados
---

# 20241102 - Empleados

Crea un programa que lea un [[Archivo]] `empleados.dat`, donde cada registro contiene:

- Legajo de empleado (entero)
- Nombre (cadena)
- Edad (entero)
- Departamento (cadena): "a", "b", o "c"
- Salario (real)

El programa debe permitir al usuario ingresar un departamento y mostrar:

- La cantidad de empleados en ese departamento
- El promedio de salario de los empleados en ese departamento
- El legajo, nombre y salario del empleado más joven en ese departamento (único)

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`
	`"]
    
    fin([fin])
    
	comienzo --> variables --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-empleados/main.py"
```
