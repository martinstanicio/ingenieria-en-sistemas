---
created: 2024-11-05 10:36:29
modified: 2024-11-05 11:19:18
title: 20241105 - Concesionario
---

# 20241105 - Concesionario

Existe un [[Archivo]] plano  `ventas.txt` con los datos de las ventas de automóviles efectuadas por vendedores de una empresa en el año 2022, separador ";". Cada registro representa una venta.

- Número de vendedor (entero, entre 1 y 40)
- Fecha de facturación (cadena dd/mm/aaaa)
- Importe (real)

Mostrar:

- Cantidad de ventas realizadas por cada número de vendedor.
- Total de importe facturado por cada número de vendedor.
- Total de importe facturado en cada mes.
- Número de vendedor con la mayor cantidad de ventas realizadas (máximo repetido).

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declarar["`vendedores = entero
	ventas[40] = entero
	importes[40] = real
	meses[12] = real
	max_ventas = entero
	archivo = archivo
	registro = cadena
	vector[3] = cadena
	n = entero
	fecha = cadena
	importe = real
	mes = entero
	i = entero`"]
	inicializar["`vendedores = 40
	max_ventas = -1`"]
	
	for1{{"i, 1, vendedores + 1"}}
	inicializar_vectores1["`ventas[i] = 0
	importes[i] = 0.0`"]
	
	for2{{"i, 1, 12 + 1"}}
	inicializar_vectores2["meses[i] = 0.0"]
	
	archivo_abrir["archivo = ABRIR('ventas.txt', 'r')"]
	registro1["registro = LEER(archivo)"]
	
	while{"registro <> ''"}
	vector["vector = SEPARAR(registro, ';')"]
	campos["`n = VALOR(vector[1])
	fecha = vector[2]
	importe = VALOR(vector[3])`"]
	mes["mes = VALOR(fecha[4:6])"]
	ventas["ventas[n] = ventas[n] + 1"]
	importes["importes[n] = importes[n] + importe"]
	meses["meses[mes] = meses[mes] + importe"]
	
	registro2["registro = LEER(archivo)"]
	
	archivo_cerrar["CERRAR(archivo)"]
	
	for3{{"i, 1, vendedores + 1"}}
	mostrar1{{"`ventas[i]
	importes[i]`"}}
	if1{"ventas[i] > max_ventas"}
	max_ventas["max_ventas = ventas[i]"]
	
	for4{{"i, 1, 12 + 1"}}
	mostrar2{{"meses[i]"}}
	
	for5{{"i, 1, vendedores + 1"}}
	if2{"ventas[i] = max_ventas"}
	mostrar3{{"i"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    e[" "]
    f[" "]
    g[" "]
    h[" "]
    
	comienzo --> declarar --> inicializar --> for1 --> inicializar_vectores1 --> a
	for1 --> a --> for2 --> inicializar_vectores2 --> b
	for2 --> b --> archivo_abrir --> registro1 --> c --> while -- "Sí" --> vector --> campos --> mes --> ventas --> importes --> meses --> registro2 --> c
	while -- "No" --> archivo_cerrar --> for3 --> mostrar1 --> if1
	if1 -- "Sí" --> max_ventas --> d
	if1 -- "No" --> d
	d --> e
	for3 --> e --> for4 --> mostrar2 --> f
	for4 --> f --> for5 --> if2
	if2 -- "Sí" --> mostrar3 --> g
	if2 -- "No" --> g
	g --> h
	for5 --> h --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241105-concesionario/main.py"
```
