---
created: 2025-06-12 11:48:54
modified: 2025-06-13 01:54:46
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

- [[Espectro]] de la [[Señal]]: se busca evitar altas [[Frecuencia|Frecuencias]] y la [[Componente continua]], y también es deseable que la potencia transmitida esté en la parte central del [[Ancho de banda]]
- [[Sincronización]]
- [[Detección de errores]]
- Inmunidad al [[Ruido]] e interferencias
- Coste y complejidad: cuanto mayor es la [[Velocidad de modulación]] para una [[Velocidad de transmisión]] dada, mayor es el coste

Se introducen las [[Técnicas de aleatorización]]:

- [[B8ZS]]
- [[HDB3]]

## 5.2. Datos digitales, señales analógicas

Se analiza la conversión digital-analógica mediante [[Modulación]]: [[ASK]], [[FSK]] y [[PSK]], junto con sus variantes más importantes ([[BFSK]], [[MFSK]], [[BPSK]], [[DPSK]], [[QPSK]], [[OQPSK]] y [[MPSK]]). Se introduce también la [[QAM]], que combina [[PSK]] y [[ASK]].

Se comparan prestaciones:

- [[Ancho de banda]]
- Eficiencia del [[Ancho de banda]]
- [[Cociente EbNo]] y [[Bit Error Rate]]

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
