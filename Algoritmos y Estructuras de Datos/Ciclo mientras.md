# Ciclo mientras

Es una [[Estructuras de control#De repetición]] que ejecuta una serie de instrucciones dadas **mientras** se cumpla una condición.

Para evitar que se vuelva un ciclo infinito, podemos utilizar diferentes estrategias:

- Utilizar un [[Acumulador]]
- Controlar con una opción a continuar
- Controlar con valor centinela
- Controlar con una [[Bandera]]

```mermaid
flowchart TB
	comienzo([comienzo])
    
    condicion{{"Condición"}}
    
    A[A]
    B[B]
    C[C]
    
    X[X]
    
	fin([fin])
    
	comienzo --> condicion
	condicion -- Sí --> A --> B --> C --> condicion
	condicion -- No --> X ---> fin
```

## Python

```python
c = 0

while c < 4:
    c = c + 1
    print(f"El ciclo se ejecutó {c} veces")
```
