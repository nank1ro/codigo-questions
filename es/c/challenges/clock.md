---
language: c
exerciseType: 1
difficulty: 2
title: Reloj
---

# --description--

Un reloj de 24 horas muestra la hora del día como `HH:MM`, empezando en `00:00` justo después de la medianoche y terminando en `23:59`, un minuto antes de la siguiente medianoche. Ambas partes se escriben siempre con dos dígitos, así que nueve minutos después de las once de la mañana se lee `11:09`.

Un día completo dura 1440 minutos. Cuando el reloj pasa de `23:59`, vuelve a `00:00` y empieza el día de nuevo, y girarlo hacia atrás más allá de `00:00` cae en `23:59`.

# --instructions--

Escribe una función `clock_time` que reciba dos números enteros, `hours` y `minutes`, y devuelva la lectura de un reloj de 24 horas como la cadena `"HH:MM"`, con ambas partes rellenas con dos dígitos.

Ejemplos:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Cualquiera de los dos números puede ser negativo, o mayor de lo que permite un reloj real.
- Calcula el número total de minutos como `hours * 60 + minutes` y después encaja ese total en el rango de `0` a `1439` para que el reloj dé la vuelta en ambas direcciones.
- `clock_time(24, 0)` es exactamente un día, así que se lee `"00:00"`.

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
char* clock_time(int hours, int minutes) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

A las ocho de la mañana se lee `08:00`

```c
    try_catch(strcmp(clock_time(8, 0), "08:00") == 0);
```

Los números de un solo dígito se rellenan con dos, así que nueve minutos después de las once se lee `11:09`

```c
    try_catch(strcmp(clock_time(11, 9), "11:09") == 0);
```

Exactamente un día completo de horas da la vuelta a `00:00`

```c
    try_catch(strcmp(clock_time(24, 0), "00:00") == 0);
```

Los minutos por encima de 60 se trasladan a las horas

```c
    try_catch(strcmp(clock_time(25, 160), "03:40") == 0);
```

Una hora negativa gira el reloj hacia atrás más allá de la medianoche

```c
    try_catch(strcmp(clock_time(-1, 15), "23:15") == 0);
```

Una cantidad negativa de minutos también gira el reloj hacia atrás

```c
    try_catch(strcmp(clock_time(0, -90), "22:30") == 0);
```

Más de un día completo hacia atrás sigue dando la vuelta

```c
    try_catch(strcmp(clock_time(-25, 0), "23:00") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* clock_time(int hours, int minutes) {
    int total = (hours * 60 + minutes) % 1440;
    if (total < 0) {
        total += 1440;
    }

    char* result = malloc(6);
    sprintf(result, "%02d:%02d", total / 60, total % 60);
    return result;
}
```
