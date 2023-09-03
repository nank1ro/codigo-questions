---
language: c
exerciseType: 1
difficulty: 3
title: Anno bisestile
---

# --description--

In un anno solare ci sono esattamente 365.25 giorni. Ma questo poteva portare confusione perché gli esseri umani normalmente contano in base all'esatta divisibilità di 1 e non con i punti decimali. Quindi, per evitare quest'ultimo problema, si decise di sommare tutti gli 0.25 giorni ogni ciclo di quattro anni e dare a quell'anno 366 giorni (includendo il 29 febbraio come giorno intercalare) e chiamarlo __anno bisestile__. Gli altri tre anni del ciclo quadriennale contengono solo 365 giorni e non sono __anni bisestili__.

# --instructions--

In questa sfida ci spingeremo ad un nuovo livello, in cui dovremo determinare se si tratta di un anno bisestile o meno senza l'import `time.h`, delle dichiarazioni `switch`, dei blocchi __if__, __if-else__ o delle __operazioni ausiliarie__ (`x ? a : b`) né degli operatori logici __AND__ (`&&`) e __OR__ (`||`) con l'eccezione dell'operatore __NOT__ (`!`).

Restituisci `true` se è un anno bisestile, `false` altrimenti.

Esempio di chiamata di funzione:
```c
println(leap_year(2000));
// stampa true
```

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
```

# --seed--

```c
bool leap_year(int year) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

L'uso di `time.h`, `switch`, `if`, `else`, `&&`, `||` o `?` non è consentito.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'anno `2016` è bisestile.

```c
    try_catch(leap_year(2016) == true);
```

L'anno `1996` è bisestile.

```c
    try_catch(leap_year(1996) == true);
```

L'anno `1600` è bisestile.

```c
    try_catch(leap_year(1600) == true);
```

L'anno `2020` è bisestile.

```c
    try_catch(leap_year(2020) == true);
```

L'anno `2000` è bisestile.

```c
    try_catch(leap_year(2000) == true);
```

L'anno `2008` è bisestile.

```c
    try_catch(leap_year(2008) == true);
```

L'anno `1521` non è bisestile.

```c
    try_catch(leap_year(1521) == false);
```

L'anno `1800` non è bisestile.

```c
    try_catch(leap_year(1800) == false);
```

L'anno `2007` non è bisestile.

```c
    try_catch(leap_year(2007) == false);
```

L'anno `2002` non è bisestile.

```c
    try_catch(leap_year(2002) == false);
```

L'anno `1979` non è bisestile.

```c
    try_catch(leap_year(1979) == false);
```

L'anno `2006` non è bisestile.

```c
    try_catch(leap_year(2006) == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool leap_year(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```c
bool leap_year(int year) {
  while (year % 100 == 0) {
    year = year / 100;
  }
  return year % 4 == 0;
}
```
