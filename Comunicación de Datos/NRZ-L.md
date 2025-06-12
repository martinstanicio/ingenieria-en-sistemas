---
aliases:
  - No retorno a nivel cero
  - Nonreturn to zero level
created: 2025-06-12 12:28:07
modified: 2025-06-12 12:42:30
title: NRZ-L
---

# NRZ-L

Es la forma más común y ==sencilla== de transmitir [[Señal digital|Señales digitales]]. Utiliza un nivel de tensión diferente para cada dígito binario, que se mantiene constante durante toda la duración del [[Bit]].

- **Limitaciones:**
    - **Componente de Corriente Continua (DC)**: La principal limitación de las señales NRZ, incluyendo NRZ-L, es la presencia de una componente de corriente continua.
    - **Falta de Capacidad de Sincronización**: Otra desventaja importante es la ausencia de capacidad de sincronización.
        - Cuando hay una **cadena larga de unos o ceros**, la salida en NRZ-L es una tensión constante durante un período prolongado.
        - En estas condiciones, cualquier desajuste entre los relojes del transmisor y el receptor puede provocar una **pérdida de sincronización** entre ambos. Esto se debe a que la ausencia de transiciones en la señal dificulta que el receptor mantenga su reloj sincronizado con el del emisor.
- **Aplicaciones y Conveniencia:**
    
    - Debido a su **sencillez y a sus características de respuesta en frecuencias relativamente bajas**, los códigos NRZ se utilizan comúnmente en las **grabaciones magnéticas digitales**.
    - Sin embargo, sus limitaciones (componente DC y problemas de sincronización) los hacen **poco atractivos para aplicaciones de transmisión de señales**.
    - La señalización NRZ-L es **habitual en la transmisión asíncrona**. En este tipo de transmisión, el estado de reposo de la línea (cuando no se transmite ningún carácter) se corresponde con la presencia de una tensión negativa.
