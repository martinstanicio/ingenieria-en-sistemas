---
aliases:
  - Gramáticas ambiguas
created: 2025-06-15 20:08:56
modified: 2025-06-15 20:28:43
title: Gramática ambigua
---

# Gramática ambigua

Una [[Gramática libre de contexto]] $G = \left< N, T, P, S \right>$ se considera ambigua si existe una [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha \in L \left( G \right)$, base de dos [[Árbol de derivación|Árboles de derivación]] $\tau \left( S \right)$ y $\tau' \left( S \right)$, tales que:

$$
\tau \left( S \right) \neq \tau' \left( S \right)
$$

> [!tip]
> Es decir, si existe una [[Lógica y Estructuras Discretas/Cadena|Cadena]] del [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] generado por $G$, para la cual existen múltiples [[Árbol de derivación|Árboles de derivación]] válidos diferentes.

---

Por ejemplo, sea la siguiente [[Gramática libre de contexto|GLC]]:

$$
G = \left< \set{ E }, \set{ \text{id}, +, * }, \set{ E \to E + E | E * E | \text{id} }, S \right>
$$

Para la [[Lógica y Estructuras Discretas/Cadena|Cadena]] $\alpha = a + b * c$ existen dos [[Árbol de derivación|Árboles de derivación]]:

```mermaid
flowchart TB
    E11(("E"))
    E12(("E"))
    E13(("E"))
    E14(("E"))
    E15(("E"))
    a1@{ shape: text, label: "$$a$$" }
    p1@{ shape: text, label: "$$+$$" }
    b1@{ shape: text, label: "$$b$$" }
    m1@{ shape: text, label: "$$*$$" }
    c1@{ shape: text, label: "$$c$$" }
    
    E21(("E"))
    E22(("E"))
    E23(("E"))
    E24(("E"))
    E25(("E"))
    a2@{ shape: text, label: "$$a$$" }
    p2@{ shape: text, label: "$$+$$" }
    b2@{ shape: text, label: "$$b$$" }
    m2@{ shape: text, label: "$$*$$" }
    c2@{ shape: text, label: "$$c$$" }
    
    E11 --> E12
    E11 ----> p1
    E11 --> E13
    E12 ---> a1
    E13 --> E14
    E13 ---> m1
    E13 --> E15
    E14 --> b1
    E15 --> c1
    
    E21 --> E22
    E21 ----> m2
    E21 --> E23
    E22 --> E24
    E22 ---> p2
    E22 --> E25
    E23 ---> c2
    E24 --> a2
    E25 --> b2
```
