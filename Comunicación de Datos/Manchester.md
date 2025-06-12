---
created: 2025-06-12 12:30:43
modified: 2025-06-12 16:14:31
title: Manchester
---

# Manchester

Una técnica de [[Codificación digital]] que se caracteriza por ==siempre tener una transición== en la mitad del intervalo de duración de un [[Bit]].

> [!important]
> El hecho de que existe esta transición periódica, permite que la codificación [[Manchester]] brinde al [[Receptor]] una [[Sincronización]] constante.
> 
> Además, permite la detección de errores, cuando el [[Receptor]] detecta la ausencia de esta transición.

Además, esta transición sirve para transmitir los [[Dato|Datos]], pues una transición de bajo a alto representa un $1$, y una transición de alto a bajo representa $0$.

![[manchester.jpg]]

> [!warning]
> La principal desventaja del código [[Manchester]] es que la [[Velocidad de modulación]] **máxima** es el doble que en los [[Códigos NRZ]], por lo que requiere un [[Ancho de banda]] mayor que los [[Códigos NRZ]] y los [[Códigos multinivel]].
> 
> Esta característica se traduce en una ==eficiencia de solo el 50%==.

> [!note]
> [[Manchester]] no genera una [[Componente continua]] en la [[Señal]] resultante.
