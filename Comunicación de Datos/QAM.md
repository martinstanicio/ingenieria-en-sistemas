---
aliases:
  - Quadrature Amplitude Modulation
  - Modulación de amplitud en cuadratura
created: 2025-06-13 02:20:01
modified: 2025-06-13 02:28:00
title: QAM
---

# QAM

Técnica de [[Señalización]] analógica. Puede considerarse tanto una combinación de [[Modulación]] [[ASK]] y [[PSK]], como una generalización de la [[Modulación]] [[QPSK]].

[[QAM]] aprovecha la capacidad de enviar simultáneamente dos [[Señal|Señales]] diferentes sobre la misma [[Frecuencia]] portadora, utilizando dos réplicas de la misma portadora, desplazadas entre sí 90 grados.

$$
s \left( t \right) = d_1 \left( t \right) \cos \left( 2 \pi f_c t \right) + d_2 \left( t \right) \sin \left( 2 \pi f_c t \right)
$$

![[qam.jpg]]

La entrada binaria de $R$ bps se convierte en dos flujos de [[Bit|Bits]] separados, de $R / 2$ bps cada uno, tomando [[Bit|Bits]] alternos para cada flujo. Cada uno de estos flujos se modula utilizando [[Modulación]] [[ASK]] sobre su respectiva portadora. Luego, las dos [[Señal|Señales]] moduladas independientes se suman y se transmiten.

    - En el receptor, las dos señales se **demodulan y se combinan** para reproducir la señal binaria de entrada. El demodulador QAM recupera las dos señales que, combinadas, permiten recuperar la entrada original.

- **Estados y rendimiento**:
    
    - Si se utiliza un esquema ASK con dos niveles para cada flujo, la señal combinada tendrá **4 (2x2) posibles estados de señalización**, lo cual es esencialmente QPSK.
    - Si se usa ASK con cuatro niveles de amplitud para cada flujo, la secuencia combinada podrá tomar uno de entre **16 (4x4) estados**.
    - En la práctica, se implementan sistemas con **64 o incluso 256 estados**.
    - A mayor número de estados, **mayor es la velocidad de transmisión posible para un ancho de banda dado**.
    - Sin embargo, cuanto mayor es el número de estados, **mayor será la tasa potencial de errores por bit** debido al ruido y la atenuación.
