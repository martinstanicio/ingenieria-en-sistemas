---
created: 2024-10-22 22:52:45
modified: 2024-11-03 13:13:17
title: 20241022 - Deportistas
---

# 20241022 - Deportistas

El usuario ingresa el deporte cuyas estadísticas queremos analizar. Mostrar:

- Cantidad de deportistas que practican ese deporte
- Promedio de altura de las personas que practican ese deporte
- Mayor edad de la persona que practica ese deporte

Cada registro del archivo `deportistas.txt` contiene los siguientes campos:

- Número de socio (entero)
- Apellido (cadena)
- Altura (real)
- Edad (entero)
- Deporte (cadena): "f", "b" o "v"

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declarar["`target = entero
	deportistas = entero
	altura_acumulador = real
	altura_promedio = real
	max_edad = entero
	archivo = archivo
	registro = cadena
	vector[5] = cadena
	altura = real
	edad = entero
	deporte = cadena`"]
	inicializar["`deportistas = 0
	altura_acumulador = 0.0
	altura_promedio = 0.0
	max_edad = 0`"]
	
	target[/"target"/]
	
	archivo_abrir["archivo = ABRIR('deportistas.txt', 'r')"]
	registro1["registro = LEER(archivo)"]
	
	while{"registro <> ''"}
	vector["vector = SEPARAR(registro, ';')"]
	campos["`altura = VALOR(vector[3])
	edad = VALOR(vector[4])
	deporte = vector[5]`"]
	
	if1{"deporte = target"}
	if1_yes["`deportistas = deportistas + 1
	altura_acumulador = altura_acumulador + altura`"]
	
	if2{"edad > max_edad"}
	if2_yes["max_edad = edad"]
	
	registro2["registro = LEER(archivo)"]
	
	archivo_cerrar["CERRAR(archivo)"]
	
	if3{"deportistas > 0"}
	if3_yes["altura_promedio = altura_acumulador / deportistas"]
	
	mostrar1{{"deportistas"}}
	mostrar2{{"altura_promedio"}}
	mostrar3{{"max_edad"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> declarar --> inicializar --> target --> archivo_abrir --> registro1 --> a --> while -- "Sí" --> vector --> campos --> if1
	if1 -- "Sí" --> if1_yes --> if2
	if2 -- "Sí" --> if2_yes --> b
	if2 -- "No" --> b
	b --> c
	if1 -- "No" --> c --> registro2 --> a
	while -- "No" --> archivo_cerrar --> if3
	if3 -- "Sí" --> if3_yes --> d
	if3 -- "No" --> d
	d --> mostrar1 --> mostrar2 --> mostrar3 --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241022-deportistas/main.py"
```

```embed-shell
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241022-deportistas/deportistas.txt"
```
