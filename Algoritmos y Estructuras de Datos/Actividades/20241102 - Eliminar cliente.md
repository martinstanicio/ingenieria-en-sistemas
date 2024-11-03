---
created: 2024-11-02 19:26:57
modified: 2024-11-02 19:44:05
title: 20241102 - Eliminar cliente
---

# 20241102 - Eliminar cliente

Tienes un [[Archivo]] llamado `clientes.txt` que almacena [[Información]] de clientes. Cada registro contiene:

- ID de cliente (entero)
- Nombre (cadena)
- Edad (entero)
- Ciudad (cadena)

Implementa un programa que permita al usuario ingresar el ID de un cliente que desea eliminar. Mostrar nombre, edad y ciudad del cliente eliminado.

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])
    
	declarar["`target = entero
	clientes = archivo
	backup = archivo
	registro = cadena
	eliminado = logica
	vector[4] = cadena
	id_cliente = entero
	nombre = cadena
	edad = entero
	ciudad = cadena`"]
	inicializar["eliminado = falso"]
	
	target[/"target"/]
	copiar1["COPIAR('clientes.txt', 'backup.txt')"]
	
	clientes_abrir["clientes = ABRIR('clientes.txt', 'r')"]
	backup_abrir["backup = ABRIR('backup.txt', 'w')"]
	registro1["registro = LEER(clientes)"]
	
	while{"registro <> '' y no eliminado"}
	vector["vector = SEPARAR(registro, ';')"]
	campos["`id_cliente = VALOR(vector[1])
	nombre = vector[2]
	edad = VALOR(vector[3])
	ciudad = vector[4]`"]
	
	if1{"id_cliente <> target"}
	if1_yes["GUARDAR()"]
	
    fin([fin])
    
	comienzo --> variables --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-eliminar-cliente/main.py"
```

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-eliminar-cliente/clientes.txt"
```
