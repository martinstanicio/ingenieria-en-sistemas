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
    
    segun_sea sexo entonces
        "H": cantidad_de_hombres = cantidad_de_hombres + 1
        "M": cantidad_de_mujeres = cantidad_de_mujeres + 1
        sino: mostrar("Sexo no contemplado")
    
    sumatoria_de_edad = sumatoria_de_edad + edad

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
    
	variables["`sueldo = real
	cantidad_de_empleados = entero
	contador_empleado = entero
	sumatoria_de_sueldos = real
	promedio_de_sueldos = real`"]
    
    cantidad_de_empleados["cantidad_de_empleados = 5"]
    contador_empleado["contador_empleado = 0"]
    
    mientras{"contador_empleado < cantidad_de_empleados"}
    
    contador_empleado_suma["contador_empleado = contador_empleado + 1"]
    
    sueldo[/sueldo/]
    
    sumatoria_de_sueldos["sumatoria_de_sueldos = sumatoria_de_sueldos + sueldo"]
    
    promedio_de_sueldos["promedio_de_sueldos = sumatoria_de_sueldos / cantidad_de_empleados"]
    
	mostrar_sumatoria{{sumatoria_de_sueldos}}
	mostrar_promedio{{promedio_de_sueldos}}
	
	fin([fin])
    
	comienzo --> variables --> cantidad_de_empleados --> contador_empleado --> mientras
	mientras -- Sí --> contador_empleado_suma --> sueldo --> sumatoria_de_sueldos --> mientras
	mientras -- No --> promedio_de_sueldos
	promedio_de_sueldos --> mostrar_sumatoria --> mostrar_promedio --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240510-deportistas.py"
```
