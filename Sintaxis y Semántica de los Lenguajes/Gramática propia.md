---
aliases:
  - Gramáticas propias
created: 2025-06-15 21:08:34
modified: 2025-06-15 21:11:58
title: Gramática propia
---

# Gramática propia

Una [[Gramática libre de contexto]] $G = \left< N, T, P, S \right>$ es [[Gramática propia|Propia]] si y solo si:

$$
\forall \left( A \to \beta \right) \in P, \left( \beta \neq \lambda \lor A = S \right)
$$

> [!tip]
> Una [[Gramática]] es [[Gramática propia|Propia]] si no existen [[Símbolo anulable|Símbolos anulables]], excepto el símbolo distinguido $S$, que puede o no ser [[Símbolo anulable|Anulable]].
