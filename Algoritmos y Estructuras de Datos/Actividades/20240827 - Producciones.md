---
created: 2024-08-27 22:35:22
modified: 2024-08-30 15:47:54
title: 20240827 - Producciones
---

# 20240827 - Producciones

Se ingresa con opción a continuar las producciones de distintas sucursales de una empresa:

- Número de sucursal (entero, 1-15)
- Toneladas producidas (real)
- Fecha de producción (cadena)

Mostrar:

- Total de toneladas producidas por cada número de sucursal
- Cantidad de producciones por cada número de sucursal
- Promedio de toneladas producidas por cada número de sucursal
- Número de sucursales con el mayor total de toneladas producidas (repetido)
- Total de toneladas producidas por cada mes

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	variables["`toneladas_producidas[16] = real
	cantidad_producciones[16] = entero
	promedio_produccion[16] = real
	toneladas_por_mes[13] = real
	max_ton = real
	max_ton_repeticiones = entero
	continuar = cadena`"]
	init["`max_ton = -1.0
	max_ton_repeticiones = 0
	continuar = 'si'`"]
	
	while{"continuar <> 'no'"}
	input[/"`numero_sucursal
	ton
	fecha_produccion`"/]
	contador["toneladas_producidas[numero_sucursal] = toneladas_producidas[numero_sucursal] + ton"]
	acumulador["cantidad_producciones[numero_sucursal] = cantidad_producciones[numero_sucursal] + 1"]
	mes["mes_produccion = entero(fecha_produccion[3:5])"]
	ton_mes["toneladas_por_mes[mes_produccion] = toneladas_por_mes[mes_produccion] + ton]"]
	continuar[/continuar/]
	
	for1{{"i, 1, 16"}}
	if1{"cantidad_producciones[i] <> 0"}
	calc_promedio["promedio_produccion[i] = toneladas_producidas[i] / cantidad_producciones[i]"]
	if2{"toneladas_producidas[i] > max_ton"}
	new_max["max_ton = toneladas_producidas[i]"]
	
	for2{{"i, 1, 16"}}
	if3{"toneladas_producidas[i] = max_ton"}
	new_max_repeat["max_ton_repeticiones = max_ton_repeticiones + 1"]
	
	for3{{"i, 1, 16"}}
	mostrar_toneladas_producidas{{"toneladas_producidas[i]"}}
	mostrar_cantidad_producciones{{"cantidad_producciones[i]"}}
	mostrar_promedio_toneladas{{"promedio_produccion[i]"}}
	
	mostrar_numero_sucursales_max_produccion{{"max_ton_repeticiones"}}
	
	for4{{"i, 1, 13"}}
	mostrar_toneladas_mes{{"toneladas_por_mes[i]"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    e[" "]
    f[" "]
    g[" "]
    h[" "]
    
	comienzo --> variables --> init --> a --> while --> input --> contador --> acumulador --> mes --> ton_mes --> continuar --> a
	continuar --> for1 --> if1
	for1 --> d
	if1 -- "Sí" --> calc_promedio --> b
	if1 -- "No" --> b
	b --> if2
	if2 -- "Sí" --> new_max --> c
	if2 -- "No" --> c
	c --> d --> for2 --> if3
	for2 --> f
	if3 -- "Sí" --> new_max_repeat --> e
	if3 -- "No" --> e
	e --> f --> for3 --> mostrar_toneladas_producidas --> mostrar_cantidad_producciones --> mostrar_promedio_toneladas --> g
	for3 --> g --> mostrar_numero_sucursales_max_produccion --> for4 --> mostrar_toneladas_mes --> h
	for4 --> h --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240827-producciones.py"
```
