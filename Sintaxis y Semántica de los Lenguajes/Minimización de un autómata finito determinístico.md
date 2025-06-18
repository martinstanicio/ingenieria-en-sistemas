---
aliases:
  - Minimización de un AFD
created: 2025-06-18 01:10:13
modified: 2025-06-18 01:36:12
title: Minimización de un autómata finito determinístico
---

# Minimización de un autómata finito determinístico

El proceso de minimización de un [[Autómata finito determinístico]] consiste de los siguientes pasos:

1. Calcular y eliminar [[Estado no accesible|Estados no accesibles]]
2. Calcular los [[Indistinguibilidad|Estados indistinguibles]] y dejar un único [[Lógica y Estructuras Discretas/Estado|Estado]] por cada clase de [[Relación de equivalencia|Equivalencia]]
3. Eliminar de la [[Función de transición]] aquellas transiciones que hacen referencia a [[Lógica y Estructuras Discretas/Estado|Estados]] ya eliminados
