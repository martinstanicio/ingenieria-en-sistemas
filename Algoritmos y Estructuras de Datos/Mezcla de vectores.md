---
aliases:
  - Vector merge
created: 2024-10-08 21:11:00
modified: 2024-10-09 00:43:40
title: Mezcla de vectores
---

# Mezcla de vectores

Dados 2 [[Vector|Vectores]] **ordenados** obtener un tercer [[Vector]] [[Ordenamiento|Ordenado]].

## Diagrama de flujo

En [[Diagrama de flujo]], se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo([comienzo])
    
    declarar["`a[4] = entero
    b[6] = entero
    m[10] = entero
    xa = entero
    xb = entero
    z = entero
    i = entero`"]
    inicializar["`xa = 0
    xb = 0
    z = 0`"]
    
    vector_a["Carga y ordenamiento de vector a"]
    vector_b["Carga y ordenamiento de vector a"]
    
    while{"xa < largo(a) y xb < largo(b)"}
    if{"a[xa] < b[xb]"}
    if_yes["`m[z] = a[xa]
    xa = xa + 1`"]
    if_no["`m[z] = b[xb]
    xb = xb + 1`"]
    z["z = z + 1"]
    
    for1{{"i, xa, largo(a)"}}
    for_a["`m[z] = a[i]
    z = z + 1`"]
    for2{{"i, xb, largo(b)"}}
    for_b["`m[z] = b[i]
    z = z + 1`"]
    
    for3{{"i, 0, largo(m)"}}
    mostrar{{"m[i]"}}
    
	fin([fin])
	
	a[" "]
	b[" "]
	c[" "]
	d[" "]
	e[" "]
	f[" "]
    
	comienzo --> declarar --> inicializar --> vector_a --> vector_b --> a --> while -- "Sí" --> if
	if -- "Sí" --> if_yes --> b
	if -- "No" --> if_no --> b
	b --> z --> c --> a
	while -- "No" ---> for1 --> for_a --> d
	for1 --> d --> for2 --> for_b --> e
	for2 --> e --> for3 --> mostrar --> f
	for3 --> f --> fin
```

## Python

En [[Python]], se realiza de la siguiente forma.

```Python
from random import randint

a = [0] * 4
b = [0] * 6
m = [0] * 10

xa = 0
xb = 0
z = 0

for i in range(0, len(a)):
    a[i] = randint(0, 100)

for i in range(0, len(b)):
    b[i] = randint(0, 100)

a.sort()
b.sort()

while xa < len(a) and xb < len(b):
    if a[xa] < b[xb]:
        m[z] = a[xa]
        xa += 1
    else:
        m[z] = b[xb]
        xb += 1
    
    z += 1

for i in range(xa, len(a)):
    m[z] = a[i]
    z += 1

for i in range(xb, len(b)):
    m[z] = b[i]
    z += 1

for i in range(0, len(m)):
    print(m[i])
```
