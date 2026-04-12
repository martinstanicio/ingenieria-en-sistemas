---
created: 2026-04-11 23:31:02
modified: 2026-04-11 23:32:24
title: TP01 - Repaso Arquitectura
---
# TP01 - Repaso Arquitectura

## Ejercicio 1

Realizar un programa assembler que permita ingresar por teclado una cadena de caracteres que termine con el signo \$.

Usar la función de la interrupción `21h` que toma el ingreso de datos de a un byte, los bytes ingresados deben almacenarse desde el desplazamiento `2000h` del segmento de datos guardado en el registro `DS`.

```asm
(01) MOV SI, 2000
(02) MOV AH, 01
(03) INT 21
(04) MOV [SI], AL
(05) CMP AL, 24
(06) JZ  (09)
(07) INC SI
(08) JMP (03)
(09) INT 20
```

## Ejercicio 2

Realizar un programa assembler que permita ingresar por teclado una expresión algebraica del tipo $número + número =$, debe aparecer el resultado de la suma después del signo $=$.

Para simplificar el problema los números a sumar serán de un digito cada uno, por ejemplo $3 + 4 = 7$, y para simplificarlo aún más la suma de los dos números siempre debe dar un número de un dígito. No es necesario hacer ningún tipo de validación en el ingreso de datos.

```asm
(01) MOV SI, 2000
(02) MOV AH, 01
(03) INT 21        ; Primer número (x)
(04) MOV [SI], AL
(05) INT 21        ; Símbolo de suma (+)
(06) INT 21        ; Segundo número (y)
(07) ADD [SI], AL
(08) INT 21        ; Símbolo de igualdad (=)
(09) SUB [SI], 30
(10) MOV DL, [SI]
(11) MOV AH, 02
(12) INT 21
(13) INT 20
```

## Ejercicio 3

Crear una rutina que muestre por pantalla los caracteres de tabla ASCII de los códigos `30h` a `39h`. Se utilizará `INT 61`, y la rutina tiene como última instrucción `IRET`.

Los 4 bytes que forman la dirección de memoria donde se encontrará el código de máquina de la rutina que resuelve el problema se almacenan en el vector de interrupciones en el desplazamiento $61h \cdot 4h = 184h$.

Antes de ejecutar el programa y la rutina de interrupción, se debe escribir en memoria los contenidos del vector. Para ello, se debe escribir el comando `E 0000:0184` y a partir de esta dirección se debe escribir a la manera de Intel primero el valor de `IP` (donde está la primera instrucción elegida para la rutina de interrupción) y luego el de `CS`, que es el que muestra el DEBUG a la izquierda de los dos puntos que aparecen en cada dirección. De no realizarse este paso, cuando se ejecuta la instrucción `INT 61`, la `UC` irá a la dirección `0000:0184` donde no encontrará la dirección correcta de inicio de la rutina, por lo que seguramente la CPU se "colgará" sin poder saltar la ejecución al lugar adecuado de memoria.

Observar en el DEBUG, que sucede con el FLAG `I`, después de ejecutar `INT 61` y luego de ejecutar `IRET`.

```asm
(01) MOV AH, 02
(02) MOV DL, 30
(03) INT 21
(04) CMP DL, 39
(05) JZ  (08)
(06) INC DL
(07) JMP (03)
(08) IRET
```

Para que el programa anterior se ejecute cuando llamamos a la interrupción `61h`:

```asm
(09) MOV AX, 0000
(10) MOV ES, AX
(11) MOV ES:[0184], (1)  ; El IP de la INT 61 está en 0184
(12) MOV ES:[0186], CS   ; El CS de la INT 61 está en 0186
(13) INT 20
```

> [!NOTE]
> No es posible asignar un valor literal al registro `ES` (Extra Segment) directamente, por lo que se utiliza el registro `AX` como intermediario para cargar el valor deseado en `ES`.
