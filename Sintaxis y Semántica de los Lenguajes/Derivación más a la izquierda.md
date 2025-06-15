---
aliases:
  - Derivaciones más a la izquierda
created: 2025-06-15 20:35:42
modified: 2025-06-15 20:43:06
title: Derivación más a la izquierda
---

# Derivación más a la izquierda

Una [[Derivación más a la izquierda]] ocurre cuando, en cada paso de la derivación de una [[Lógica y Estructuras Discretas/Cadena|Cadena]], se elige el símbolo ==no terminal== que está más a la ==izquierda== en la [[Forma sentencial]] para aplicar una regla de producción.

> [!note]
> Formalmente, $w \alpha \beta$ es una [[Derivación más a la izquierda]] si y solo si:
>
> $$
> \left( w A \beta \to w \alpha \beta \right) \land \exists \left( A \to \alpha \right) \in P \land w \in T^*
> $$
>
> Donde $T$ es el [[Conjunto]] de terminales de la [[Gramática]].
