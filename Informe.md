---
created: 2025-10-07 19:14:48
modified: 2025-10-07 19:34:23
title: Informe
---

# Informe

## Implementación

El analizador fue desarrollado en Python, manteniendo una estructura modular similar al TP1.

El proyecto se compone de los siguientes archivos principales:

- `parser.py`: implementación del analizador sintáctico.
- `lexer.py`: importado del TP1, encargado de tokenizar el código fuente.
- `main.py`: ejecuta las pruebas del parser sobre los distintos programas TINY.
- `tiny/`: contiene los programas de prueba (p1 a p15).

El *parser* está construido a partir de procedimientos que representan a los no terminales de la gramática.

Cada procedimiento verifica los tokens esperados y, si estos coinciden, continúa la derivación. En caso contrario, muestra un mensaje de error indicando el token esperado.

### Ejemplo de procedimiento

```python
FUNCION TCode():
    SI token_actual == 'PROGRAM':
        consumir('PROGRAM') # terminal
        consumir('ID') # terminal
        consumir('DOT') # terminal
        Body() # no terminal
    SINO:
        error("Se esperaba 'program'")
```

La función `match(token)` consume el token actual si coincide con el esperado.

Si no, invoca la rutina de manejo de errores, que muestra un mensaje como `DecVarBody: Se esperaba INT, o BOOL, pero se encontró ID en posición 6` (prueba 13).

## Gramática original

$$
P = \left\{
  \begin{array}{l}
    TCode \to \text{program id .} \space Body \\
    Body \to \text{begin} \space StatementList \space \text{end} | \text{var} \space DecVar \space DecVarList \space \text{begin} \space StatementList \space \text{end} \\
    DecVarList \to DecVarList \space DecVar | \lambda \\
    DecVar \to \text{id :} \space DecVarBody \\
    DecVarBody \to \text{int} \left( \text{num} \dots \text{num} \right) \text{= num ;} | \text{bool = true ;} | \text{bool = false ;} \\
    StatementList \to StatementList \space Statement | \lambda \\
    Statement \to \text{id :} \space StatementBody | StatementBody \\
    StatementBody \to Assignment | Conditional | Goto \\
    Goto \to \text{goto id ;} \\
    Assignment \to \text{let} \space Lvalue \space  \text{=} \space Rvalue \space \text{;} | \text{let} \space Lvalue \space \text{=} \space Rvalue \space Op \space Rvalue \space \text{;} | \text{let} \space Lvalue \space \text{=} \space \text{not} \space Rvalue \space \text{;} \\
    Op \to MatOp | BoolOp \\
    MatOp \to \text{+} | \text{-} | \text{*} \\
    BoolOp \to \text{or} | \text{and} \\
    Lvalue \to \text{id} \\
    Rvalue \to \text{id} | \text{num} | \text{true} | \text{false} \\
    Conditional \to \text{if} \space CompExpr \space \text{goto id ; else goto id ;} | \text{if} \space CompExpr \space \text{goto id ;} \\
    CompExpr \to Rvalue \space CompOp \space Rvalue \\
    CompOp \to \text{==} | \text{<>} | \text{<} | \text{>} | \text{<=} | \text{>=} \\
  \end{array}
\right\}
$$

## Gramática corregida

$$
P' = \left\{
  \begin{array}{l}
    TCode \to \text{program id .} \space Body \\
    Body \to \text{begin} \space StatementList \space \text{end} | \text{var} \space DecVar \space DecVarList \space \text{begin} \space StatementList \space \text{end} \\
    DecVarList \to DecVar \space DecVarList | \lambda \\
    DecVar \to \text{id :} \space DecVarBody \space \text{;} \\
    DecVarBody \to \text{int} \left( \text{num} \dots \text{num} \right) \text{= num} | \text{bool =} \space DecVarBody' \\
    DecVarBody' \to \text{true} | \text{false} \\
    StatementList \to Statement \space StatementList | \lambda \\
    Statement \to \text{id :} \space StatementBody | StatementBody \\
    StatementBody \to Assignment | Conditional | Goto \\
    Goto \to \text{goto id ;} \\
    Assignment \to \text{let} \space Lvalue \space \text{=} \space Assignment' \space \text{;} \\
    Assignment' \to Rvalue \space Assignment'' | \text{not} \space Rvalue \\
    Assignment'' \to Op \space Rvalue | \lambda \\
    Op \to MatOp | BoolOp \\
    MatOp \to \text{+} | \text{-} | \text{*} \\
    BoolOp \to \text{or} | \text{and} \\
    Lvalue \to \text{id} \\
    Rvalue \to \text{id} | \text{num} | \text{true} | \text{false} \\
    Conditional \to \text{if} \space CompExpr \space Goto \space Conditional' \\
    Conditional' \to \text{else} \space Goto | \lambda \\
    CompExpr \to Rvalue \space CompOp \space Rvalue \\
    CompOp \to \text{==} | \text{<>} | \text{<} | \text{>} | \text{<=} | \text{>=} \\
  \end{array}
\right\}
$$

## Pruebas realizadas

### Programa 1

```text
program p1 .
var
x : int (1 ... 10) = 5 ;
flag : bool = true ;
y : int (0 ... 100) = 42 ;
begin
let x = y + 5 ;
if x > 10 goto etiqueta1 ; else goto etiqueta2 ;
etiqueta1 : let y = not flag ;
goto fin ;
etiqueta2 : let flag = not false ;
fin : let x = x - y ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p1'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'x'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('ID', 'flag'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('ID', 'y'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '100'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '42'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'y'),
 ('PLUS', '+'),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'x'),
 ('GREATER_THAN', '>'),
 ('NUMBER', '10'),
 ('GOTO', 'goto'),
 ('ID', 'etiqueta1'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'etiqueta2'),
 ('SEMICOLON', ';'),
 ('ID', 'etiqueta1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'y'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'flag'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'etiqueta2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('MINUS', '-'),
 ('ID', 'y'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> id',
 'StatementList -> λ']
```

### Programa 2

```text
program p2 .
var
a : bool = false ;
b : int (0 ... 5) = 3 ;
c : int (10 ... 20) = 15 ;
begin
let b = c * 2 ;
if b <= 30 goto paso1 ;
paso1 : let a = not a ;
if a == true goto fin ; else goto paso2 ;
paso2 : let c = b + 1 ;
goto fin ;
fin : let b = c - 2 ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p2'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'a'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('ID', 'b'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '5'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('ID', 'c'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '10'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '20'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '15'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'b'),
 ('ASSIGN', '='),
 ('ID', 'c'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'b'),
 ('LESS_EQUAL', '<='),
 ('NUMBER', '30'),
 ('GOTO', 'goto'),
 ('ID', 'paso1'),
 ('SEMICOLON', ';'),
 ('ID', 'paso1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'a'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'a'),
 ('EQUAL', '=='),
 ('TRUE', 'true'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'paso2'),
 ('SEMICOLON', ';'),
 ('ID', 'paso2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'c'),
 ('ASSIGN', '='),
 ('ID', 'b'),
 ('PLUS', '+'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'b'),
 ('ASSIGN', '='),
 ('ID', 'c'),
 ('MINUS', '-'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> false",
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> <=',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> true',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> λ']
```

### Programa 3

```text
program p3 .
var
m : int (1 ... 9) = 1 ;
n : int (1 ... 9) = 2 ;
ok : bool = true ;
begin
let m = n + 3 ;
if m >= 5 goto L1 ;
L1 : let ok = not ok ;
if ok == false goto L2 ; else goto L3 ;
L2 : let n = m * 4 ;
goto fin ;
L3 : let m = n - 1 ;
fin : let ok = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p3'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'm'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '9'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('ID', 'n'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '9'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'ok'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'm'),
 ('ASSIGN', '='),
 ('ID', 'n'),
 ('PLUS', '+'),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'm'),
 ('GREATER_EQUAL', '>='),
 ('NUMBER', '5'),
 ('GOTO', 'goto'),
 ('ID', 'L1'),
 ('SEMICOLON', ';'),
 ('ID', 'L1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'ok'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'ok'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'ok'),
 ('EQUAL', '=='),
 ('FALSE', 'false'),
 ('GOTO', 'goto'),
 ('ID', 'L2'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'L3'),
 ('SEMICOLON', ';'),
 ('ID', 'L2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'n'),
 ('ASSIGN', '='),
 ('ID', 'm'),
 ('ASTERISK', '*'),
 ('NUMBER', '4'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'L3'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'm'),
 ('ASSIGN', '='),
 ('ID', 'n'),
 ('MINUS', '-'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'ok'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >=',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> false',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> λ']
```

### Programa 4

```text
program p4 .
var
counter : int (0 ... 100) = 0 ;
done : bool = false ;
begin
let counter = counter + 1 ;
if counter < 10 goto loop ; else goto salida ;
loop : let done = not done ;
goto counterCheck ;
counterCheck : if done == true goto endloop ; else goto loop ;
endloop : let counter = counter * 2 ;
salida : let done = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p4'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'counter'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '100'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '0'),
 ('SEMICOLON', ';'),
 ('ID', 'done'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'counter'),
 ('ASSIGN', '='),
 ('ID', 'counter'),
 ('PLUS', '+'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'counter'),
 ('LESS_THAN', '<'),
 ('NUMBER', '10'),
 ('GOTO', 'goto'),
 ('ID', 'loop'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'salida'),
 ('SEMICOLON', ';'),
 ('ID', 'loop'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'done'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'done'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'counterCheck'),
 ('SEMICOLON', ';'),
 ('ID', 'counterCheck'),
 ('COLON', ':'),
 ('IF', 'if'),
 ('ID', 'done'),
 ('EQUAL', '=='),
 ('TRUE', 'true'),
 ('GOTO', 'goto'),
 ('ID', 'endloop'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'loop'),
 ('SEMICOLON', ';'),
 ('ID', 'endloop'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'counter'),
 ('ASSIGN', '='),
 ('ID', 'counter'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'salida'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'done'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> false",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> <',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> true',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> λ']
```

### Programa 5

```text
program p5 .
var
x : int (1 ... 5) = 2 ;
y : int (1 ... 5) = 3 ;
z : bool = false ;
begin
let z = not z ;
if x <> y goto etiquetaA ; else goto etiquetaB ;
etiquetaA : let y = x + y ;
if y >= 5 goto etiquetaC ;
etiquetaC : let z = not true ;
goto fin ;
etiquetaB : let x = y * 2 ;
fin : let x = x - y ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p5'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'x'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '5'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'y'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '5'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('ID', 'z'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'z'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'z'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'x'),
 ('NOT_EQUAL', '<>'),
 ('ID', 'y'),
 ('GOTO', 'goto'),
 ('ID', 'etiquetaA'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'etiquetaB'),
 ('SEMICOLON', ';'),
 ('ID', 'etiquetaA'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'y'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('PLUS', '+'),
 ('ID', 'y'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'y'),
 ('GREATER_EQUAL', '>='),
 ('NUMBER', '5'),
 ('GOTO', 'goto'),
 ('ID', 'etiquetaC'),
 ('SEMICOLON', ';'),
 ('ID', 'etiquetaC'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'z'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'etiquetaB'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'y'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('MINUS', '-'),
 ('ID', 'y'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> false",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> <>',
 'Rvalue -> id',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >=',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> true',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> id',
 'StatementList -> λ']
```

### Programa 6

```text
program p6 .
var
a : int (0 ... 50) = 25 ;
b : int (0 ... 50) = 30 ;
flag : bool = true ;
begin
let a = b - 10 ;
if a <= b goto L1 ;
L1 : let flag = not flag ;
if flag == false goto L2 ; else goto L3 ;
L2 : let b = a + 5 ;
goto fin ;
L3 : let a = b * 2 ;
fin : let flag = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p6'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'a'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '50'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '25'),
 ('SEMICOLON', ';'),
 ('ID', 'b'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '50'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '30'),
 ('SEMICOLON', ';'),
 ('ID', 'flag'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('ID', 'b'),
 ('MINUS', '-'),
 ('NUMBER', '10'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'a'),
 ('LESS_EQUAL', '<='),
 ('ID', 'b'),
 ('GOTO', 'goto'),
 ('ID', 'L1'),
 ('SEMICOLON', ';'),
 ('ID', 'L1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'flag'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'flag'),
 ('EQUAL', '=='),
 ('FALSE', 'false'),
 ('GOTO', 'goto'),
 ('ID', 'L2'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'L3'),
 ('SEMICOLON', ';'),
 ('ID', 'L2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'b'),
 ('ASSIGN', '='),
 ('ID', 'a'),
 ('PLUS', '+'),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'L3'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('ID', 'b'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> <=',
 'Rvalue -> id',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> false',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> λ']
```

### Programa 7

```text
program p7 .
var
num : int (0 ... 10) = 1 ;
res : int (0 ... 10) = 0 ;
ok : bool = true ;
begin
let res = num * 2 ;
if res > 5 goto paso1 ; else goto paso2 ;
paso1 : let ok = not ok ;
if ok == true goto fin ;
paso2 : let num = res + 3 ;
goto paso1 ;
fin : let res = num - 1 ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p7'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'num'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('ID', 'res'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '0'),
 ('SEMICOLON', ';'),
 ('ID', 'ok'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'res'),
 ('ASSIGN', '='),
 ('ID', 'num'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'res'),
 ('GREATER_THAN', '>'),
 ('NUMBER', '5'),
 ('GOTO', 'goto'),
 ('ID', 'paso1'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'paso2'),
 ('SEMICOLON', ';'),
 ('ID', 'paso1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'ok'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'ok'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'ok'),
 ('EQUAL', '=='),
 ('TRUE', 'true'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'paso2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'num'),
 ('ASSIGN', '='),
 ('ID', 'res'),
 ('PLUS', '+'),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'paso1'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'res'),
 ('ASSIGN', '='),
 ('ID', 'num'),
 ('MINUS', '-'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> true',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> λ']
```

### Programa 8

```text
program p8 .
var
i : int (0 ... 20) = 0 ;
total : int (0 ... 20) = 0 ;
flag : bool = false ;
begin
let i = i + 1 ;
if i < 10 goto ciclo ;
ciclo : let total = total + i ;
if total >= 15 goto endciclo ; else goto ciclo ;
endciclo : let flag = not flag ;
goto salida ;
salida : let i = total - 5 ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p8'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'i'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '20'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '0'),
 ('SEMICOLON', ';'),
 ('ID', 'total'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '20'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '0'),
 ('SEMICOLON', ';'),
 ('ID', 'flag'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'i'),
 ('ASSIGN', '='),
 ('ID', 'i'),
 ('PLUS', '+'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'i'),
 ('LESS_THAN', '<'),
 ('NUMBER', '10'),
 ('GOTO', 'goto'),
 ('ID', 'ciclo'),
 ('SEMICOLON', ';'),
 ('ID', 'ciclo'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'total'),
 ('ASSIGN', '='),
 ('ID', 'total'),
 ('PLUS', '+'),
 ('ID', 'i'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'total'),
 ('GREATER_EQUAL', '>='),
 ('NUMBER', '15'),
 ('GOTO', 'goto'),
 ('ID', 'endciclo'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'ciclo'),
 ('SEMICOLON', ';'),
 ('ID', 'endciclo'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'flag'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'salida'),
 ('SEMICOLON', ';'),
 ('ID', 'salida'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'i'),
 ('ASSIGN', '='),
 ('ID', 'total'),
 ('MINUS', '-'),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> false",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> <',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >=',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> λ']
```

### Programa 9

```text
program p9 .
var
val : int (0 ... 100) = 50 ;
check : bool = true ;
tmp : int (0 ... 10) = 3 ;
begin
let tmp = val - 20 ;
if tmp >= 0 goto L1 ; else goto L2 ;
L1 : let check = not check ;
if check == false goto L3 ;
L2 : let val = tmp + 5 ;
goto L3 ;
L3 : let tmp = val * 2 ;
goto fin ;
fin : let check = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p9'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'val'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '100'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '50'),
 ('SEMICOLON', ';'),
 ('ID', 'check'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('ID', 'tmp'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'tmp'),
 ('ASSIGN', '='),
 ('ID', 'val'),
 ('MINUS', '-'),
 ('NUMBER', '20'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'tmp'),
 ('GREATER_EQUAL', '>='),
 ('NUMBER', '0'),
 ('GOTO', 'goto'),
 ('ID', 'L1'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'L2'),
 ('SEMICOLON', ';'),
 ('ID', 'L1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'check'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'check'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'check'),
 ('EQUAL', '=='),
 ('FALSE', 'false'),
 ('GOTO', 'goto'),
 ('ID', 'L3'),
 ('SEMICOLON', ';'),
 ('ID', 'L2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'val'),
 ('ASSIGN', '='),
 ('ID', 'tmp'),
 ('PLUS', '+'),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'L3'),
 ('SEMICOLON', ';'),
 ('ID', 'L3'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'tmp'),
 ('ASSIGN', '='),
 ('ID', 'val'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'check'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >=',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> false',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> λ']
```

### Programa 10

```text
program p10 .
var
a : int (0 ... 10) = 2 ;
b : int (0 ... 10) = 3 ;
c : bool = true ;
begin
let a = b + 4 ;
if a > 5 goto S1 ; else goto S2 ;
S1 : let c = not c ;
if c == false goto S3 ;
S2 : let b = a * 2 ;
goto S3 ;
S3 : let a = b - a ;
goto fin ;
fin : let c = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p10'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'a'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('ID', 'b'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '3'),
 ('SEMICOLON', ';'),
 ('ID', 'c'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('ID', 'b'),
 ('PLUS', '+'),
 ('NUMBER', '4'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'a'),
 ('GREATER_THAN', '>'),
 ('NUMBER', '5'),
 ('GOTO', 'goto'),
 ('ID', 'S1'),
 ('SEMICOLON', ';'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'S2'),
 ('SEMICOLON', ';'),
 ('ID', 'S1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'c'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'c'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'c'),
 ('EQUAL', '=='),
 ('FALSE', 'false'),
 ('GOTO', 'goto'),
 ('ID', 'S3'),
 ('SEMICOLON', ';'),
 ('ID', 'S2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'b'),
 ('ASSIGN', '='),
 ('ID', 'a'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'S3'),
 ('SEMICOLON', ';'),
 ('ID', 'S3'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('ID', 'b'),
 ('MINUS', '-'),
 ('ID', 'a'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'c'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> var DecVar DecVarList begin StatementList end',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 'DecVarBody -> int ( num ... num ) = num',
 'DecVarList -> DecVar DecVarList',
 'DecVar -> id : DecVarBody ;',
 "DecVarBody -> bool = DecVarBody'",
 "DecVarBody' -> true",
 'DecVarList -> λ',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> +',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> >',
 'Rvalue -> num',
 'Goto -> goto id ;',
 "Conditional' -> else Goto",
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Conditional',
 "Conditional -> if CompExpr Goto Conditional'",
 'CompExpr -> Rvalue CompOp Rvalue',
 'Rvalue -> id',
 'CompOp -> ==',
 'Rvalue -> false',
 'Goto -> goto id ;',
 "Conditional' -> λ",
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> *',
 'Rvalue -> num',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> Rvalue Assignment''",
 'Rvalue -> id',
 "Assignment'' -> Op Rvalue",
 'Op -> MatOp',
 'MatOp -> -',
 'Rvalue -> id',
 'StatementList -> Statement StatementList',
 'Statement -> StatementBody',
 'StatementBody -> Goto',
 'Goto -> goto id ;',
 'StatementList -> Statement StatementList',
 'Statement -> id : StatementBody',
 'StatementBody -> Assignment',
 "Assignment -> let Lvalue = Assignment' ;",
 'Lvalue -> id',
 "Assignment' -> not Rvalue",
 'Rvalue -> false',
 'StatementList -> λ']
```

### Programa 11

```text
program p11 .
begin
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p11'),
 ('DOT', '.'),
 ('BEGIN', 'begin'),
 ('END', 'end')]
```

#### Salida del parser

```python
['TCode -> program id . Body',
 'Body -> begin StatementList end',
 'StatementList -> λ']
```

### Programa 12

```text
program p12 .
var
x$ : int (1 ... 5) = 2 ;
begin
let x$ = 1 ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p12'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'x'),
 ('ERROR', '$'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '1'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '5'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ERROR', '$'),
 ('ASSIGN', '='),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

### Programa 13

```text
program p13 .
var
a : bol = true ;
begin
let a = not false ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p13'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'a'),
 ('COLON', ':'),
 ('ID', 'bol'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'a'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
'DecVarBody: Se esperaba INT, o BOOL, pero se encontró ID en posición 6'
```

### Programa 14

```text
program p14 .
var
x : int (0 ... 10) = 5 ;
begin
if x > 3 goto L1 else goto L2 ;
L1 : let x = x + 1 ;
goto fin
L2 : let x = x - 1 ;
fin : let x = x * 2 ;
end
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p14'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'x'),
 ('COLON', ':'),
 ('INT', 'int'),
 ('LPAREN', '('),
 ('NUMBER', '0'),
 ('ELLIPSIS', '...'),
 ('NUMBER', '10'),
 ('RPAREN', ')'),
 ('ASSIGN', '='),
 ('NUMBER', '5'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('IF', 'if'),
 ('ID', 'x'),
 ('GREATER_THAN', '>'),
 ('NUMBER', '3'),
 ('GOTO', 'goto'),
 ('ID', 'L1'),
 ('ELSE', 'else'),
 ('GOTO', 'goto'),
 ('ID', 'L2'),
 ('SEMICOLON', ';'),
 ('ID', 'L1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('PLUS', '+'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('GOTO', 'goto'),
 ('ID', 'fin'),
 ('ID', 'L2'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('MINUS', '-'),
 ('NUMBER', '1'),
 ('SEMICOLON', ';'),
 ('ID', 'fin'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'x'),
 ('ASSIGN', '='),
 ('ID', 'x'),
 ('ASTERISK', '*'),
 ('NUMBER', '2'),
 ('SEMICOLON', ';'),
 ('END', 'end')]
```

#### Salida del parser

```python
'Se esperaba SEMICOLON, pero se encontró ELSE en posición 22'
```

### Programa 15

```text
program p15 .
var
flag : bool = true ;
begin
let flag = not flag ;
if flag == true goto L1 ;
L1 : let flag = not false ;
```

#### Salida del lexer

```python
[('PROGRAM', 'program'),
 ('ID', 'p15'),
 ('DOT', '.'),
 ('VAR', 'var'),
 ('ID', 'flag'),
 ('COLON', ':'),
 ('BOOL', 'bool'),
 ('ASSIGN', '='),
 ('TRUE', 'true'),
 ('SEMICOLON', ';'),
 ('BEGIN', 'begin'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('ID', 'flag'),
 ('SEMICOLON', ';'),
 ('IF', 'if'),
 ('ID', 'flag'),
 ('EQUAL', '=='),
 ('TRUE', 'true'),
 ('GOTO', 'goto'),
 ('ID', 'L1'),
 ('SEMICOLON', ';'),
 ('ID', 'L1'),
 ('COLON', ':'),
 ('LET', 'let'),
 ('ID', 'flag'),
 ('ASSIGN', '='),
 ('NOT', 'not'),
 ('FALSE', 'false'),
 ('SEMICOLON', ';')]
```

#### Salida del parser

```python
'Se esperaba END, pero se encontró EOF en posición 32'
```
