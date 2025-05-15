---
created: 2025-04-06 05:19:17
modified: 2025-05-15 14:35:35
title: "Capítulo 3: Transmisión de datos"
---

# Capítulo 3: Transmisión de datos

## 3.1. Conceptos y terminología

[[Comunicación de Datos/Medio|Medios de transmisión]] [[Medio guiado|guiados]] y [[Medio no guiado|no guiados]], [[Enlace directo]], configuraciones [[Enlace punto a punto|Punto a punto]] y [[Medio multipunto|multipunto]], y los modos de transmisión [[Simplex]] (unidireccional), [[Half-duplex]] (bidireccional por turnos) y [[Full-duplex]] (bidireccional simultaneo).

[[Señal analógica|Señales analógicas]] y [[Señal digital|digitales]], [[Señal periódica|Señales periódicas]], componentes de una onda electromagnética ([[Amplitud]], [[Frecuencia]], [[Fase]], [[Periodo]], [[Longitud de onda]]), y sus diferencias fundamentales al aplicarlas en el dominio del tiempo y de la frecuencia; características de una [[Transmisión]] ([[Espectro]], [[Ancho de banda absoluto]] y [[Ancho de banda|efectivo]], y [[Componente continua]]).

## 3.2. Transmisión de datos analógicos y digitales

### Datos analógicos y digitales

Los [[Dato analógico|Datos analógicos]] toman valores en un intervalo continuo (audio, video), y los [[Dato digital|digitales]] toman valores discretos (cadenas de texto, números enteros). Entre los ejemplos se explican conceptos varios como el barrido entrelazado para la [[Transmisión]] de video.

### Señales analógicas y digitales

Una [[Señal analógica]] es una onda electromagnética que varía continuamente, y una [[Señal digital]] es secuencia de pulsos de tensión. Los [[Dato digital|Datos digitales]] se pueden representar también mediante [[Señal analógica|Señales analógicas]], usando un [[Módem]] (modulador/demodulador); y los [[Dato analógico|Datos analógicos]] también mediante [[Señal digital|Señales digitales]], usando un [[Códec]] (codificador/decodificador).

### Transmisión analógica y digital

Tanto [[Señal analógica|Señales analógicas]] como [[Señal digital|digitales]] se pueden transmitir utilizando el [[Comunicación de Datos/Medio|Medio de transmisión]] adecuado. El alcance de la [[Transmisión analógica]] se puede extender mediante [[Amplificador|Amplificadores]], y el de la [[Transmisión digital]] mediante [[Repetidor|Repetidores]].

Se destacan las ventajas de la [[Transmisión digital]] (tecnología digital, integridad de los [[Dato|Datos]], utilización de la capacidad, seguridad y privacidad, e integración).

## 3.3. Dificultades en la transmisión

### Atenuación

La [[Energía]] de la [[Señal]] decae con la distancia. La [[Atenuación]] varía con la [[Frecuencia]], lo que puede distorsionar la [[Señal]] recibida.

### Distorsión de retardo

La velocidad de propagación de una [[Señal]] varía con la [[Frecuencia]], por lo que las componentes de [[Frecuencia]] de la [[Señal]] pueden llegar al receptor con cierto desplazamiento de [[Fase]], llamado [[Distorsión de retardo]].

### Ruido

El [[Ruido]] se clasifica en cuatro categorías:

- [[Ruido térmico|Ruido térmico o blanco]]: agitación térmica de los electrones. No se puede eliminar.
- [[Ruido de intermodulación]]: mezcla de [[Señal|Señales]] de diferentes [[Frecuencia|Frecuencias]].
- [[Diafonía]]: acoplamiento no deseado entre las líneas que transportan las [[Señal|Señales]].
- [[Ruido impulsivo]]: pulsos irregulares cortos de gran [[Amplitud]]. Difícil de mitigar.

## 3.4. Capacidad del canal

La capacidad $C$ de un canal es la velocidad máxima de [[Transmisión]] de [[Dato|Datos]] en un canal bajo condiciones dadas, como velocidad deseada, [[Ancho de banda]], [[Ruido]] y tasa de errores permitida.

### Ancho de banda de Nyquist

En un canal exento de [[Ruido]], dado un [[Ancho de banda]] $B$, la máxima velocidad de [[Transmisión]] que se puede alcanzar es $2B$. Para [[Señal|Señales]] multinivel ([[Señal digital|Señalización digital]] con $M \in \mathbb{N}$ niveles de tensión) se utiliza la formulación de [[Ancho de banda de Nyquist|Nyquist]].

$$
C = 2B \cdot \log_2 M
$$

### Fórmula para la capacidad de Shannon

Relación entre la velocidad de [[Transmisión]], el [[Ruido]] y la tasa de errores. La fórmula de Shannon define la capacidad máxima del canal en [[Bit|Bits]] por segundo, en base al [[Ancho de banda]] $B$ y la [[Relación señal-ruido]] (SNR).

$$
C = B \cdot \log_2 \left( 1 + \text{SNR} \right)
$$

### El cociente $E_b / N_0$

El [[Cociente EbNo]] es la relación entre la [[Energía]] de la [[Señal]] por [[Bit]] y la densidad de potencia del [[Ruido]] por hercio. Es más adecuado que el [[Relación señal-ruido|SNR]] para determinar las tasas de error y la velocidad de [[Transmisión]] en [[Sistemas]] de comunicación [[Transmisión digital|digital]], ya que tiene en cuenta el [[Ancho de banda]].

## Apéndice 3A: Decibelios y energía de la señal

Se destaca la importancia de la [[Energía]] de la [[Señal]] transmitida y cómo se [[Atenuación|atenúa]] al propagarse por el [[Comunicación de Datos/Medio|Medio]]. Se introduce el concepto de [[Decibelio]] ($\text{dB}$) como herramienta para medir la diferencia relativa entre dos niveles de la [[Señal]] (tanto ganancias como pérdidas). También se introducen $\text{dBW}$ (decibelio-vatio), $\text{dBm}$ (decibelio-milivatio) y $\text{dBmV}$ (decibelio-milivoltio) como medidas absolutas de potencia o tensión en [[Decibelio|Decibelios]].
