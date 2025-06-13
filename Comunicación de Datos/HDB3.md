---
aliases:
  - High Density Bipolar-3 Zeros
created: 2025-06-12 12:31:20
modified: 2025-06-13 00:58:03
title: HDB3
---

# HDB3

Igual que el [[Bipolar-AMI]], excepto que cualquier [[Lógica y Estructuras Discretas/Cadena|Cadena]] de cuatro ceros se reemplaza por una [[Lógica y Estructuras Discretas/Cadena|Cadena]] que contiene una violación de código.

El reemplazo de la secuencia de ceros se realiza en base al número de pulsos bipolares desde la última sustitución:

| Polaridad del pulso anterior | Impar  | Par    |
| ---------------------------- | ------ | ------ |
| $-$                          | $000-$ | $+00+$ |
| $+$                          | $000+$ | $-00-$ |

![[Técnicas de aleatorización#^scrambling]]
