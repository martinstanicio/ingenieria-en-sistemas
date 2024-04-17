# Notación de modelos de procesos de negocios (BPMN)

<iframe width="560" height="315" src="https://www.youtube.com/embed/BbT0IN3y2V4?si=SNnIoo6RVllxmkuj" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Similar a un [[Diagrama de flujo]]. Posee los siguientes elementos:

- Inicio: círculo.
- Actividad: rectángulo con esquinas redondeadas. En el caso de una decisión, se expresa como un rectángulo, seguido de un rombo vacío.

Las flechas que conectan a todos los elementos son llamadas **flujo de mensaje**. La información de los mismos entra por izquierda y sale por derecha.

## Compuertas

Siempre hay que abrir o cerrar las compuertas. El objeto "final" también cierra a la última compuerta que haya quedado abierta.

- **Compuerta exclusiva:** elegir una de las opciones, un único camino.
- **Compuerta paralela:** se pueden realizar varias cosas al mismo tiempo.
- **Compuerta inclusiva:** algo que puede o no realizarse, sin afectar al proceso completo.
