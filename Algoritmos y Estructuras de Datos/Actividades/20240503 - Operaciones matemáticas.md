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

```python
# AyED
# Autor: Martín Stanicio
# Fecha: 03/05/2024

numero1 = 0
numero2 = 0
operacion = ""

try:
    numero1 = int(input("Ingrese el número 1 (entero): "))
    numero2 = int(input("Ingrese el número 2 (entero): "))
    operacion = input("Ingrese la operación que desea realizar (S, R, C o M): ")
except ValueError:
    print("\nPor favor ingrese números válidos")

if operacion == "S":
    print(numero1 + numero2)
elif operacion == "R":
    print(numero1 - numero2)
elif operacion == "C":
    if numero2 == 0:
        print("No se puede dividir por cero")
    else:
        print(numero1 / numero2)
elif operacion == "M":
    print(numero1 * numero2)
else:
    print("Por favor ingrese una operación válida")
```
