---
created: 2025-04-03 18:52:50
modified: 2025-04-03 19:15:54
title: Polimorfismo
---

# Polimorfismo

El [[Polimorfismo]] es un concepto fundamental dentro del [[Paradigma orientado a objetos]] que permite que [[Objeto|Objetos]] de diferentes [[Clase|Clases]] respondan a los mismos [[Método|Métodos]] y/o [[Atributo|Atributos]].

> [!important]
> Dados dos [[Objeto|Objetos]], estos son [[Polimorfismo|Polimórficos]] si puedo reemplazar a uno con el otro sin generar [[Errores]] en la ejecución del [[Programa propio|Programa]].

Dentro de cada [[Objeto]], sus [[Método|Métodos]] deben tener la misma firma, pero su implementación puede ser diferente. Esto quiere decir que, dados dos [[Objeto|Objetos]] [[Polimorfismo|Polimórficos]], sus [[Método|Métodos]] deben cumplir las siguientes condiciones:

- Tener el mismo nombre
- La misma cantidad de [[Parámetros]], donde cada uno de ellos debe respetar un dado tipo de [[Dato]]
- Tener el mismo tipo de [[Dato]] retornado

> [!note]
> El [[Polimorfismo]] siempre se evalúa en relación a una operación. Entonces, para que dos [[Objeto|Objetos]] sean [[Polimorfismo|Polimórficos]], solo es necesario que tengan el mismo [[Método]] en común que está siendo utilizado.
