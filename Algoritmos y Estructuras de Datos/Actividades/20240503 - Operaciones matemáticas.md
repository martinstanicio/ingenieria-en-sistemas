---
created: 2024-05-03 18:15:46
modified: 2024-05-08 01:33:30
title: 20240503 - Operaciones matemáticas
---

# 20240503 - Operaciones matemáticas

Se ingresan dos números enteros y una letra que representa la operación matemática a resolver ("S" para suma, "R" para resta, "C" para cociente, y "M" para multiplicar). Realizar la operación por la letra y mostrar el resultado.

## Pseudocódigo

```
comienzo

declarar numero1 = entero, numero2 = entero, operacion = cadena

leer(numero1)
leer(numero2)
leer(operacion)

segun_sea operacion hacer:
    "S": mostrar(numero1 + numero2)
    "R": mostrar(numero1 - numero2)
    "C":
        si numero2 == 0 entonces:
            mostrar("No se puede dividir por cero")
        sino:
            mostrar(numero1 / numero2)
    "M": mostrar(numero1 * numero2)
    sino:
    print("Por favor ingrese una operación válida")
fin_segun_sea

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`numero1 = entero
	numero2 = entero
	operacion = cadena`"]
    
	numero1[/numero1/]
    numero2[/numero2/]
    operacion[/operacion/]
    
    condicion{operacion}
    
    S{{"numero1 + numero2"}}
    
    R{{"numero1 - numero2"}}
    
    CCondicion{"numero2 == 0"}
    CSi{{"No se puede dividir por cero"}}
    CNo{{"numero1 / numero2"}}
    
	M{{"numero1 * numero2"}}
    
	fin([fin])
    
	comienzo --> variables --> numero1 --> numero2 --> operacion --> condicion
	condicion -- "S" --> S
	condicion -- "R" --> R
	condicion -- "C" --> CCondicion
	CCondicion -- Sí --> CSi
	CCondicion -- No --> CNo
	condicion -- "M" --> M
	S --> fin
	R --> fin
	CSi --> fin
	CNo --> fin
	M --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240503-operaciones-matematicas.py"
```
