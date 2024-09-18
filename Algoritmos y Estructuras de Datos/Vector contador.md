---
created: 2024-08-23 17:36:56
modified: 2024-08-23 17:42:18
title: Vector contador
---

# Vector contador

Un [[Vector|Vector]] donde cada elemento es un [[Contador]] para alguna serie de [[Dato|Datos]] particular.

> [!tip]
> Un [[Vector contador]] sirve para reemplazar una [[Estructura de casos]] de [[Contador|Contadores]].
> ```mermaid
> flowchart TB
>     comienzo([comienzo])
>     
>     condicion{variable}
>     
>     e1["c1 += 1"]
>     e2["c2 += 1"]
>     ei["..."]
>     en["cn += 1"]
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
contadores[i] = contadores[i] + 1
```
