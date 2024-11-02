---
created: 2024-10-22 22:52:45
modified: 2024-11-02 18:37:00
title: 20241022 - Deportistas
---

# 20241022 - Deportistas

El usuario ingresa el deporte cuyas estadísticas queremos analizar. Mostrar:

- Cantidad de deportistas que practican ese deporte
- Promedio de altura de las personas que practican ese deporte
- Mayor edad de la persona que practica ese deporte

Cada registro del archivo `deportistas.txt` contiene los siguientes campos:

- Número de socio (entero)
- Apellido (cadena)
- Altura (real)
- Edad (entero)
- Deporte (cadena): "f", "b" o "v"

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
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241022-deportistas/main.py"
```

```embed-shell
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241022-deportistas/deportistas.txt"
```
