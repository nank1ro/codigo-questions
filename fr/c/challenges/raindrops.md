---
language: c
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne qui contient des sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui divise uniformément un autre nombre sans laisser de reste.
Le moyen le plus simple de tester si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont les suivantes :

- a 3 comme facteur, ajoutez 'Pling' au résultat.
- a 5 comme facteur, ajoutez 'Plang' au résultat.
- a 7 comme facteur, ajoutez 'Plong' au résultat.
- n'a aucun de 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas factorisé par 3, 5 ou 7, donc le résultat serait `"34"`.

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
char* convert(int number) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Le son pour 1 est "1"

```c
    try_catch(strcmp(convert(1), "1") == 0);
```

Le son pour 3 est "Pling"

```c
    try_catch(strcmp(convert(3), "Pling") == 0);
```

Le son pour 5 est "Plang"

```c
    try_catch(strcmp(convert(5), "Plang") == 0);
```

Le son pour 7 est "Plong"

```c
    try_catch(strcmp(convert(7), "Plong") == 0);
```

Le son pour 6 est "Pling"

```c
    try_catch(strcmp(convert(6), "Pling") == 0);
```

Le son pour 8 est "8"

```c
    try_catch(strcmp(convert(8), "8") == 0);
```

Le son pour 9 est "Pling"

```c
    try_catch(strcmp(convert(9), "Pling") == 0);
```

Le son pour 10 est "Plang"

```c
    try_catch(strcmp(convert(10), "Plang") == 0);
```

Le son pour 14 est "Plong"

```c
    try_catch(strcmp(convert(14), "Plong") == 0);
```

Le son pour 15 est "PlingPlang"

```c
    try_catch(strcmp(convert(15), "PlingPlang") == 0);
```

Le son pour 21 est "PlingPlong"

```c
    try_catch(strcmp(convert(21), "PlingPlong") == 0);
```

Le son pour 25 est "Plang"

```c
    try_catch(strcmp(convert(25), "Plang") == 0);
```

Le son pour 27 est "Pling"

```c
    try_catch(strcmp(convert(27), "Pling") == 0);
```

Le son pour 35 est "PlangPlong"

```c
    try_catch(strcmp(convert(35), "PlangPlong") == 0);
```

Le son pour 49 est "Plong"

```c
    try_catch(strcmp(convert(49), "Plong") == 0);
```

Le son pour 52 est "52"

```c
    try_catch(strcmp(convert(52), "52") == 0);
```

Le son pour 105 est "PlingPlangPlong"

```c
    try_catch(strcmp(convert(105), "PlingPlangPlong") == 0);
```


Le son pour 3125 est "Plang"

```c
    try_catch(strcmp(convert(3125), "Plang") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* convert(int number) {
    char *result = malloc(sizeof(char) * 15);
    if (number % 3 == 0) {
        strcat(result, "Pling");
    }
    if (number % 5 == 0) {
        strcat(result, "Plang");
    }
    if (number % 7 == 0) {
        strcat(result, "Plong");
    }
    if (strlen(result) == 0) {
        sprintf(result, "%d", number);
    }
    return result;
}
```
