---
created: 2025-06-12 11:48:54
modified: 2025-06-14 15:37:45
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
- [[Eficiencia del ancho de banda]]
- [[Cociente EbNo]] y [[Bit Error Rate]]

## 5.3. Datos analógicos, señales digitales

Se describe la [[Digitalización]] de [[Dato analógico|Datos analógicos]]: [[PCM]] y [[Modulación delta]], junto con sus conceptos relacionados ([[Teorema de muestreo]], [[Error de cuantización]], [[Codificación no lineal]] y [[Companding]])

## 5.4. Datos analógicos, señales analógicas

Se repasan técnicas de [[Modulación]] analógica:

- [[Modulación de amplitud]]
- [[Modulación angular]] ([[Modulación de frecuencia]] y [[Modulación de fase]])

Se menciona la [[FDM|Multiplexación por división en frecuencia]] para transmitir múltiples [[Señal|Señales]] sobre un mismo [[Comunicación de Datos/Medio|Medio]].

> [!danger]
> FALTA COMPLETAR LOS SIGUIENTES CONCEPTOS CON MÁS INFORMACIÓN.
> 
> - [[Modulación de amplitud]]
> - [[Modulación angular]]
> - [[Modulación de frecuencia]]
> - [[Modulación de fase]]
> - [[Multiplexación]]
> - [[FDM]]
> - [[TDM]]
