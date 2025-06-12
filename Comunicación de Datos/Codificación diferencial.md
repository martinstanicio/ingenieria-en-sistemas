---
aliases:
  - Codificaciones diferenciales
created: 2025-06-12 12:32:23
modified: 2025-06-12 14:43:55
title: Codificación diferencial
---

# Codificación diferencial

Es una técnica para codificar [[Dato digital|Datos digitales]] en una [[Señal digital]] o [[Señal analógica|Analógica]], donde la [[Información]] transmitida se representa mediante ==variaciones== entre [[Elemento de señal|Elementos de señal]] ==sucesivos==. Por ejemplo:

- Si el [[Bit]] actual es un $0$, la [[Señal]] se codifica con el ==mismo nivel de tensión== que el [[Bit]] anterior.
- Si el [[Bit]] actual es un $1$, la [[Señal]] se codifica con un nivel de tensión ==diferente== al del [[Bit]] anterior.

> [!note]
> Una de sus principales ventajas es que resulta más fiable **detectar una transición** en presencia de [[Ruido]], que comparar un valor con un umbral fijo.

> [!important]
> Cuando se utiliza una [[Codificación diferencial]], es necesario que el [[Emisor]] y el [[Receptor]] decidan cuál será el [[Bit]] que simulará ser *el anterior* al primer [[Bit]] de los [[Dato digital|Datos digitales]] que se busca transmitir.
