---
created: 2024-11-20 11:33:26
modified: 2024-11-20 11:45:27
title: Instrucción
---

# Instrucción

Una sentencia de código que posibilita la acción. Se escribe en **Assembler**.

> [!note]
> En muchas [[Instrucción|Instrucciones]], el resultado de la [[Operación]] suele guardarse en el primer [[Registro]] o dirección de [[RAM|Memoria]].
> 
> ```assembly
> ADD R1, R3, R7
> ```
> 
> Aquí, se suma el valor almacenado en los [[Registro|Registros]] `R3` y 
## Instrucciones aritmético lógicas

Trabajan sobre [[Registro|Registros]] internos a la [[CPU]].

Por ejemplo, `ADD`, `SUB`, `ADC`, `AND`, `OR`, `NOR`, `XOR`.

## Instrucciones de carga y almacenamiento

Operaciones de interacción con [[RAM|Memoria]]. Por ejemplo, `MOV`.

Si el [[Dato]] va de la [[RAM|Memoria]] al [[CPU]], es una operación de **carga**. Por ejemplo, `MOV R1, M1234`.

Si va del [[CPU]] a la [[RAM|Memoria]], es una operación de **almacenamiento**. Por ejemplo, `MOV M1234, R1`.

## Instrucciones de transferencia entre registros

Operaciones internas a la [[CPU]]. Por ejemplo, `MOV R1, R2`, `XCHG`.

## Instrucciones de entrada y salida (E/S o I/O)

Control de periféricos. Por ejemplo, `OUT DX, AL`, `IN AL, DX`.

## Instrucciones de control de programa

Existen dos tipos:

- **Condicionales: ejecutan saltos condicionales.**
  Tienen en cuenta `PSW` antes de su ejecución. Por ejemplo, `SMP`, `SUMP`.
- **Incondicionales.**
  Transfiere a otro punto del programa sin tener en cuenta `PSW`. Por ejemplo, `SZ`.
