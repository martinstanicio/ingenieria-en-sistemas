---
created: 2024-11-02 18:06:32
modified: 2024-11-02 18:36:51
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
	
	archivo_abrir["archivo = ABRIR('empleados.dat', 'r')"]
	registro1["registro = LEER(archivo)"]
	
	while{"registro != ''"}
	vector["vector = SEPARAR(registro, ';')"]
    
    fin([fin])
    
	comienzo --> variables --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-empleados/main.py"
```

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-empleados/empleados.dat"
```
