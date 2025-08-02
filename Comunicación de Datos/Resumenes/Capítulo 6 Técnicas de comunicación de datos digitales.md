---
created: 2025-08-02 13:50:05
modified: 2025-08-02 13:50:42
title: "Capítulo 6: Técnicas de comunicación de datos digitales"
---

# Capítulo 6: Técnicas de comunicación de datos digitales

## 6.1. Transmisión asíncrona y síncrona

Se presentan dos formas de [[Transmisión de datos]]: la [[Transmisión asíncrona]], en la que los datos se envían carácter por carácter con bits adicionales de control; y la [[Transmisión síncrona]], en la que los datos se agrupan en bloques más grandes, requiriendo sincronización entre emisor y receptor.

Conceptos mencionados:

- [[Bit de inicio]]
- [[Bit de parada]]
- [[Bit de paridad]]
- [[Temporización]]
- [[Bloque de datos]]
- [[Sincronización de reloj]]

## 6.2. Tipos de errores

Se analizan los distintos tipos de [[Error de transmisión]] que pueden producirse durante la [[Transmisión de datos]]:

- [[Error aislado]]
- [[Ráfaga de errores]]

También se menciona la [[Tasa de error de bits]], como medida para evaluar la calidad de una línea de transmisión.

## 6.3. Detección de errores

Se presentan varias técnicas para la [[Detección de errores]], basadas en el uso de información redundante:

- [[Bit de paridad]]: se utiliza [[Paridad par]] o [[Paridad impar]]
- [[Verificación de redundancia longitudinal]] ([[LRC]])
- [[Verificación de redundancia cíclica]] ([[CRC]])

Otros conceptos utilizados:

- [[Matriz de bits]]
- [[Polinomio generador]]
- [[División módulo 2]]
- [[Secuencia de verificación]]

## 6.4. Corrección de errores

Se introduce la [[Corrección de errores]] mediante el agregado de [[Bit de verificación]] en posiciones específicas. Se menciona el uso del [[Código de Hamming]] como técnica capaz de detectar y corregir errores simples.

También se incluyen esquemas basados en [[Retransmisión automática]] ([[ARQ]]):

- [[Stop and wait]]
- [[Go back N]]
- [[Selective reject]]

Conceptos relacionados:

- [[Distancia de Hamming]]
- [[Número de bits de verificación]]
- [[Detección de errores simples]]
- [[Corrección de errores simples]]
- [[Errores múltiples]]

## 6.5. Configuraciones de línea

Se describen diferentes formas de organización de los dispositivos en una [[Configuración de línea]]:

- [[Punto a punto]]
- [[Multipunto]]

También se clasifican según la [[Direccionalidad de la transmisión]]:

- [[Simplex]]
- [[Semidúplex]]
- [[Dúplex completo]]

## 6.6. Interfaces

Se introduce el concepto de [[Interfaz de comunicación]] entre un [[DTE]] (equipo terminal de datos) y un [[DCE]] (equipo de comunicación de datos).

Se describen sus distintas características:

- [[Características mecánicas]]
- [[Características eléctricas]]
- [[Características funcionales]]
- [[Características de procedimiento]]

Ejemplos de interfaces estandarizadas:

- [[RS-232]]
- [[V.24]]
- [[V.35]]
- [[X.21]]
