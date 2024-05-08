# Ciclo mientras
Es una [[Estructuras de control#De repetición]] que ejecuta una serie de instrucciones dadas **mientras** se cumpla una condición.

```mermaid
flowchart TB
	comienzo([comienzo])
    
    C1{{"Condición"}}
    
    A[A]
    B[B]
    C[C]
    
    X[X]
    
	fin([fin])
    
	comienzo --> C1
	C1 -- Sí --> A --> B --> C -->
	match -- "B" --> B
	match -- "C" --> C
	match -- "Otro" --> categoria_invalida
	A & B & C & categoria_invalida --> validez
	validez -- Sí --> sueldo --> mostrar_sueldo
	validez -- NO --> mostrar_categoria_incorrecta
	mostrar_sueldo & mostrar_categoria_incorrecta --> fin