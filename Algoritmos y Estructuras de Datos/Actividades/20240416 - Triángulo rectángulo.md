# 20240416 - Triángulo rectángulo

Se ingresan los catetos de un triángulo rectángulo, hallar la hipotenusa.

## Pseudocódigo

```
comienzo

declarar cateto_a = real, cateto_b = real, hipotenusa = entero

leer(cateto_a)
leer(cateto_b)

hipotenusa = √(cateto_a^2 + cateto_b^2)

mostrar(hipotenusa)

fin
```

## Diagrama de flujo

```mermaid
flowchart TB
	comienzo([comienzo])

	variables["`cateto_a = real
	cateto_b = real
	hipotenusa = real`"]

	leer_cateto_a[/apellido/]
	leer_cateto_b[/valorHora/]

	hipotenusa["hipotenusa = √(cateto_a^2 + cateto_b^2)"]

	mostrar{{"hipotenusa"}}
	
	fin([fin])

	comienzo --> variables --> leer_cateto_a --> leer_cateto_b --> hipotenusa --> mostrar --> fin
```
