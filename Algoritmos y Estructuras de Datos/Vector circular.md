---
created: 2024-10-01 21:25:00
modified: 2024-10-01 21:58:52
title: Vector circular
---

# Vector circular

Permite reutilizar los elementos de un [[Vector]], de forma que luego de haber utilizado el último elemento, podamos volver a utilizar el primer elemento, y todos los que le siguen.

Para obtener el elemento con el que queremos trabajar, debemos realizar la siguiente operación

```
elemento = (i + 1) RESTO n
```

Donde `i` es el número de elemento, y `n` es la cantidad de elementos en el [[Vector]].

## Diagrama de flujo

El [[Diagrama de flujo]] se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declaracion["`vector[6] = cadena
	continuar = cadena
	nuevo_elemento = entero
	dato = cadena
	i = entero`"]
	inicializar["`continuar = 'si'
	nuevo_elemento = -1`"]
	
	while{"continuar <> 'no'"}
	dato[/dato/]
	nuevo_elemento["nuevo_elemento = (nuevo_elemento + 1) RESTO 6"]
	vector["vector[nuevo_elemento] = dato"]
	continuar[/continuar/]
	
	for{{"i, 0, 6"}}
	mostrar{{"vector[i]"}}
    
	fin([fin])
	
	a[" "]
	b[" "]
	c[" "]
    
	comienzo --> declaracion --> inicializar --> a --> while -- "Sí" --> dato --> nuevo_elemento --> vector --> continuar --> a
	while -- "No" --> for --> mostrar --> b --> fin
	for --> b
```

## Python

En [[Python]] se realiza de la siguiente forma.

```python
n = 6
vector = [0] * n
continuar = "si"
nuevo_elemento = -1

while continuar != "no":
    dato = input("Dato: ")
    
    nuevo_elemento = (nuevo_elemento + 1) % n
    vector[nuevo_elemento] = dato
    
    continuar = input("Desea continuar? ")

for i in range(0, n):
    print(vector[i])
```
