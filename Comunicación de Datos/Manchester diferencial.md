---
aliases:
  - Differential manchester
created: 2025-06-12 12:30:08
modified: 2025-06-12 16:34:02
title: Manchester diferencial
---

# Manchester diferencial

Una técnica de [[Codificación digital]] similar a [[Manchester]], pero con la diferencia de que utiliza [[Codificación diferencial]].

> [!important]
> En esta codificación, la transición en el medio del intervalo del [[Bit]] es utilizada solo para la [[Sincronización]].

La [[Dato|Datos]] se codifican utilizando la [[Codificación diferencial]]: un $0$ se representa por la presencia de una transición al principio del intervalo del [[Bit]], y un $1$ mediante su ausencia.

![[manchester-diferencial.jpg]]

> [!warning]
> Al igual que [[Manchester]], requiere un [[Ancho de banda]] mayor que los [[Códigos NRZ]] y [[Códigos multinivel|Multinivel]].

> [!note]
> Al igual que [[Manchester]], permite la [[Detección de errores]] mediante la ausencia de una transición en el intervalo del [[Bit]].
