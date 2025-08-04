---
created: 2025-08-02 13:50:05
modified: 2025-08-03 20:37:34
title: "Capítulo 6: Técnicas de comunicación de datos digitales"
---

# Capítulo 6: Técnicas de comunicación de datos digitales

## 6.1. Transmisión asíncrona y síncrona

Se presentan dos formas de [[Transmisión]] de [[Dato|Datos]]: la [[Transmisión asíncrona]] y la [[Transmisión síncrona]].

En la [[Transmisión asíncrona]], los [[Dato|Datos]] se envían carácter por carácter, utilizando [[Bit|Bits]] adicionales de control, como el [[Bit de inicio]], el [[Bit de parada]] y, opcionalmente, el [[Bit de paridad]]. Esta técnica no requiere que el [[Emisor]] y el [[Receptor]] mantengan una [[Sincronización]] constante.

En la [[Transmisión síncrona]], los [[Dato|Datos]] se envían como [[Bloque de datos]], sin [[Bit|Bits]] de control por carácter, pero se necesita [[Sincronización]] permanente entre [[Emisor]] y [[Receptor]].

## 6.2. Tipos de errores

Durante la [[Transmisión]] de [[Dato|Datos]] pueden producirse errores que alteren uno o más [[Bit|Bits]] de una secuencia. Se distingue entre [[Error aislado]] y [[Ráfaga de errores]].
## 6.3. Detección de errores

Se presentan técnicas de [[Detección de errores]] que permiten identificar si una secuencia de datos ha sido alterada durante la transmisión, sin necesidad de corregirla en el momento.

Una técnica simple consiste en agregar un [[Bit de paridad]] al final de cada carácter, de modo que el número total de bits 1 sea par (paridad par) o impar (paridad impar). Aunque simple, esta técnica solo permite detectar un número impar de errores por carácter.

Otra técnica es la [[Verificación de redundancia longitudinal]] (LRC), que organiza los datos en una [[Matriz de bits]] y agrega una fila adicional calculada por [[Bit de paridad]] en cada columna, mejorando la capacidad de detección frente a ráfagas de errores cortas.

Finalmente, se introduce la [[Verificación de redundancia cíclica]] (CRC), una técnica más robusta que representa la secuencia de datos como un polinomio binario y la divide por un [[Polinomio generador]], usando [[División módulo 2]]. El [[Residuo]] de esta división se transmite como [[Secuencia de verificación]]. El receptor repite la operación para verificar la integridad de los datos.

## 6.4. Corrección de errores

Para la [[Corrección de errores]] se agregan [[Bits de verificación]] a la secuencia transmitida, permitiendo al receptor no solo detectar, sino también corregir errores sin necesidad de retransmisión. Se presenta el [[Código de Hamming]], que permite detectar y corregir errores simples, y detectar errores dobles. Este código se basa en el concepto de [[Distancia de Hamming]], que mide el número de bits diferentes entre dos cadenas binarias. La cantidad de [[Número de bits de verificación]] necesarios depende de la longitud del mensaje y de la capacidad de corrección deseada.

Como alternativa a la corrección directa, se presenta la [[Retransmisión automática]] (ARQ), en la que el receptor solicita una retransmisión en caso de detectar errores. Se describen tres variantes: [[Stop and wait]], donde el emisor espera una confirmación antes de enviar la siguiente trama; [[Go back N]], donde se pueden enviar varias tramas antes de recibir confirmación, pero se deben retransmitir todas en caso de error; y [[Selective reject]], donde solo se retransmiten las tramas erróneas.

## 6.5. Configuraciones de línea

Se describen las distintas [[Configuraciones de línea]] posibles en una red de transmisión. La configuración [[Punto a punto]] conecta un emisor y un receptor en forma exclusiva. En cambio, la configuración [[Multipunto]] permite que varios dispositivos compartan un mismo canal de transmisión, aunque solo uno puede transmitir a la vez.

Además, según la [[Direccionalidad de la transmisión]], se clasifican los sistemas como [[Simplex]] (transmisión en una sola dirección), [[Semidúplex]] (transmisión en ambas direcciones, pero no simultáneamente) y [[Dúplex completo]] (transmisión simultánea en ambas direcciones).

## 6.6. Interfaces

Se introduce el concepto de [[Interfaz de comunicación]] entre un [[DTE]] (Equipo terminal de datos) y un [[DCE]] (Equipo de comunicación de datos), que define la forma en que ambos dispositivos se conectan e intercambian información.

Las interfaces se caracterizan por:

- Sus [[Características mecánicas]]: como el tipo de conector y la cantidad de pines.
- Sus [[Características eléctricas]]: como los niveles de tensión requeridos para representar los bits.
- Sus [[Características funcionales]]: que describen la función de cada señal.
- Sus [[Características de procedimiento]]: que definen cómo se intercambian las señales en tiempo.

Se mencionan algunos estándares comunes de interfaz, como [[RS-232]], [[V.24]], [[V.35]] y [[X.21]].
