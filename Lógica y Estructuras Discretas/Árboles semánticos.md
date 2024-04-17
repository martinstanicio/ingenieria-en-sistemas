# Árboles semánticos

Se utiliza para verificar que una serie de [[Proposiciones]] no pueden ser todas verdaderas simultáneamente. Para esto, se evalúa la conjunción de todas las premisas, y la negación de la conclusión.

Cuando tengo una [[Disyunción (∨)]], las ramas del árbol se bifurcan por cada preposición de la misma.

Cuando tengo una [[Conjunción (∧)]], se continúa la rama, con las proposiciones una luego de la otra.

Cuando tengo una doble [[Negación (-)]], se continúa en la misma rama, con la simplificación de la preposición, sin la doble negación.

Cuando tengo una [[Implicación (→)]], se aplica $(p\rightarrow q)\Leftrightarrow -p \lor q$, y se ramifica como una conjunción.
