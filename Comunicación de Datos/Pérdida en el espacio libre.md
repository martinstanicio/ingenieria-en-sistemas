---
created: 2025-05-16 11:30:11
modified: 2025-05-16 11:55:54
title: Pérdida en el espacio libre
---

# Pérdida en el espacio libre

Es un tipo de [[Atenuación]] que ocurre en cualquier tipo de [[Medio no guiado|Medio inalámbrico]]. Se produce porque la ==[[Señal]] se dispersa con la distancia==.

> [!tip]
> A medida que una [[Señal]] transmitida se aleja de la [[Antena]] emisora, ocupa un **área cada vez mayor**. Por lo tanto, la [[Antena]] receptora recibirá menos potencia **cuanto más alejada esté**.

> [!important]
> Es la principal causa de las pérdidas en comunicaciones vía satélite.

Para la [[Antena isotrópica]], la [[Pérdida en el espacio libre]] se puede calcular de la siguiente forma.

$$
\frac{P_t}{P_r} =
\frac{\left( 4 \pi d \right)^2}{\lambda^2} =
\frac{\left( 4 \pi fd \right)^2}{c^2}
$$

- $P_t$: potencia de la [[Señal]] en la [[Antena]] emisora
- $P_r$: potencia de la [[Señal]] en la [[Antena]] receptora
- $\lambda$: [[Longitud de onda]] de la portadora
- $d$: separación entre las [[Antena|Antenas]]
- $c$: [[Rapidez de la luz|Velocidad de la luz]]

También podemos expresar la [[Pérdida en el espacio libre]] en [[Decibelio|Decibelios]]:

$$
L_{dB} =
10 \log \left( \frac{P_t}{P_r} \right)
$$

Para otro tipo de [[Antena|Antenas]], se debe tener en cuenta la [[Ganancia de una antena|Ganancia de la misma]] ($G_t$ y $G_r$) o el área efectiva ($A_t$, $A_r$).

$$
\frac{P_t}{P_r} =
\frac{\left( 4 \pi \right)^2 \left( d \right)^2}{ G_t G_r \lambda^2} =
\frac{\left( \lambda d \right)^2}{A_t A_r} =
\frac{\left( cd \right)^2}{f^2 A_t A_r}
$$

> [!important]
> La [[Pérdida en el espacio libre]] aumenta con la **distancia** $d$ y con la [[Longitud de onda]] $\lambda$; pero disminuye con la [[Frecuencia]] $f$.
