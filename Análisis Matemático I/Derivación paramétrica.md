---
created: 2024-08-19 18:37:36
modified: 2024-08-19 20:39:50
title: Derivación paramétrica
---

# Derivación paramétrica

Dada una [[Relación]] en [[Forma paramétrica]] $\left\{ \begin{array}{c} x = f(t) \\ y = g(t) \end{array} \right.$, y con un parámetro $t$. Para calcular la [[Derivada]] debemos seguir los siguientes pasos.

> [!note]
> Por costumbre, tomamos $x$ como la **variable independiente**, e $y$ como la **variable dependiente**, pero también se puede realizar lo opuesto.

1. Calcular el [[Diferencial]] de cada variable.

   $$
   \begin{array}{c}
       dx = x'(t) \cdot dt \\
       dy = y'(t) \cdot dt
   \end{array}
   $$

2. Formamos el **cociente** $\frac{dy}{dx}$ para obtener la [[Derivada]].

   $$
   \frac{dy}{dx} =
   \frac{y'(t) \cdot dt}{x'(t) \cdot dt} =
   \frac{y'(t)}{x'(t)}
   $$
