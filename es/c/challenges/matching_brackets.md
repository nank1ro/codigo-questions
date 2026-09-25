---
language: c
exerciseType: 1
difficulty: 3
title: Corchetes coincidentes
---

# --description--

El texto que contiene código, matemáticas o marcado está lleno de corchetes, y cada corchete de apertura necesita uno de cierre de la misma clase. Una cadena está equilibrada cuando sus corchetes se emparejan y se anidan como las capas de una cebolla: `{[()]}` está equilibrada, mientras que `{[(])}` no lo está, porque el par redondo se cierra antes que el par cuadrado dentro del cual se encuentra.

Aquí cuentan tres pares: paréntesis `()`, corchetes `[]` y llaves `{}`. Todos los demás caracteres de la cadena se ignoran. Un corchete de cierre debe cerrar el último corchete que se haya abierto y que aún siga abierto, y cuando la cadena termina no debe quedar ningún corchete abierto.

# --instructions--

Escribe una función `is_balanced` que tome una cadena y devuelva `true` cuando todos los corchetes que contiene estén emparejados y anidados correctamente, y `false` en caso contrario.

Ejemplos:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- Una cadena vacía está equilibrada.
- Los caracteres que no son corchetes se ignoran.
- Un corchete de cierre debe corresponder al último corchete que se haya abierto y que aún siga abierto.
- No debe quedar ningún corchete abierto cuando la cadena termina.

# --before-seed--

```c
// DO NOT EDIT FROM HERE
#include <setjmp.h>
#include <stdio.h>
#include <stdbool.h>

#ifndef _CEXCEPTION_H
#define _CEXCEPTION_H

#ifdef __cplusplus
extern "C"
{
#endif

//This is the value to assign when there isn't an exception
#ifndef CEXCEPTION_NONE
#define CEXCEPTION_NONE      (0x5A5A5A5A)
#endif

//This is number of exception stacks to keep track of (one per task)
#ifndef CEXCEPTION_NUM_ID
#define CEXCEPTION_NUM_ID    (1) //there is only the one stack by default
#endif

//This is the method of getting the current exception stack index (0 if only one stack)
#ifndef CEXCEPTION_GET_ID
#define CEXCEPTION_GET_ID    (0) //use the first index always because there is only one anyway
#endif

//The type to use to store the exception values.
#ifndef CEXCEPTION_T
#define CEXCEPTION_T         unsigned int
#endif

//This is an optional special handler for when there is no global Catch
#ifndef CEXCEPTION_NO_CATCH_HANDLER
#define CEXCEPTION_NO_CATCH_HANDLER(id)
#endif

//These hooks allow you to inject custom code into places, particularly useful for saving and restoring additional state
#ifndef CEXCEPTION_HOOK_START_TRY
#define CEXCEPTION_HOOK_START_TRY
#endif
#ifndef CEXCEPTION_HOOK_HAPPY_TRY
#define CEXCEPTION_HOOK_HAPPY_TRY
#endif
#ifndef CEXCEPTION_HOOK_AFTER_TRY
#define CEXCEPTION_HOOK_AFTER_TRY
#endif
#ifndef CEXCEPTION_HOOK_START_CATCH
#define CEXCEPTION_HOOK_START_CATCH
#endif

//exception frame structures
typedef struct {
  jmp_buf* pFrame;
  CEXCEPTION_T volatile Exception;
} CEXCEPTION_FRAME_T;

//actual root frame storage (only one if single-tasking)
extern volatile CEXCEPTION_FRAME_T CExceptionFrames[];

//Try
#define Try                                                         \
    {                                                               \
        jmp_buf *PrevFrame, NewFrame;                               \
        unsigned int MY_ID = CEXCEPTION_GET_ID;                     \
        PrevFrame = CExceptionFrames[MY_ID].pFrame;                 \
        CExceptionFrames[MY_ID].pFrame = (jmp_buf*)(&NewFrame);     \
        CExceptionFrames[MY_ID].Exception = CEXCEPTION_NONE;        \
        CEXCEPTION_HOOK_START_TRY;                                  \
        if (setjmp(NewFrame) == 0) {                                \
            if (1)

//Catch
#define Catch(e)                                                    \
            else { }                                                \
            CExceptionFrames[MY_ID].Exception = CEXCEPTION_NONE;    \
            CEXCEPTION_HOOK_HAPPY_TRY;                              \
        }                                                           \
        else                                                        \
        {                                                           \
            e = CExceptionFrames[MY_ID].Exception;                  \
            (void)e;                                                \
            CEXCEPTION_HOOK_START_CATCH;                            \
        }                                                           \
        CExceptionFrames[MY_ID].pFrame = PrevFrame;                 \
        CEXCEPTION_HOOK_AFTER_TRY;                                  \
    }                                                               \
    if (CExceptionFrames[CEXCEPTION_GET_ID].Exception != CEXCEPTION_NONE)

#endif

volatile CEXCEPTION_FRAME_T CExceptionFrames[CEXCEPTION_NUM_ID] = {{ 0 }};

void Throw(CEXCEPTION_T ExceptionID)
{
    unsigned int MY_ID = CEXCEPTION_GET_ID;
    CExceptionFrames[MY_ID].Exception = ExceptionID;
    if (CExceptionFrames[MY_ID].pFrame)
    {
        longjmp(*CExceptionFrames[MY_ID].pFrame, 1);
    }
    CEXCEPTION_NO_CATCH_HANDLER(ExceptionID);
}

CEXCEPTION_T e;
int _test_failed_count = 0;
int _test_count = 0;

void try_catch(bool assertion) {
    _test_count++;
    Try {
        if (!assertion) {
            Throw(_test_count);
        }
    } Catch (e) {
        _test_failed_count += 1;
        printf("Test Case '--err-t%i--' failed\n", e);
    }
}
// DO NOT EDIT UNTIL HERE
#include <stdlib.h>
#include <string.h>
```

# --seed--

```c
bool is_balanced(const char* text) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Una cadena vacía está equilibrada

```c
    try_catch(is_balanced("") == true);
```

Un solo par de paréntesis está equilibrado

```c
    try_catch(is_balanced("()") == true);
```

Los tres tipos de pares anidados unos dentro de otros están equilibrados

```c
    try_catch(is_balanced("{[()]}") == true);
```

Los corchetes mezclados con otro texto siguen estando equilibrados

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

Los pares colocados uno al lado del otro están equilibrados

```c
    try_catch(is_balanced("()[]{}") == true);
```

Una cadena sin ningún corchete está equilibrada

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

Un par cruzado no está equilibrado

```c
    try_catch(is_balanced("{[(])}") == false);
```

Un corchete de apertura que nunca se cierra no está equilibrado

```c
    try_catch(is_balanced("(") == false);
```

Un corchete de cierre antes de cualquier corchete de apertura no está equilibrado

```c
    try_catch(is_balanced(")(") == false);
```

Los pares cruzados en lo profundo de la cadena no están equilibrados

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

Un corchete de cierre que sobra al final no está equilibrado

```c
    try_catch(is_balanced("())") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool is_balanced(const char* text) {
    size_t length = strlen(text);
    char stack[length + 1];
    size_t top = 0;

    for (size_t i = 0; i < length; i++) {
        char current = text[i];

        if (current == '(' || current == '[' || current == '{') {
            stack[top++] = current;
        } else if (current == ')' || current == ']' || current == '}') {
            if (top == 0) {
                return false;
            }

            char opening = stack[--top];
            if ((current == ')' && opening != '(') ||
                (current == ']' && opening != '[') ||
                (current == '}' && opening != '{')) {
                return false;
            }
        }
    }

    return top == 0;
}
```
