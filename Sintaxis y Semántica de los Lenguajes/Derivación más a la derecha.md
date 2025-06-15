---
aliases:
  - Derivaciones más a la derecha
created: 2025-06-15 20:35:42
modified: 2025-06-15 20:43:12
title: Derivación más a la derecha
---

# Derivación más a la derecha

Una [[Derivación más a la derecha]] ocurre cuando, en cada paso de la derivación de una [[Lógica y Estructuras Discretas/Cadena|Cadena]], se elige el símbolo ==no terminal== que está más a la ==derecha== en la [[Forma sentencial]] para aplicar una regla de producción.

> [!note]
> Formalmente, $w \alpha \beta$ es una [[Derivación más a la derecha]] si y solo si:
>
> $$
> \left( w A \beta \to w \alpha \beta \right) \land \exists \left( A \to \alpha \right) \in P \land \beta \in T^*
> $$
>
> Donde $T$ es el [[Conjunto]] de terminales de la [[Gramática]].
