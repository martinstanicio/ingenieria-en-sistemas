---
created: 2024-11-02 18:06:32
modified: 2024-11-02 19:15:11
title: 20241102 - Empleados
---

# 20241102 - Empleados

Crea un programa que lea un [[Archivo]] `empleados.dat`, donde cada registro contiene:

- Legajo de empleado (entero)
- Nombre (cadena)
- Edad (entero)
- Departamento (cadena): "a", "b", o "c"
- Salario (real)

El programa debe permitir al usuario ingresar un departamento y mostrar:

- La cantidad de empleados en ese departamento
- El promedio de salario de los empleados en ese departamento
- El nombre, edad y salario del empleado con menor legajo en ese departamento

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declarar["`target = cadena
	empleados = entero
	acu_salario = real
	promedio_salario = real
	min_legajo = entero
	empleado[3] = cadena
	archivo = archivo
	registro = cadena
	vector[5] = cadena
	legajo = entero
	nombre = cadena
	edad = entero
	departamento = cadena
	salario = real`"]
	inicializar["`empleados = 0
	acu_salario = 0.0
	promedio_salario = 0.0
	min_legajo = 9999999
	empleado = ['', '', '']`"]
	
	target[/"target"/]
	
	archivo_abrir["archivo = ABRIR('empleados.dat', 'r')"]
	registro1["registro = LEER(archivo)"]
	
	while{"registro != ''"}
	vector["vector = SEPARAR(registro, ';')"]
	
    campos["`legajo = VALOR(vector[0])
    nombre = vector[1]
    edad = VALOR(vector[2])
    departamento = vector[3]
    salario = VALOR(vector[4])`"]
    
    if1{"departamento = target"}
    if1_si["`empleados = empleados + 1
    acu_salario = acu_salario + salario`"]
    
    if2{"legajo < min_legajo"}
    if2_si["`min_legajo = legajo
    empleado[0] = nombre
    empleado[1] = VALOR(edad)
    empleado[2] = VALOR(salario)`"]
    
    registro2["registro = LEER(archivo)"]
    
    archivo_cerrar["CERRAR(archivo)"]
    
    if3{"empleados > 0"}
    promedio["promedio_salario = acu_salario / empleados"]
    
    mostrar1{{"empleados"}}
    mostrar2{{"promedio_salario"}}
    mostrar3{{"`empleado[0]
    empleado[1]
    empleado[2]`"}}
    
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    d[" "]
    
	comienzo --> declarar --> inicializar --> target --> archivo_abrir --> registro1 --> a --> while -- "Sí" --> vector --> campos --> if1
	if1 -- "Sí" --> if1_si --> if2
	if2 -- "Sí" --> if2_si --> b
	if2 -- "No" --> b
	b --> c
	if1 -- "No" --> c --> registro2 --> a
	while -- "No" --> archivo_cerrar --> if3
	if3 -- "Sí" --> promedio --> d
	if3 -- "No" --> d
	d --> mostrar1 --> mostrar2 --> mostrar3 --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-empleados/main.py"
```

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-empleados/empleados.dat"
```
