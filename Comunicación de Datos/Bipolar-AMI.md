---
aliases:
  - AMI
created: 2025-06-12 12:30:08
modified: 2025-06-12 15:09:40
title: Bipolar-AMI
---

# Bipolar-AMI

Técnica de [[Codificación digital]], que se caracteriza por generar [[Señal|Señales]] con ==tres niveles de tensión==:

- Un $0$ se representa por la ausencia de [[Señal]] (tensión nula)
- Un $1$ se representa como un pulso de una tensión determinada, que ==alterna su polaridad== con cada iteración.

![[bipolar-ami.jpg]]

> [!note]
> Gracias a que se alterna la polaridad de los pulsos para los $1$, no hay una [[Componente continua]] en la [[Señal]] resultante.

> [!warning]
> Aunque [[Bipolar-AMI]] permite la [[Sincronización]] frente a [[Lógica y Estructuras Discretas/Cadena|Cadenas]] largas de unos, una [[Lógica y Estructuras Discretas/Cadena|Cadena]] larga de ceros sigue siendo un pulso de tensión constante, que no es posible [[Sincronización|Sincronizar]].

 Además, los códigos binarios multinivel como [[Bipolar-AMI]] **no son tan eficaces como los [[NRZ]]**. Para lograr la misma probabilidad de error, una señal [[Bipolar-AMI]] requiere aproximadamente **3 dB más de potencia** que las señales bivaluadas (como [[NRZ-L]]). Esto implica que, para una [[Relación señal-ruido|relación señal-ruido]] dada, la [[Tasa de errores por bit|tasa de errores por bit]] es significativamente mayor en [[Bipolar-AMI]].

> [!important]
> La alternancia de los pulsos permite la ==detección de errores==, ya que, si se invierte una cantidad de [[Bit|Bits]] impar, causará una violación de la [[Codificación digital|Codificación]] romperá la secuencia alternante. Un error aislado, ya sea que elimine o añada un pulso, causará una violación de esta propiedad, lo que permitirá al receptor detectarlo.
