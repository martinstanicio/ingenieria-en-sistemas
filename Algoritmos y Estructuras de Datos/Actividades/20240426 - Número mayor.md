# 20240426 - Número mayor

Se ingresan 4 números, obtener el mayor. Solo utilizar [[Bifurcaciones#Bifurcación simple|bifurcaciones simples]] o [[Bifurcaciones#Bifurcación doble|dobles]].

## Pseudocódigo

```
comienzo

declarar numero1 = real, numero2 = real, numero3 = real, numero4 = real, numero_mayor = real

leer(numero1)
leer(numero2)
leer(numero3)
leer(numero4)

numero_mayor = numero1

si numero2 >= numero_mayor entonces
    numero_mayor = numero2
fin si

si numero3 >= numero_mayor entonces
    numero_mayor = numero3
fin si

si numero4 >= numero_mayor entonces
    numero_mayor = numero4
fin si

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`numero1 = real
	numero2 = real
	numero3 = real
	numero4 = real
	numero_mayor = real`"]

	leer1[/numero1/]
    leer2[/numero2/]
    leer3[/numero3/]
    leer4[/numero4/]

    numero_mayor[numero_mayor = numero1]

    si2{numero2 >= numero_mayor}
	mayor2["numero_mayor = numero2"]

    si3{numero3 >= numero_mayor}
	mayor3["numero_mayor = numero3"]

    si4{numero4 >= numero_mayor}
	mayor4["numero_mayor = numero4"]

    mostrar{{"numero_mayor"}}

	fin([fin])

	comienzo --> variables --> leer1 --> leer2 --> leer3 --> leer4 --> numero_mayor --> si2
	si2 -- Sí --> mayor2 --> si3
	si2 -- No --> si3
	si3 -- Sí --> mayor3 --> si4
	si3 -- No --> si4
	si4 -- Sí --> mayor4 --> mostrar
	si4 -- No --> mostrar
	
	mostrar --> fin
```

## Código

```embed-python
PATH: "vault://Algoritmos y Estructuras de Datos/python/20240426-numero-mayor.py"
```
