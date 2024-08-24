---
created: 2024-08-23 17:36:56
modified: 2024-08-23 17:53:51
title: Vector acumulador
---

# Vector acumulador

Un [[Array|Vector]] donde cada elemento es un [[Acumulador]] para alguna serie de [[Dato|Datos]] particular.

> [!tip]
> Un [[Vector acumulador]] sirve para reemplazar una [[Estructura de casos]] de [[Acumulador|Acumuladores]].
> ```mermaid
> flowchart TB
>     comienzo([comienzo])
>     
>     condicion{variable}
>     
>     e1["a1 += valor"]
>     e2["a2 += valor"]
>     ei["..."]
>     en["an += valor"]
>     
>     a[" "]
>     
>     fin([fin])
>     
>     comienzo --> condicion
>     condicion -- 1 --> e1
>     condicion -- 2 --> e2
>     condicion -- "..." --> ei
>     condicion -- n --> en
>     e1 & e2 & ei & en --> a --> fin
> ```

```python
acumuladores[i] = acumuladores[i] + x
```
