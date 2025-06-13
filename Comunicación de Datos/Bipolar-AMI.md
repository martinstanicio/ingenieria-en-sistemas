---
aliases:
  - AMI
created: 2025-06-12 12:30:08
modified: 2025-06-13 00:44:54
title: Bipolar-AMI
---

# Bipolar-AMI

Técnica de [[Codificación digital]], que se caracteriza por generar [[Señal|Señales]] con ==tres niveles de tensión==:

- Un $0$ se representa por la ausencia de [[Señal]] (tensión nula)
- Un $1$ se representa como un pulso de una tensión determinada, que ==alterna su polaridad== con cada iteración.

> [!note]
> Gracias a que se alterna la polaridad de los pulsos para los $1$, no hay una [[Componente continua]] en la [[Señal]] resultante.

![[bipolar-ami.jpg]]

> [!warning]
> Aunque [[Bipolar-AMI]] permite la [[Sincronización]] frente a [[Lógica y Estructuras Discretas/Cadena|Cadenas]] largas de unos, una [[Lógica y Estructuras Discretas/Cadena|Cadena]] larga de ceros sigue siendo un pulso de tensión constante, que no es posible [[Sincronización|Sincronizar]].

> [!important]
> La alternancia de los pulsos permite la [[Detección de errores]], ya que, si se invierte una cantidad de [[Bit|Bits]] impar, causará una violación de la [[Codificación digital|Codificación]], pues romperá la secuencia alternante de pulsos.
