---
aliases:
  - SR flip-flop
created: 2024-11-06 13:13:28
modified: 2024-11-06 13:37:26
title: Biestable RS
---

# Biestable RS

Un [[Biestable]] cuyas [[Entradas]] son $S$ (set) y $R$ (reset), y sus [[Salidas]] $Q$ y $\overline{Q}$.

![[sr-flip-flop.gif]]

| $S$ | $R$ | $Q$ | $\overline{Q}$ |                     |
| --- | --- | --- | -------------- | ------------------- |
| $0$ | $0$ | $Q$ | $\overline{Q}$ |                     |
| $0$ | $1$ | $0$ | $1$            |                     |
| $1$ | $0$ | $1$ | $0$            |                     |
| $1$ | $1$ | $X$ | $X$            | [[Forbbiden state]] |

## Biestable RS síncrono

Funciona igual que el [[Biestable RS]] (asíncrono), pero se suma una [[Entradas|Entrada]] de **reloj** (*clock*, *clock pulse*, *ck*).

> [!important]
> El reloj se asegura de que cualquier **disparo** solo pueda ocurrir en el instante en el que el pulso del mismo pasa de $0$ a $1$ (visualmente, el comienzo de la cresta).

![[sr-flip-flop-clk.png]]

| $S$ | $R$ | $Ck$ | $Q$ | $\overline{Q}$ |                     |
| --- | --- | ---- | --- | -------------- | ------------------- |
| $X$ | $X$ | $0$  | $Q$ | $\overline{Q}$ |                     |
| $0$ | $0$ | $1$  | $Q$ | $\overline{Q}$ |                     |
| $1$ | $0$ | $1$  | $1$ | $0$            |                     |
| $0$ | $1$ | $1$  | $0$ | $1$            |                     |
| $1$ | $1$ | $1$  | $X$ | $X$            | [[Forbbiden state]] |
