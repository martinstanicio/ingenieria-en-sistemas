---
created: 2024-10-01 21:25:00
modified: 2024-10-01 21:40:23
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
	otro = cadena
	nuevo_elemento = entero
	dato = cadena`"]
        
	fin([fin])
    
	comienzo --> declaracion --> fin
```
