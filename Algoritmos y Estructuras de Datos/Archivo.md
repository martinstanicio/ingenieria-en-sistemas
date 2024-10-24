---
created: 2024-10-08 22:10:52
modified: 2024-10-22 21:33:04
title: Archivo
---

# Archivo

Una [[Estructuras de datos]] que de almacena en memoria **permanente**.

Un [[Archivo]] es un [[Conjunto]] de registros. Un registro es un [[Conjunto]] de campos, y en cada campo guardamos un [[Dato]].

Por ejemplo, la siguiente tabla representa un [[Archivo]].

| Registro 1 | Registro 2 |
| ---------- | ---------- |
| Campo      | Campo      |
| Campo      | Campo      |
| Campo      | Campo      |

> [!tip]
> Todo [[Archivo]] siempre tiene una **marca de final de [[Archivo]]** o EOF: *End Of File*. En [[Python]], es una **cadena vacía** (`""`).

## Abrir archivo

En [[Python]], se realiza de la siguiente forma.

```python
nombre = "test.txt"
modo = "w"

archivo = open(nombre, modo)
```

En un [[Diagrama de flujo]], se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo([comienzo])
    
    A["..."]
    B["variable = abrir(nombre_archivo)"]
    C["..."]
    
	fin([fin])
    
	comienzo --> A --> B --> C --> fin
```

Existen múltiples modos para abrir un archivo, algunos de los más utilizados son los siguientes.

### Modo escritura

```python
open(nombre, "w")
```

Escribe el [[Archivo]] desde 0, eliminando sus contenidos previos.

> [!note]
> Si el [[Archivo]] no existe, se crea automáticamente.

### Modo lectura

```python
open(nombre, "r")
```

Nos permite leer los contenidos de un [[Archivo]].

> [!caution]
> El [[Archivo]] debe existir. Caso contrario, devuelve un [[Errores|Error]] de tipo `FileNotFoundError`.

Al abrir el [[Archivo]] en [[Archivo#Modo lectura]], un **puntero** se ubica en el **primer registro**.

### Modo append

```python
open(nombre, "a")
```

Permite escribir [[Información]] al [[Archivo]], sin eliminar sus contenidos previos.

> [!note]
> Si el [[Archivo]] no existe, se crea automáticamente.

## Cerrar archivo

Es importante **cerrar** el [[Archivo]]. Si nos olvidamos de hacerlo, pueden haber *memory leaks*, y es posible que los cambios realizados **no sean guardados**.

En [[Python]], se realiza de la siguiente forma.

```python
archivo.close()
```

En [[Diagrama de flujo]], se realiza de la siguiente forma.

```mermaid
flowchart TB
	comienzo([comienzo])
    
    A["..."]
    B["cerrar(nombre_archivo)"]
    C["..."]
    
	fin([fin])
    
	comienzo --> A --> B --> C --> fin
```

## Leer archivo

Podemos leer un **registro** de un [[Archivo]] utilizando el método `readline`.

> [!important]
> Cada vez que llamamos al método `readline`, nos devuelve una nueva línea.

```python
archivo = open(nombre, "r")

registro = archivo.readline()
print(registro) # linea 1

registro = archivo.readline()
print(registro) # linea 2
```

> [!warning]
> Una vez que se leyeron todas las líneas, el método `readline` devuelve una cadena vacía.

## Escribir archivo

Podemos escribir un **registro** a un [[Archivo]] utilizando el método `write`.

```python
archivo = open(nombre, "w")
registro = f"{campo1};{campo2};{campo3}"

archivo.write(registro + "\n")
archivo.close()
```

> [!tip]
> Para que cada registro esté en una línea nueva, agregamos `\n`.
