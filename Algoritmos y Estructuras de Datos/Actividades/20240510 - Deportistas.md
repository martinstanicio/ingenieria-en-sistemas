---
created: 2024-05-07 21:20:25
modified: 2024-05-10 18:44:30
title: 20240510 - Deportistas
---

# 20240510 - Deportistas

Se ingresan los datos de los deportistas: apellido, edad, sexo (El sexo es una letra, M o H). Hallar:

- Cantidad de personas ingresadas
- Cantidad de hombres
- Cantidad de mujeres
- Promedio de edad de las personas

## Pseudocódigo

```
comienzo

declarar cantidad_de_deportistas = entero, cantidad_de_hombres = entero, cantidad_de_mujeres = entero, sumatoria_de_edad = entero, promedio_de_edad = real, continuar = cadena, apellido = cadena, edad = entero, sexo = cadena

cantidad_de_deportistas = 0
continuar = ""
cantidad_de_hombres = 0
cantidad_de_mujeres = 0
sumatoria_de_edad = 0

mientras continuar != "no" entonces
    leer(apellido)
    leer(edad)
    leer(sexo)
    
    cantidad_de_deportistas = cantidad_de_deportistas + 1
    
    sumatoria_de_edad = sumatoria_de_edad + edad
    
    segun_sea sexo entonces
        "H": cantidad_de_hombres = cantidad_de_hombres + 1
        "M": cantidad_de_mujeres = cantidad_de_mujeres + 1
        sino: mostrar("Sexo no contemplado")
    
    leer(continuar)

promedio_de_edad = sumatoria_de_edad / cantidad_de_deportistas

mostrar(cantidad_de_deportistas)
mostrar(cantidad_de_hombres)
mostrar(cantidad_de_mujeres)
mostrar(promedio_de_edad)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`cantidad_de_deportistas = entero
	cantidad_de_hombres = entero
	cantidad_de_mujeres = entero
	sumatoria_de_edad = entero
	promedio_de_edad = real
	continuar = cadena
	apellido = cadena
	edad = entero
	sexo = cadena`"]
    
    cantidad_de_deportistas["cantidad_de_deportistas = 0"]
    continuar["continuar = ''"]
    cantidad_de_hombres["cantidad_de_hombres = 0"]
    cantidad_de_mujeres["cantidad_de_mujeres = 0"]
    sumatoria_de_edad["sumatoria_de_edad = 0"]
    
    mientras{"continuar != 'no'"}
    
    apellido[/apellido/]
    edad[/edad/]
    sexo[/sexo/]
    
    cantidad_de_deportistas_suma["cantidad_de_deportistas = cantidad_de_deportistas + 1"]
    
    sumatoria_de_edad_suma["sumatoria_de_edad = sumatoria_de_edad + edad"]
    
    match{{sexo}}
    
    H["cantidad_de_hombres = cantidad_de_hombres + 1"]
    M["cantidad_de_mujeres = cantidad_de_mujeres + 1"]
    otro{{"Sexo no contemplado"}}
    
    desea_continuar[/continuar/]
    
    promedio_de_edad["promedio_de_edad = sumatoria_de_edad / cantidad_de_deportistas"]
    
	mostrar_cantidad_de_deportistas{{cantidad_de_deportistas}}
	mostrar_cantidad_de_hombres{{cantidad_de_hombres}}
	mostrar_cantidad_de_mujeres{{cantidad_de_mujeres}}
	mostrar_promedio_de_edad{{promedio_de_edad}}
	
	fin([fin])
    
	comienzo --> variables --> cantidad_de_deportistas --> continuar --> cantidad_de_hombres --> cantidad_de_mujeres --> sumatoria_de_edad --> mientras
	mientras -- Sí --> apellido --> edad --> sexo --> cantidad_de_deportistas_suma --> sumatoria_de_edad_suma --> match
	match -- "H" --> H
	match -- "M" --> M
	match -- "Otro" --> otro
	H & M & otro --> desea_continuar --> mientras
	mientras --- No ---> promedio_de_edad
	promedio_de_edad --> mostrar_cantidad_de_deportistas --> mostrar_cantidad_de_hombres --> mostrar_cantidad_de_mujeres --> mostrar_promedio_de_edad --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240510-deportistas.py"
```
