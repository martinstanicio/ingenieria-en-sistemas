---
aliases:
  - Differential manchester
created: 2025-06-12 12:30:08
modified: 2025-06-12 15:41:31
title: Manchester diferencial
---

# Manchester diferencial

Una técnica de [[Codificación digital]] similar a [[Manchester]], pero con la diferencia de que utiliza [[Codificación diferencial]].

> [!note]
> En esta codificación, la transición en el medio del intervalo del [[Bit]] es utilizada solo para la [[Sincronización]].

La [[Dato|Datos]] se codifican utilizando la [[Codificación diferencial]]: un $0$ se representa por la presencia de una transición al principio del intervalo del [[Bit]], y un $1$ mediante su ausencia.

![[manchester-diferencial.jpg]]

> [!warning]
> Al igual que [[Manchester]], requiere un [[Ancho de banda]] mayor que los [[Códigos NRZ]] y [[Códigos multinivel|Multinivel]].

A pesar de sus requisitos de [[ancho de banda]] más elevados, el código Manchester Diferencial ofrece ventajas significativas. Una de ellas es la **ausencia de [[Componente continua]]** (o componente DC) en la [[Señal]], lo cual es beneficioso para la transmisión. Además, proporciona una capacidad integrada de **[[Detección de errores]]**. Un error puede detectarse si no se encuentra la transición esperada en la mitad del intervalo, ya que para que un error pasara desapercibido, el [[Ruido]] tendría que invertir la [[Señal]] tanto antes como después de la transición. El código Manchester Diferencial ha sido elegido en la norma **IEEE 802.5 para redes [[LAN]] en anillo con paso de testigo**, donde se utilizan pares trenzados apantallados.
