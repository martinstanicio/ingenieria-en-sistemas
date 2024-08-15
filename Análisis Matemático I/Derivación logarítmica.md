---
created: 2024-08-15 18:03:20
modified: 2024-08-15 18:16:21
title: Derivación logarítmica
---

# Derivación logarítmica

Dada las [[Análisis Matemático I/Función|Funciones]] $f(x)$ y $g(x)$ **derivables** en $x$, y dada $h(x) = f(x)^{g(x)}$. Para calcular la [[Derivada]] de $h(x)$, debemos seguir los siguientes pasos.

1. Aplicar **logaritmo natural** a ambos lados.

   $$\ln (h(x)) = \ln (f(x)^{g(x)})$$

2. Aplicar la **propiedad de logaritmos** $\log_a x^y = y \cdot \log_a x$.

   $$\ln (h(x)) = g(x) \cdot \ln (f(x))$$

3. Calcular la [[Derivada]] miembro a miembro.

   $$\frac{1}{h(x)} \cdot h'(x) = g'(x) \cdot \ln (f(x)) + g(x) \cdot \frac{1}{f(x)} \cdot f'(x)$$

4. Despejar la [[Derivada]] buscada.

   $$h'(x) = h(x) \cdot \left( g'(x) \cdot \ln (f(x)) + g(x) \cdot \frac{1}{f(x)} \cdot f'(x) \right)$$

5. **Reemplazamos** $h(x)$ por $f(x)^{g(x)}$ por definición.

   $$h'(x) = f(x)^{g(x)} \cdot \left( g'(x) \cdot \ln (f(x)) + g(x) \cdot \frac{1}{f(x)} \cdot f'(x) \right)$$
