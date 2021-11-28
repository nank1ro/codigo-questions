---
language: c
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertiire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `"Plong"`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `"PlingPlang"`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' `"34"`.

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
char* converti(int number) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Il suono per 1 è "1"

```c
    try_catch(strcmp(converti(1), "1") == 0);
```

Il suono per 3 è "Pling"

```c
    try_catch(strcmp(converti(3), "Pling") == 0);
```

Il suono per 5 è "Plang"

```c
    try_catch(strcmp(converti(5), "Plang") == 0);
```

Il suono per 7 è "Plong"

```c
    try_catch(strcmp(converti(7), "Plong") == 0);
```

Il suono per 6 è "Pling"

```c
    try_catch(strcmp(converti(6), "Pling") == 0);
```

Il suono per 8 è "8"

```c
    try_catch(strcmp(converti(8), "8") == 0);
```

Il suono per 9 è "Pling"

```c
    try_catch(strcmp(converti(9), "Pling") == 0);
```

Il suono per 10 è "Plang"

```c
    try_catch(strcmp(converti(10), "Plang") == 0);
```

Il suono per 14 è "Plong"

```c
    try_catch(strcmp(converti(14), "Plong") == 0);
```

Il suono per 15 è "PlingPlang"

```c
    try_catch(strcmp(converti(15), "PlingPlang") == 0);
```

Il suono per 21 è "PlingPlong"

```c
    try_catch(strcmp(converti(21), "PlingPlong") == 0);
```

Il suono per 25 è "Plang"

```c
    try_catch(strcmp(converti(25), "Plang") == 0);
```

Il suono per 27 è "Pling"

```c
    try_catch(strcmp(converti(27), "Pling") == 0);
```

Il suono per 35 è "PlangPlong"

```c
    try_catch(strcmp(converti(35), "PlangPlong") == 0);
```

Il suono per 49 è "Plong"

```c
    try_catch(strcmp(converti(49), "Plong") == 0);
```

Il suono per 52 è "52"

```c
    try_catch(strcmp(converti(52), "52") == 0);
```

Il suono per 105 è "PlingPlangPlong"

```c
    try_catch(strcmp(converti(105), "PlingPlangPlong") == 0);
```


Il suono per 3125 è "Plang"

```c
    try_catch(strcmp(converti(3125), "Plang") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* converti(int number) {
    char *risultato = malloc(sizeof(char) * 15);
    if (number % 3 == 0) {
        strcat(risultato, "Pling");
    }
    if (number % 5 == 0) {
        strcat(risultato, "Plang");
    }
    if (number % 7 == 0) {
        strcat(risultato, "Plong");
    }
    if (strlen(risultato) == 0) {
        sprintf(risultato, "%d", number);
    }
    return risultato;
}
```
