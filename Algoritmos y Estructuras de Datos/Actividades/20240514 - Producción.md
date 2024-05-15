---
created: 2024-05-14 21:15:00
modified: 2024-05-14 21:37:01
title: 20240514 - Producción
---

# 20240514 - Producción

Se ingresan los datos de producción de una empresa de cerámicos:

- Fecha de producción (cadena de la forma `dd/mm/aaaa`)
- Toneladas producidas
- Turno de producción ("M" para mañana o "T" para tarde)

Hallar:

- Total de toneladas producidas en el turno mañana
- Total de toneladas producidas en el turno tarde

La última producción tiene como toneladas producidas $-9999$ y no se debe procesar. Usar un [[Ciclo mientras]] controlado con [[Valor centinela]]

## Pseudocódigo

```
comienzo

declarar toneladas_producidas_manana = real, toneladas_producidas_tarde = real, toneladas_producidas_turno = real, fecha_produccion = cadena, turno_produccion = cadena

toneladas_producidas_manana = 0
toneladas_producidas_tarde = 0

leer(toneladas_producidas_turno)

mientras toneladas_producidas_turno != -9999 entonces
    si toneladas_producidas_turno != -9999 entonces
        leer(fecha_produccion)
        leer(turno_produccion)
        
        segun_sea turno_produccion entonces
            "M": toneladas_producidas_manana = toneladas_producidas_manana + toneladas_producidas_turno
            "T": toneladas_producidas_tarde = toneladas_producidas_tarde + toneladas_producidas_turno
        fin_segun_sea
        
        leer(toneladas_producidas_turno)
    fin_si
fin_mientras

mostrar(toneladas_producidas_manana)
mostrar(toneladas_producidas_tarde)

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
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240514-produccion.py"
```
