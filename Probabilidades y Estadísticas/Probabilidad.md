---
created: 2025-03-19 19:41:57
modified: 2025-06-22 16:22:30
title: Probabilidad
---

# Probabilidad

Sea $S$ un [[Espacio muestrario|Espacio muestral]] asociado a un [[Experimento]], la [[Probabilidades y Estadísticas/Probabilidad|Probabilidad]] es una [[Análisis Matemático I/Función|Función]] $P$.

$$
P: A \to [0, 1]
$$

Donde $A \subseteq S$ es un [[Evento]].

---

Es posible calcular la [[Probabilidad]] del [[Complemento]] de un [[Evento]].

$$
P \left( A \right) = 1 - P \left( A' \right)
\Leftrightarrow
P \left( A' \right) = 1 - P \left( A \right)
$$

> [!tip]
> Esto es particularmente útil, ya que muchas veces es más fácil calcular $P \left( A' \right)$ por métodos directos.

Y también es posible calcular la [[Probabilidad]] de la [[Unión (∪)]] de [[Evento|Eventos]].

$$
P \left( A \cup B \right) = P \left( A \right) + P \left( B \right) - P \left( A \cap B \right)
$$

> [!note]
> Es posible calcular la [[Probabilidad]] de la [[Intersección (∩)]] de [[Evento|Eventos]] mediante [[Probabilidad condicional]].
