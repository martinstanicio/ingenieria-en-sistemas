---
aliases:
  - Amplitude Modulation
  - Modulación de amplitud
created: 2025-06-13 11:41:10
modified: 2025-06-13 12:41:05
title: AM
---

# AM

Es la forma más sencilla de [[Modulación]], donde la [[Amplitud]] de la onda portadora varía de acuerdo con alguna característica de la [[Señal analógica]] modulante.

$$
s \left( t \right) = \left( 1 + n_a \cdot x\left( t \right) \right) \cos \left( 2 \pi f_c t \right)
$$

- $s \left( t \right)$: [[Señal]] modulada en el tiempo
- $\cos \left( 2 \pi f_c t \right)$: onda portadora normalizada a la [[Amplitud]] unidad
- $x \left( t \right)$: [[Señal]] de [[Entradas|Entrada]] normalizada a la [[Amplitud]] unidad
- $n_a = A_x / A_c$: índice de [[Modulación]], que es el cociente entre la [[Amplitud]] de la [[Señal]] de [[Entradas|Entrada]] y la portadora

> [!note]
> El término $1$ en la ecuación es una [[Componente continua]] que previene la pérdida de [[Información]].

> [!danger]
> Si $n_a < 1$, la envolvente será una reproducción **exacta** de la [[Señal]] original, pero si $n_a > 1$, la envolvente cruzará el eje de tiempos, perdiéndose así [[Información]].

![[am.jpg]]

> [!important]
> Este proceso permite que la [[Señal]] se transmita a una [[Frecuencia]] más alta, lo cual es necesario para una [[Transmisión]] efectiva en [[Comunicación de Datos/Medio|Medios]] como las [[Ondas de radio]], donde las [[Antena|Antenas]] requerirían tamaños imprácticos para [[Señal|Señales]] de baja [[frecuencia]].
> 
> También posibilita la [[Multiplexación]].

- **Espectro de la Señal AM**:
    
    - El espectro de una señal AM está compuesto por la **portadora original** y dos componentes adicionales que son el espectro de la señal de entrada trasladado a la frecuencia de la portadora.
    - Estas componentes adicionales se conocen como **banda lateral superior** (para frecuencias mayores que la portadora) y **banda lateral inferior** (para frecuencias menores que la portadora).
    - Tanto la banda superior como la inferior son réplicas exactas del espectro original de la señal moduladora, con la banda inferior invertida en frecuencias.
    - AM es un **proceso lineal** que produce frecuencias correspondientes a la suma y diferencia de la portadora y las componentes de la señal moduladora.
    - El **ancho de banda (BT)** requerido para una señal AM es generalmente **el doble del ancho de banda (B) de la señal original** (BT = 2B). Por ejemplo, una señal de voz con un espectro de 300 a 3000 Hz, modulada sobre una portadora de 60 kHz, resultaría en una banda superior entre 60.3 y 63 kHz y una banda inferior entre 57 y 59.7 kHz, además de la portadora de 60 kHz.
- **Potencia Transmitida**:
    
    - La potencia total transmitida (Pt) en una señal AM es la suma de la potencia de la portadora (Pc) y la potencia de las bandas laterales. Se expresa como **Pt = Pc(1 + n²a/2)**.
    - Es deseable que el índice de modulación **na sea lo más grande posible (pero sin exceder 1)** para que la mayor parte de la potencia de la señal transmitida se utilice para transportar información.
- **Variantes de AM**:
    
    - **AM de Banda Lateral Única (SSB - Single Sideband)**: Transmite solo una de las bandas laterales, eliminando la otra y la portadora. Sus ventajas principales son que necesita **la mitad del ancho de banda** (BT = B) y **menos potencia**.
    - **Doble Banda Lateral con Portadora Suprimida (DSBSC - Double Sideband Suppressed Carrier)**: Se filtra la frecuencia portadora y se transmiten ambas bandas laterales. Ahorra potencia, pero utiliza el mismo ancho de banda que la AM convencional (DSBTC).
    - **Banda Lateral Residual (VSB - Vestigial Sideband)**: Es una técnica de compromiso que utiliza una de las bandas laterales y una portadora de potencia reducida. Esto es útil para la sincronización.
    - La supresión de la portadora, aunque ahorra potencia y/o ancho de banda, puede dificultar la sincronización en el receptor, ya que la portadora constante proporciona un mecanismo de temporización para la llegada de los bits.
