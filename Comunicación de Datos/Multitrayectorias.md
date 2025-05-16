---
created: 2025-05-16 12:08:26
modified: 2025-05-16 12:14:56
title: Multitrayectorias
---
# Multitrayectorias

Las **multitrayectorias** son un fenómeno que se presenta cuando la [[Señal]] transmitida desde el [[Emisor]] sigue ==múltiples caminos== hasta llegar al [[Receptor]].

![[multitrayectorias.jpg]]

Los textos describen varios mecanismos que contribuyen a las multitrayectorias:

- **Reflexión (R)**: Ocurre cuando la señal incide sobre una superficie grande en comparación con su longitud de onda [Conversación anterior]. En transmisiones superficiales, la señal puede reflejarse en la **superficie terrestre** o en **estructuras artificiales o accidentes topográficos** en el caso de comunicaciones móviles. Una reflexión en la tierra puede causar una alta pérdida debido a un desplazamiento de fase de 180° que tiende a cancelar la onda directa [Conversación anterior].
- **Refracción**: En las microondas fijas, además de la trayectoria visual directa, la señal puede seguir una **trayectoria curva a través de la atmósfera** debido a la refracción, contribuyendo también a las multitrayectorias.
- **Dispersión (S)**: Se refiere a la producción de ondas con dirección o frecuencia modificadas cuando inciden sobre materia. En entornos urbanos sin línea de visión clara, la dispersión es una fuente principal de problemas de recepción [Conversación anterior].
- **Difracción (D)**: Permite la recepción de señales incluso sin una trayectoria visual libre de obstáculos, y contribuye a las multitrayectorias, especialmente en entornos urbanos [Conversación anterior].

Las consecuencias de las multitrayectorias incluyen:

- **Interferencia**: Las ondas reflejadas o dispersas pueden interferir **constructiva o destructivamente** en el receptor [Conversación anterior, 26]. Esto se conoce como **desvanecimiento multitrayectoria**.
- **Dispersión del retardo**: Debido a las diferentes longitudes de los múltiples caminos, las componentes de la señal llegan en **diferentes momentos** al receptor. Esto se llama **dispersión del retardo de propagación multitrayectoria**. Esta dispersión temporal puede limitar la velocidad a la que los datos pueden ser correctamente recibidos [Conversación anterior, relacionada con la distorsión en fibra óptica, pero el principio aplica].

Las multitrayectorias son una de las **dificultades específicas** de la transmisión inalámbrica siguiendo la **trayectoria visual (LOS)** [Conversación anterior], y son un factor importante en los entornos móviles inalámbricos. Se mencionan técnicas para compensar los errores y distorsiones introducidos por el desvanecimiento multitrayectoria, como la corrección de errores hacia adelante, la ecualización adaptativa y las técnicas de **diversidad**. El uso de **celdas más pequeñas (microceldas)** en redes celulares puede proporcionar condiciones de propagación superiores, lo que implica una menor dispersión del retardo medio de propagación multitrayectoria.
