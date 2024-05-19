---
created: 2024-04-14 01:06:41
modified: 2024-05-19 18:10:25
title: Espacio generado
---

# Espacio generado

Dado $V$ un [[Espacio vectorial]] y $v_1, v_2, \ldots, v_n$ n vectores de $V$, se llama **espacio generado** por $v_1, v_2, \ldots, v_n$ a: 

$$H=gen\{v_1, v_2, \ldots, v_n\} = \{w \in V: w=\alpha_1 v_1 + \alpha_2 v_2 + \ldots + \alpha_n v_n, \alpha_1,\ldots ,\alpha_n \in \mathbb{R}\}$$

>[!info]
>El espacio generado de un [[Conjunto]] son todas las posibles [[Combinación lineal|combinaciones lineales]] que se pueden formar a partir del mismo.

 Por lo tanto, siempre será un [[Subespacio vectorial]] del conjunto original, por las siguientes razones:

 1. **Contiene al [[Elemento neutro|Vector nulo]]:** podemos obtenerlo multiplicando a todos los vectores por $0$.
 2. **Es cerrado bajo la multiplicación por un escalar:** ya que todos los elementos son obtenidos multiplicando a los vectores por escalares.
 3. **Es cerrado bajo la suma:** ya que $h_1 + h_2$ también puede ser expresado como $\alpha_1 v_1 + \alpha_2 v_2$.
