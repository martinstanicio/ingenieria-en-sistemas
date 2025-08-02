---
created: 2025-08-02 13:54:43
modified: 2025-08-02 13:55:03
title: "Capítulo 7: Protocolos de control del enlace de datos"
---
# Capítulo 7: Protocolos de control del enlace de datos

## 7.1. Control de flujo

Se introduce el concepto de [[Control de flujo]], necesario para evitar la saturación del receptor ante una transmisión muy rápida del emisor. Se describe el mecanismo de [[Ventana deslizante]] como técnica para regular el envío de tramas.

Conceptos mencionados:

- [[Receptor]]
- [[Emisor]]
- [[Trama]]
- [[Buffer]]
- [[Ventana]]
- [[Reconocimiento]] (acknowledgement)
- [[Temporizador]]

## 7.2. Control de errores

Se amplía el tratamiento del [[Control de errores]] incorporando mecanismos de detección y recuperación mediante [[Retransmisión automática]] ([[ARQ]]). Se describen tres técnicas principales:

- [[Stop and wait ARQ]]
- [[Go-back-N ARQ]]
- [[Selective reject ARQ]]

Se utilizan números de secuencia para las tramas, así como [[Temporizadores]] para gestionar las retransmisiones.

Conceptos relacionados:

- [[Número de secuencia]]
- [[Trama reconocida]]
- [[Trama perdida]]
- [[Retransmisión]]
- [[Duplicación de tramas]]
- [[Trama dañada]]
- [[Temporización de reconocimiento]]

## 7.3. Control del enlace de datos de alto nivel (HDLC)

Se presenta el protocolo [[HDLC]] (High-Level Data Link Control), un protocolo de [[Nivel de enlace]] basado en bits, orientado a bit, y con funcionalidades de control de flujo y errores. Se describe su estructura de trama, modos de operación y tipos de estaciones.

Tipos de estación:

- [[Estación primaria]]
- [[Estación secundaria]]
- [[Estación combinada]]

Modos de configuración:

- [[Normal response mode]] (NRM)
- [[Asynchronous response mode]] (ARM)
- [[Asynchronous balanced mode]] (ABM)

Estructura de la [[Trama HDLC]]:

- [[Bandera]]
- [[Campo de dirección]]
- [[Campo de control]]
- [[Campo de información]]
- [[Campo FCS]] (Frame Check Sequence)

Tipos de tramas:

- [[Trama de información]] (I)
- [[Trama de supervisión]] (S)
- [[Trama no numerada]] (U)

Campo de control:

- [[N(S)]] (número de secuencia de envío)
- [[N(R)]] (número de secuencia de recepción)
- [[Código de función]]
- [[Bit P/F]] (Poll/Final)

## Apéndice 7A. Análisis de prestaciones

Se realiza un [[Análisis de prestaciones]] de los mecanismos de [[ARQ]].

Conceptos involucrados:

- [[Eficiencia de la línea]]
- [[Retardo de propagación]]
- [[Tiempo de transmisión]]
- [[Probabilidad de error]]
- [[Ventana de transmisión]]
- [[Reconocimiento acumulativo]]
