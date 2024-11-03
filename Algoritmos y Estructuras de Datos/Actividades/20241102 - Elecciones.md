---
created: 2024-11-02 20:08:46
modified: 2024-11-03 17:24:09
title: 20241102 - Elecciones
---

# 20241102 - Elecciones

Se tiene el siguiente [[Archivo]] plano `elecciones.txt` con el resultado de las elecciones presidenciales en Argentina (separador ";"):

- Ciudad (cadena)
- Número de mesa (entero)
- Votos Milei (entero)
- Votos Massa (entero)

El [[Archivo]] ya está ordenado por el campo ciudad. Mostrar:

- Total de votos de Milei por cada ciudad.
- Total de votos de Massa por cada ciudad.
- Ciudad con el mayor total de votos de Milei (no repetido).
- Ciudad con el mayor total de votos de Massa (no repetido).

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declarar["`archivo = archivo
	registro = cadena
	vector[4] = cadena
	max_milei = entero
	ciudad_milei = cadena
	max_massa = entero
	ciudad_massa = cadena
	z_milei = entero
	z_massa = entero
	control = cadena
	ciudad = cadena
	n_mesa = entero
	v_milei = entero
	v_massa = entero`"]
	inicializar["`max_milei = -1
	ciudad_milei = ''
	max_massa = -1
	ciudad_massa = ''`"]
	
	archivo_abrir["archivo = ABRIR('elecciones.txt', 'r')"]
	registro1["registro = LEER(registro)"]
	vector1["vector = SEPARAR(registro, ';')"]
	
	reset1["`z_milei = 0
	z_massa = 0
	control = vector[1]`"]
	
	while{"registro <> ''"}
	vector2["vector = SEPARAR(registro, ';')"]
	campos["`ciudad = vector[1]
	n_mesa = VALOR(vector[2])
	v_milei = VALOR(vector[3])
	v_massa = VALOR(vector[4])`"]
	
	if1{"ciudad = control"}
	if1_yes["`z_milei = z_milei + v_milei
	z_massa = z_massa + v_massa`"]
	mostrar1_ciudad{{"control"}}
	mostrar1_milei{{"z_milei"}}
	mostrar1_massa{{"z_massa"}}
	
	if2{"z_milei > max_milei"}
	if2_yes["`max_milei = z_milei
	ciudad_milei = control`"]
	
	if3{"z_massa > max_massa"}
	if3_yes["`max_massa = z_massa
	ciudad_massa = control`"]
	
	reset2["`z_milei = v_milei
	z_massa = v_massa
	control = ciudad`"]
	
	registro2["registro = LEER(registro)"]
	
	archivo_cerrar["CERRAR(archivo)"]
	
	mostrar2_ciudad{{"control"}}
	mostrar2_milei{{"z_milei"}}
	mostrar2_massa{{"z_massa"}}
	
	mostrar3_milei{{"ciudad_milei"}}
	mostrar3_massa{{"ciudad_massa"}}
	
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> declarar --> inicializar --> archivo_abrir --> registro1 --> vector1 --> reset1 --> a --> while -- "Sí" --> vector2 --> campos --> if1
	if1 -- "Sí" --> if1_yes --> b
	if1 -- "No" --> mostrar1_ciudad --> mostrar1_milei --> mostrar1_massa --> if2
	if2 -- "Sí" --> if2_yes --> c
	if2 -- "No" --> c
	c --> if3
	if3 -- "Sï" --> if3_yes --> d
	if3 -- "No" --> d
	d --> reset2 --> b
	b --> registro2 --> a
	while -- "No" ---------> archivo_cerrar --> mostrar2_ciudad --> mostrar2_milei --> mostrar2_massa --> mostrar3_milei --> mostrar3_massa --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-elecciones/main.py"
```

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-elecciones/elecciones.txt"
```
