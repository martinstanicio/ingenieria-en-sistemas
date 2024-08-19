---
created: 2024-08-19 18:37:36
modified: 2024-08-19 18:47:57
title: Derivación implícita
---

# Derivación implícita

Dada una [[Relación]] en [[Forma implícita]] $f(x, y) = 0$. Para calcular la [[Derivada]] de $h(x)$, debemos seguir los siguientes pasos, hasta llegar a una expresión de la forma $\frac{dy}{dx} = (\dots)$.

> [!note]
> Por costumbre, tomamos $x$ como la **variable independiente**, e $y$ como la **variable dependiente**, pero también se puede realizar lo opuesto.

Por ejemplo, con la siguiente circunferencia.

$$
x^2 + y^2 = 25
$$

1. [[Diferencial|Diferenciar]] miembro a miembro.

   $$d(x^2 + y^2) = d(25) \Rightarrow dx^2 + dy^2 = 0$$

2. **Agrupar** los términos con $dy$ en un miembro, y los términos con $dx$ en el otro.

   $$2y \cdot dy = - 2x \cdot dx$$

3. Armar el **cociente** $\frac{dy}{dx}$.

   $$\frac{dy}{dx} = - \frac{2x}{2y} \Leftrightarrow \frac{dy}{dx} = - \frac{x}{y}$$
