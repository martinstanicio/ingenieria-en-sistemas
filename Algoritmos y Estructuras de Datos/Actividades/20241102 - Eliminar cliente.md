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
	if1_yes["backup = GUARDAR(registro)"]
	eliminado["eliminado = verdadero"]
	mostrar_eliminado{{"`id_cliente
	nombre
	edad
	ciudad`"}}
	
	registro2["registro = LEER(clientes)"]
	
	clientes_cerrar["CERRAR(clientes)"]
	backup_cerrar["CERRAR(backup)"]
	
	copiar2["COPIAR('backup.txt', 'clientes.txt')"]
	
	if2{"no eliminado"}
	if2_yes{{"No existe un cliente con id {target}"}}
	
    fin([fin])
    
    a[" "]
    b[" "]
    c[" "]
    
	comienzo --> declarar --> inicializar --> target --> copiar1 --> clientes_abrir --> backup_abrir --> registro1 --> a --> while -- "Sí" --> vector --> campos --> if1
	if1 -- "Sí" --> if1_yes --> b
	if1 -- "No" --> eliminado --> mostrar_eliminado --> b
	b --> registro2 --> a
	while -- "No" --> clientes_cerrar --> backup_cerrar --> copiar2 --> if2
	if2 -- "Sí" --> if2_yes --> c
	if2 -- "No" --> c
	c --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-eliminar-cliente/main.py"
```

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20241102-eliminar-cliente/clientes.txt"
```
