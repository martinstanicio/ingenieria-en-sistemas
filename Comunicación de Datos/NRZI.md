---
aliases:
  - No retorno a cero invertido
  - Nonreturn to zero inverted
created: 2025-06-12 12:29:08
modified: 2025-06-12 12:29:28
title: NRZI
---

# NRZI

Es una **variante** de la codificación [[NRZ]]. Al igual que [[NRZ-L]], [[NRZI]] mantiene un **nivel de tensión constante** durante toda la duración del [[Bit]]. La información se codifica mediante la **presencia o ausencia de una transición de la señal** al comienzo del intervalo del [[Bit]].

- Una **transición** (de bajo a alto o de alto a bajo) al principio del intervalo del [[Bit]] indica un **1 binario**.
- La **ausencia de transición** indica un **0 binario**.

[[NRZI]] es un ejemplo de **codificación diferencial**. En la codificación diferencial, la información transmitida se representa en términos de los **cambios entre elementos de señal sucesivos**, en lugar de los elementos de señal en sí mismos. Esto significa que, si el bit actual es un 0 binario, la señal se codifica igual que el bit anterior; si es un 1 binario, la señal se codifica de forma diferente a la utilizada para el bit precedente.

Una ventaja de este esquema es que, en presencia de [[Ruido]], puede ser **más seguro detectar una transición** que comparar un valor con un umbral. Además, en un [[Sistema de transmisión]] complejo, como una línea de [[Par trenzado]], [[NRZI]] es robusto a la inversión de polaridad de la señal, lo cual no ocurre en [[NRZ-L]] donde una inversión accidental de cables cambiaría todos los 1s por 0s y viceversa.

![[nrzi.jpg]]

> [!warning] La principal limitación de las señales [[NRZ]], incluyendo [[NRZI]], es la presencia de una **[[Componente continua]]**. Además, [[NRZI]] carece de capacidad de [[Sincronización]] cuando hay una **cadena larga de ceros**. En estas condiciones, la salida es una tensión constante durante un período prolongado, lo que puede provocar una **pérdida de [[Sincronización]]** entre los relojes del [[Emisor]] y el [[Receptor]] si hay desajustes.
> 
> A diferencia de [[NRZ-L]] (que pierde [[Sincronización]] con cadenas largas de ceros o unos), [[NRZI]] sí introduce transiciones con cadenas largas de unos (la tasa de transición normalizada es 1.0 para todo 1, y 0 para todo 0).

Debido a su sencillez y a las características de su respuesta en frecuencias relativamente bajas, los códigos [[NRZ]] se utilizan comúnmente en las **grabaciones magnéticas digitales**. Sin embargo, sus limitaciones (como la componente continua y problemas de sincronización en ciertos casos) los hacen **poco atractivos para aplicaciones de transmisión de señales**.

En las [[Redes LAN]] de alta velocidad, como **100BASE-X** y **FDDI**, se emplea un esquema que combina el código **4B/5B** con [[NRZI]] (denominado 4B/5B-NRZI). Este esquema fue elegido porque el código 4B/5B garantiza la presencia de transiciones para la [[Sincronización]], siendo más eficiente que la codificación [[Manchester]] (logrando un 80% de eficiencia frente al 50% de [[Manchester]]). Después, el código 4B/5B se codifica con [[NRZI]] para aprovechar las ventajas de la **codificación diferencial** y mejorar la fiabilidad en la recepción. La mayor parte de la energía de la señal [[NRZI]] se concentra entre la componente continua y la mitad de la velocidad de transmisión.