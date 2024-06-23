---
created: 2024-04-14 01:06:41
modified: 2024-06-23 18:33:39
title: Espacio generado
---

# Espacio generado

Dado un [[Espacio vectorial]] $V$ y un [[Subconjunto]] de $n$ vectores del mismo ($v_1, v_2, \ldots, v_n$), se llama **conjunto generador** a dicho subconjunto, y **espacio generado** por el mismo a: 

$$H=gen\{v_1, v_2, \ldots, v_n\} = \{w \in V: w=\alpha_1 v_1 + \alpha_2 v_2 + \ldots + \alpha_n v_n, \alpha_1,\ldots ,\alpha_n \in \mathbb{R}\}$$

Para que un [[Conjunto]] también sea un **espacio generador**, un [[Subconjunto]] del mismo debe ser una [[Base]] del [[Espacio vectorial]].

>[!note]
>El espacio generado de un [[Conjunto]] son todas las posibles [[Combinación lineal|combinaciones lineales]] que se pueden formar a partir del mismo.

 Por lo tanto, siempre será un [[Subespacio vectorial]] del conjunto al que pertenecen los vectores, por las siguientes razones:

 1. **Contiene al [[Elemento neutro|Vector nulo]]:** podemos obtenerlo multiplicando a todos los vectores por $0$.
 2. **Es cerrado bajo la multiplicación por un escalar:** ya que todos los elementos son obtenidos multiplicando a los vectores por escalares.
 3. **Es cerrado bajo la suma:** ya que $h_1 + h_2$ también puede ser expresado como $\alpha_1 v_1 + \alpha_2 v_2$.
