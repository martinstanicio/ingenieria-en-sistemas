---
created: 2024-05-17T21:15:00
modified: 2024-05-17 18:27:18
title: 20240517 - Producciones
---

# 20240517 - Producciones

Se ingresan los datos de producciones:

- Número de horno ($1$, $2$ o $3$)
- Toneladas producidas

Mostrar total de toneladas producidas por cada horno.

La última producción tiene como número de horno $-1$ y no debe procesarse.

Usar un [[Ciclo mientras]] controlado por [[Bandera]].

## Pseudocódigo

```
comienzo

declarar numero_horno = entero, toneladas_producidas = real, bandera = logica, toneladas_horno_1 = real, toneladas_horno_2 = real, toneladas_horno_3 = real

numero_horno = 0
bandera = verdadero
toneladas_horno_1 = 0
toneladas_horno_2 = 0
toneladas_horno_3 = 0

mientras bandera entonces
    leer(toneladas_producidas)
    leer(numero_horno)
    
    segun_sea numero_horno entonces
        1: toneladas_horno_1 = toneladas_horno_1 + toneladas_producidas
        2: toneladas_horno_2 = toneladas_horno_2 + toneladas_producidas
        3: toneladas_horno_3 = toneladas_horno_3 + toneladas_producidas
        -1: bandera = falso
    fin_segun_sea
fin_mientras

mostrar(toneladas_horno_1)
mostrar(toneladas_horno_2)
mostrar(toneladas_horno_3)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`numero_horno = entero
	toneladas_producidas = real
	bandera = logica
	toneladas_horno_1 = real
	toneladas_horno_2 = real
	toneladas_horno_3 = real`"]
    
    numero_horno["numero_horno = 0"]
    bandera["bandera = verdadero"]
    toneladas_horno_1["toneladas_horno_1 = 0"]
    toneladas_horno_2["toneladas_horno_2 = 0"]
    toneladas_horno_3["toneladas_horno_3 = 0"]
    
    mientras{bandera}
    
        leer_toneladas_producidas[/toneladas_producidas/]
        leer_numero_horno[/numero_horno/]
        match{"numero_horno"}
            horno_1["toneladas_horno_1 = toneladas_horno_1 + toneladas_producidas"]
            horno_2["toneladas_horno_2 = toneladas_horno_2 + toneladas_producidas"]
            horno_3["toneladas_horno_3 = toneladas_horno_3 + toneladas_producidas"]
            horno_menos1["bandera = falso"]
        
        a[" "]
    
    mostrar_horno_1{{toneladas_horno_1}}
    mostrar_horno_2{{toneladas_horno_2}}
    mostrar_horno_3{{toneladas_horno_3}}
    
	fin([fin])
    
	comienzo --> variables --> numero_horno --> bandera --> toneladas_horno_1 --> toneladas_horno_2 --> toneladas_horno_3 --> mientras
	mientras -- Sí --> leer_toneladas_producidas --> leer_numero_horno --> match
	match -- 1 --> horno_1
	match -- 2 --> horno_2
	match -- 3 --> horno_3
	match -- -1 --> horno_menos1
	horno_1 & horno_2 & horno_3 & horno_menos1 --> a --> mientras
	mientras -- No ---> mostrar_horno_1 --> mostrar_horno_2 --> mostrar_horno_3 --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240517-producciones.py"
```
