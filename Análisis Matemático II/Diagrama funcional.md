---
created: 2025-05-20 17:39:31
modified: 2025-05-20 17:42:34
title: Diagrama funcional
---

# Diagrama funcional

Es un diagrama que ayuda a mostrar la dependencia de variables en [[Función compuesta|Funciones compuestas]].

---

$$
z = f \left( x(t), y(t) \right)
$$

```mermaid
flowchart LR
    z --> x & y --> t
```

---

$$
z = f \left( x(r, s), y(r, s) \right)
$$

```mermaid
flowchart LR
    z --> x & y --> r & s
```
