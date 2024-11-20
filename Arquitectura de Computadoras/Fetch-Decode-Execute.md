---
created: 2024-11-20 12:32:39
modified: 2024-11-20 12:48:15
title: Fetch-Decode-Execute
---

# Fetch-Decode-Execute

Es el ciclo fundamental que realiza un procesador para ejecutar cada [[Instrucción]] de un programa. 

| **Etapa**   | **[[Unidad de Control (CU)]]**                                                      | **[[Registro\|Registros]]**                                                                                                       | **[[ALU]]**                              |
| ----------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Fetch**   | Coordina la obtención de la [[Instrucción]]. Actualiza el [[Program Counter (PC)]]. | [[Program Counter (PC)]] indica la dirección de [[RAM\|Memoria]]; [[Registro de Instrucciones (IR)]] almacena la [[Instrucción]]. | No participa.                            |
| **Decode**  | Interpreta la [[Instrucción]] y genera señales de control.                          | Identifica [[Registro\|Registros]] fuente/destino.                                                                                | No participa.                            |
| **Execute** | Supervisa la ejecución y actualiza [[Flags]].                                       | Proveen [[Dato\|Datos]] y almacenan resultados.                                                                                   | Realiza operaciones aritméticas/lógicas. |

## Fetch

El procesador localiza y obtiene la próxima [[Instrucción]] desde la [[RAM|Memoria]] principal. 

1. La [[Unidad de Control (CU)]] utiliza el [[Program Counter (PC)]].
2. El procesador envía esta dirección al bus de [[RAM|Memoria]], solicitando la [[Instrucción]] almacenada.
3. La [[Instrucción]] es transferida desde la [[RAM|Memoria]] principal hacia el [[Registro de Instrucciones (IR)]].
4. El [[Program Counter (PC)]] se incrementa automáticamente para apuntar a la siguiente [[Instrucción]].

## Decode

En esta etapa, el procesador interpreta la [[Instrucción]] almacenada en el [[Registro de Instrucciones (IR)]] y determina qué operación realizar.

1. La [[Unidad de Control (CU)]] examina la instrucción en el [[Registro de Instrucciones (IR)]], identificando el *opcode* (código de operación) y los operandos.
2. Según la [[Instrucción]], la [[Unidad de Control (CU)]] identifica los [[Recursos]] necesarios: [[Registro|Registros]] fuente, destino, [[RAM|Memoria]] o la [[ALU]].
3. Si la [[Instrucción]] requiere acceder a operandos en [[RAM|Memoria]], la [[Unidad de Control (CU)]] emite las señales necesarias para obtenerlos.

## Execute

En esta etapa, el procesador realiza la operación indicada por la [[Instrucción]] decodificada.

1. Si la [[Instrucción]] es [[Instrucción#Instrucciones aritmético lógicas|Aritmético lógica]], la [[ALU]] realiza la operación.
2. Si la [[Instrucción]] implica [[Instrucción#Instrucciones de carga y almacenamiento|Transferencia de datos]], estos se mueven entre [[Registro|Registros]] y [[RAM|Memoria]].
3. Si es una [[Instrucción#Instrucciones de control de programa|Instrucción de control]] (como un salto), el [[Program Counter (PC)]] se actualiza con la nueva dirección de [[RAM|Memoria]] indicada.
4. Se actualiza el [[Program Status Word (PSW)]], que contiene [[Flags]] como *Carry*, *Zero*, *Overflow*, y otras, que reflejan el resultado de la operación.
