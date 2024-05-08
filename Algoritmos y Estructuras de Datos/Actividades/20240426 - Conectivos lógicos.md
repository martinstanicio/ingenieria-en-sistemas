# 20240426 - Conectivos lógicos

Se ingresan 3 números, obtener el mayor utilizando [[Conectivos lógicos]].

## Pseudocódigo

```
comienzo

declarar numero1 = real, numero2 = real, numero3 = real

leer(numero1)
leer(numero2)
leer(numero3)

si (numero1 >= numero2) y (numero1 >= numero3) entonces
    print(numero1)
fin si

si (numero2 >= numero1) y (numero2 >= numero3) entonces
    print(numero2)
fin si

si (numero3 >= numero1) y (numero3 >= numero2) entonces
    print(numero3)
fin si

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`numero1 = real
	numero2 = real
	numero3 = real`"]

	leer1[/numero1/]
    leer2[/numero2/]
    leer3[/numero3/]

    si1{"(numero1 >= numero2) y (numero1 >= numero3)"}
	mayor1{{numero1}}
	
	si2{"(numero2 >= numero1) y (numero2 >= numero3)"}
	mayor2{{numero2}}
	
	si3{"(numero3 >= numero1) y (numero3 >= numero2)"}
	mayor3{{numero3}}

	fin([fin])

	comienzo --> variables --> leer1 --> leer2 --> leer3 --> si1
	si1 -- Sí --> mayor1 --> si2
	si1 -- No --> si2
	si2 -- Sí --> mayor2 --> si3
	si2 -- No --> si3
	si3 -- Sí --> mayor3 --> fin
	si3 -- No --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240426-conectivos-logicos.py"
```
