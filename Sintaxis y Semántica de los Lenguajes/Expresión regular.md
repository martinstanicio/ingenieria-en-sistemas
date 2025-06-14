---
aliases:
  - Expresiones regulares
  - ER
  - REGEX
created: 2025-06-10 21:47:38
modified: 2025-06-14 18:58:27
title: Expresión regular
---

# Expresión regular

Es un formalismo para expresar un [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] ==regular== (tipo 3).

Sea un [[Alfabeto]] $\Sigma$, las [[Expresión regular|ER]] sobre $\Sigma$ y los [[Conjunto|Conjuntos]] que ellas denotan ([[Conjunto regular|Conjuntos regulares]]) son definidos recursivamente de la siguiente forma.

1. $\emptyset$ es una [[Expresión regular|ER]] y denota el [[Conjunto vacío]] $\emptyset$
2. $\lambda$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ \lambda }$
3. Por cada $a \in \Sigma$, $a$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $\set{ a }$
4. Si $r$ y $s$ son [[Expresión regular|ER]] que denotan los [[Lógica y Estructuras Discretas/Lenguaje|Lenguajes]] $R$ y $S$, entonces:
	- $r + s \Leftrightarrow r / s$ es una [[Expresión regular|ER]] y denota $R \cup S$
	- $rs \Leftrightarrow r \cdot s$ es una [[Expresión regular|ER]] y denota $R \circ S$ (concatenación)
	- $r^*$ es una [[Expresión regular|ER]] y denota el [[Conjunto]] $R^*$ ([[Cerradura de Kleene]] de $R$)

> [!tip]
> Por la definición de la [[Cerradura de Kleene]] y la [[Cerradura positiva]], las siguientes expresiones son equivalentes.
>
> $$
> rr^* = r^+
> $$

## Pasaje de ER a AFD

La [[Expresión regular|ER]] inicial $u$ representa el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] $L_0 = L \left( u \right)$ que será aceptado por el [[Lógica y Estructuras Discretas/Estado|Estado]] inicial $q_0$ del [[Autómata finito determinístico|AFD]]. Luego, se calculan las [[Derivada de una expresión regular|Derivadas]] de la [[Expresión regular|ER]] para cada símbolo del alfabeto $\Sigma$; cada [[Expresión regular|ER]] $L_i$ diferente resultante representa un [[Lógica y Estructuras Discretas/Estado|Estado]] $q_i$ del [[Autómata finito determinístico|AFD]], que se alcanza ante una transición por el símbolo $a \in \Sigma$ respecto al cual se realizó la [[Derivada de una expresión regular|Derivada]] $D_a \left( L_0 \right) = L_i$.

> [!important]
> Un [[Lógica y Estructuras Discretas/Estado|Estado]] es final si el [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] que representa contiene la [[Cadena vacía]] $\lambda$; es decir, si $T \left( L_i \right)$ no es $\emptyset$.

## Pasaje de ER a AFND-λ

Sea $r$ una [[Expresión regular|ER]], entonces existe un [[Autómata finito no determinístico lambda|AFND-λ]] que acepta $L \left( r \right)$.

```mermaid
flowchart LR
    q0["$$q_0$$"]
    subgraph "$$M_1$$"
        q1["$$q_1$$"] -- "..." --> f1["$$f_1$$"]
    end
    subgraph "$$M_2$$"
        q2["$$q_2$$"] -- "..." --> f2["$$f_2$$"]
    end
    f0["$$f_0$$"]
    
    q0 --> |"$$\lambda$$"| q1 & q2
    f1 & f2 --> |"$$\lambda$$"| f0
```

$$
r = r_1 + r_2 \land L \left( r_1 \right) = L \left( M_1 \right) \land L \left( r_2 \right) = L \left( M_2 \right) \Rightarrow L \left( r \right) = L \left( M \right)
$$

==**FALTA PROCEDIMIENTO (gráficos de disyunción, concatenación y cerradura de kleene)**==
