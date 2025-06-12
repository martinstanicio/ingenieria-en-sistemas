---
created: 2025-06-12 11:48:54
modified: 2025-06-12 15:26:31
title: "Capítulo 5: Técnicas para la codificación de señales"
---

# Capítulo 5: Técnicas para la codificación de señales

## 5.1. Datos digitales, señales digitales

Se introduce la terminología básica:

- [[Velocidad de modulación]]
- [[Elemento de señal]]
- [[Señal unipolar|Señales unipolares]] y [[Señal polar|Polares]]

> [!note]
> Además, a veces se utilizan los términos **marca** y **espacio** para referirse a los dígitos binarios $1$ y $0$ respectivamente.

Se estudian distintos esquemas de [[Codificación digital]] para convertir [[Dato digital|Datos digitales]] en [[Señal digital|Señales digitales]]

- [[Códigos NRZ]] ([[NRZ-L]] y [[NRZI]])
- [[Códigos multinivel]] ([[Bipolar-AMI]] y [[Pseudoternaria]])
- [[Códigos autosincronizados]] ([[Manchester]] y [[Manchester diferencial]])

Se discuten aspectos clave para evaluar esquemas:

- [[Espectro de la señal]]
- [[Sincronización]]
- [[Detección de errores]]
- [[Inmunidad al ruido e interferencias]]
- [[Coste y complejidad]]

Se introducen las [[Técnicas de aleatorización]]:

- [[B8ZS]]
- [[HDB3]]

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
