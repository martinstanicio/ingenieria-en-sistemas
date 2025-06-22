---
aliases:
  - Definición clásica de probabilidad de Laplace
  - Definición clásica de probabilidad
  - Probabilidad de eventos igualmente probables
created: 2025-03-19 19:14:08
modified: 2025-06-22 16:37:21
title: Probabilidad de eventos equiprobables
---

# Probabilidad de eventos equiprobables

Si los [[Evento|Eventos]] que constituyen el [[Espacio muestrario|Espacio muestral]] $S$ son ==equiprobables==, se cumple lo siguiente.

$$
\forall E \in S: P \left( E \right) = \frac{1}{\# S}
$$

Por lo tanto, la [[Probabilidad]] de un [[Evento compuesto]] $A \subseteq S$ se puede calcular de la siguiente forma.

$$
P \left( A \right) =
\sum_{E_i \in A} P \left( E_i \right) =
\sum_{E_i \in A} \frac{1}{\# S} =
\frac{\# A}{\# S} =
\frac{\text{casos favorables}}{\text{casos totales}}
$$
