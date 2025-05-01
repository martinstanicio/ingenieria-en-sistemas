---
aliases:
  - Estructura
created: 2025-05-01 19:10:46
modified: 2025-05-01 19:26:14
title: Estructura organizacional
---

# Estructura organizacional

La [[Estructura]] de una [[Organización]].

## Tramos estrechos

Este formato permite una supervisión estrecha, ==control estricto==, y comunicación rápida.

```mermaid
flowchart TB
	A[" "]
	AA[" "]
	AB[" "]
	AC[" "]
	AAA[" "]
	AAB[" "]
	ABA[" "]
	ABB[" "]
	ACA[" "]
	ACB[" "]
	AAAA[" "]
	AAAB[" "]
	AABA[" "]
	AABB[" "]
	ABAA[" "]
	ABAB[" "]
	ABBA[" "]
	ABBB[" "]
	ACAA[" "]
	ACAB[" "]
	ACBA[" "]
	ACBB[" "]
	
	A --> AA & AB & AC
	AA --> AAA & AAB
	AB --> ABA & ABB
	AC --> ACA & ACB
	AAA --> AAAA & AAAB
	AAB --> AABA & AABB
	ABA --> ABAA & ABAB
	ABB --> ABBA & ABBB
	ACA --> ACAA & ACAB
	ACB --> ACBA & ACBB
```

Sin embargo, se puede ver a simple vista que genera ==muchos niveles administrativos==, y hace que los superiores tiendan a ==involucrarse demasiado== en el trabajo de sus subordinados.

## Tramos amplios

Este formato permite el fácil uso de la ==delegación==, y la creación de políticas claras para toda la [[Organización]].

```mermaid
flowchart TB
	A[" "]
	AA[" "]
	AB[" "]
	AC[" "]
	AD[" "]
	AE[" "]
	AF[" "]
	AG[" "]
	AH[" "]
	AI[" "]
	ADA[" "]
	ADB[" "]
	ADC[" "]
	ADD[" "]
	ADE[" "]
	ADF[" "]
	ADG[" "]
	ADH[" "]
	ADI[" "]
	ADJ[" "]
	ADK[" "]
	ADL[" "]
	
	A --> AA & AB & AC & AD & AE & AF & AG & AH & AI
	AD --> ADA & ADB & ADC & ADD & ADE & ADF & ADG & ADH & ADI & ADJ & ADK & ADL
```

Sin embargo, genera ==cuellos de botella== en la [[Delegación de decisiones|Toma de decisiones]], haciendo que el superior correspondiente pueda ==perder el control==.
