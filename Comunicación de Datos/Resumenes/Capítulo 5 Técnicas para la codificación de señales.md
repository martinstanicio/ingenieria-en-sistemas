---
created: 2025-06-12 11:48:54
modified: 2025-06-12 11:50:32
title: "Capítulo 5: Técnicas para la codificación de señales"
---

# Capítulo 5: Técnicas para la codificación de señales

## 5.1. Datos digitales, señales digitales

Se estudian distintos esquemas de codificación para convertir datos digitales en señales digitales. Se introduce la terminología básica:

- [[Velocidad de modulación]]
- [[Elemento de señal]]
- Señales [[unipolares]] y [[polares]]
- [[Marca]] y [[espacio]]

Se detallan varias técnicas de codificación:

- [[NRZ-L]] (No retorno a nivel cero): niveles fijos para 0 y 1.
- [[NRZI]] (No retorno a cero invertido): transición para 1, sin cambio para 0.
- [[AMI]] (Bipolar-AMI): 1 alterna polaridad, 0 sin señal.
- [[Pseudoternario]]: 0 alterna polaridad, 1 sin señal.
- [[Manchester]]: transición en mitad del bit, bajo-alto (1), alto-bajo (0).
- [[Manchester diferencial]]: siempre hay transición en el medio; codificación diferencial.

Se discuten aspectos clave para evaluar esquemas:

- [[Espectro de la señal]]
- [[Sincronización]]
- [[Detección de errores]]
- [[Inmunidad al ruido e interferencias]]
- [[Coste y complejidad]]

Se introducen las [[técnicas de aleatorización]]:

- [[B8ZS]] (Bipolar with 8-Zeros Substitution): reemplaza 8 ceros por patrones con violaciones.
- [[HDB3]] (High Density Bipolar-3 Zeros): reemplaza 4 ceros según reglas dependientes de polaridad y cantidad de pulsos.

## 5.2. Datos digitales, señales analógicas

Se analiza la conversión digital-analógica mediante modulación:

- [[ASK]] (Amplitude Shift Keying): amplitud cambia según bit.
- [[FSK]] (Frequency Shift Keying): frecuencia cambia según bit.
- [[PSK]] (Phase Shift Keying): fase cambia según bit.

Variantes importantes:

- [[BPSK]]: fase de 180° entre 0 y 1.
- [[DPSK]]: codificación diferencial, cambio relativo de fase.
- [[QPSK]]: 2 bits por símbolo, desplazamientos de 90°.
- [[OQPSK]]: versión de QPSK con desfase en la secuencia Q.
- [[MPSK]] y [[MFSK]]: versiones multinivel.

Se introduce también la [[QAM]] (Quadrature Amplitude Modulation), que combina PSK y ASK.

Se comparan prestaciones:

- [[Ancho de banda]] (BT)
- [[Eficiencia del ancho de banda]]
- [[Eb/N0]] y [[BER]] (Bit Error Rate)

## 5.3. Datos analógicos, señales digitales

Se describe la [[digitalización]] de señales analógicas:

- [[PCM]] (Pulse Code Modulation): muestreo + cuantificación.
    - Uso del [[Teorema de muestreo]].
    - [[Ruido de cuantificación]]
    - Codificación [[lineal]] y [[no lineal]] (compresión-expansión)
- [[DM]] (Delta Modulation): aproxima mediante una función escalera.
    - [[Tamaño del paso]] (d)
    - [[Frecuencia de muestreo]]

## 5.4. Datos analógicos, señales analógicas

Se repasan técnicas de modulación analógica:

- [[AM]] (Modulación de Amplitud)
- [[FM]] (Modulación de Frecuencia)
- [[PM]] (Modulación de Fase)

Se menciona la [[multiplexación por división en frecuencia]] (FDM) para transmitir múltiples señales sobre un mismo medio.
