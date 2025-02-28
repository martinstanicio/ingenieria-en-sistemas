---
created: 2025-02-28 16:10:19
modified: 2025-02-28 17:13:33
title: Gramática
---

# Gramática

Es una cuaterna.

$$
G = (T, N, P, \sigma)
$$

## Símbolos terminales

$T$ es el [[Conjunto]] de **símbolos terminales**, que son aquellas ==subcadenas== que terminan formando [[Lógica y Estructuras Discretas/Cadena|Cadenas]] más complejas, llamadas ==oraciones==.

> [!note]
> Este [[Conjunto]] suele coincidir con el [[Alfabeto]] $\Sigma$.

Una ==oración== o [[Lógica y Estructuras Discretas/Cadena|Cadena]] de nuestro [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]] siempre está formada únicamente por **símbolos terminales**.

## Símbolos no terminales

$N$ es el [[Conjunto]] de **símbolos no terminales**, que son un medio que me permite formar ==oraciones más complejas==, pero ==no aparecen== en las mismas.

> [!important]
> Un símbolo no puede ser terminal y no terminal a la vez.
>
> $$
> T \cap N = \emptyset
> $$

## Producciones

$P$ es el [[Conjunto]] de **producciones**, de forma que:

$$
P \subseteq \left[ \left( T \cup N \right)^* - T^* \right] \times \left[ \left( T \cup N \right)^* \right]
$$

Me dice como intercambiar los ==objetos intermedios== por los ==objetos finales==, que son los que van a aparecer en la oración formada.

## Símbolo inicial o distinguido

$\sigma$ o $S$ es el **símbolo inicial o distinguido** de la [[Gramática]], y $\sigma \in N$.

Es un caso especial de los [[Gramática#Símbolos no terminales]], que es el punto de partida para empezar a ==generar las oraciones== de mi [[Lógica y Estructuras Discretas/Lenguaje|Lenguaje]].
