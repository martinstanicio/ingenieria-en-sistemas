---
created: 2024-11-20 11:47:25
modified: 2024-11-20 18:00:53
title: Modos de direccionamiento
---

# Modos de direccionamiento

Forma en que la [[Instrucción]] especifica la dirección en donde está el operando, ya sea en [[RAM|Memoria]] o en un [[Registro]].

## Implícito

Operandos internos a [[CPU]] en [[Registro|Registros]].

Se suele utilizar con [[Instrucción#Instrucciones aritmético lógicas|Instrucciones aritmético lógicas]]. Por ejemplo, `MOV R1, R2`.

## Directo

Operando en memoria. Se suele utilizar con [[Instrucción#Instrucciones de carga y almacenamiento|Instrucciones de carga y almacenamiento]].

## Indirecto o indexado

El operando refiere a un puntero o índice mediante su dirección en [[RAM|Memoria]].

Por ejemplo, `MOV R5, @X`.

## Inmediato

Cuando el operando forma parte de la [[Instrucción]]. Por ejemplo, `MOV R1, #H4C`.
