---
aliases:
  - Campos eléctricos
created: 2025-06-28 16:30:29
modified: 2025-06-28 17:33:22
title: Campo eléctrico
---

# Campo eléctrico

El [[Campo eléctrico]] $\vec{E}$ es la influencia de una carga eléctrica $q_1$ sobre el espacio que la rodea. Específicamente, dado un punto $P$, y una ==carga de prueba== $q_0$ que experimenta una [[Fuerza]] eléctrica $\vec{F}$, el [[Campo eléctrico]] $\vec{E}$ es la [[Fuerza]] eléctrica por unidad de carga de prueba.

$$
\vec{E} = \frac{\vec{F}}{q_0}
$$

## Campo eléctrico generado por una carga puntual

Es posible calcular el [[Campo eléctrico]] $\vec{E}$ generado por una carga puntual $q_1$, en un punto determinado, a una distancia $r$ y en dirección del [[Versor]] $\hat{x}$.

$$
\vec{E} = k \cdot \frac{q_1}{r^2} \cdot \hat{x}
$$

## Campo eléctrico generado por una distribución continua de cargas

También es posible calcular el [[Campo eléctrico]] $\vec{E}$ generado por un cuerpo con una [[Distribución continua de cargas]], en un punto determinado, a una distancia $r$ y en dirección del [[Versor]] $\hat{r}$.

$$
\vec{E} = k \cdot \int \frac{dq}{r^2} \cdot \hat{r}
$$

Si es un caso de [[Densidad de carga lineal]] $\lambda$, con un cuerpo de longitud $L$, se utiliza una [[Integral|Integral simple]] con $dq = \lambda dx$:

$$
\vec{E} = k \cdot \int_L \frac{\lambda dx}{r^2} \cdot \hat{r}
$$

> [!tip]
> También es posible calcular la [[Integral]] utilizando [[Coordenadas polares]].
> 
> $$
> dq = \lambda \cdot r \cdot d \theta
> $$

Si es un caso de [[Densidad de carga superficial]] $\sigma$, con un cuerpo de superficie $S$, se utiliza una [[Integral doble]] con $dq = \sigma dS = \sigma dx dy$:

$$
\vec{E} = k \cdot \iint_S \frac{\sigma dS}{r^2} \cdot \hat{r}
$$

Si es un caso de [[Densidad de carga volumétrica]] $\rho$, con un cuerpo de [[Volumen]] $V$, se utiliza una [[Integral triple]] con $dq = \rho dV = \rho dx dy dz$:

$$
\vec{E} = k \cdot \iiint_V \frac{\rho dV}{r^2} \cdot \hat{r}
$$
