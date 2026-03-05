---
language: c
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Dans une année civile, il y a exactement 365,25 jours. Mais, finalement, cela entraînera de la confusion car les humains comptent normalement par une divisibilité exacte de 1 et non par des décimales. Donc, pour éviter ce dernier, il a été décidé d'additionner tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (y compris le 29 février comme jour intercalaire) et de l'appeler une __année bissextile__. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et __ne seraient pas des années bissextiles__.

# --instructions--

Dans ce défi, nous allons l'amener à un nouveau niveau, où vous devez déterminer si c'est une année bissextile ou non sans l'utilisation de l'importation `time.h`, des instructions `switch`, des __blocs if__, des __blocs if-else__ ou des __opérations ternaires__ (`x ? a : b`) ni des opérateurs logiques __AND__ (`&&`) et __OR__ (`||`) sauf pour l'opérateur __NOT__ (`!`).

Retournez `true` si c'est une année bissextile, `false` sinon.

Exemple d'appel de fonction :
```c
printf("%d\n", leap_year(2000));
// prints true
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

L'utilisation de `time.h`, `switch`, `if`, `else`, `&&`, `||` ou `?` n'est pas autorisée.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'année `2016` est une année bissextile.

```c
    try_catch(leap_year(2016) == true);
```

L'année `1996` est une année bissextile.

```c
    try_catch(leap_year(1996) == true);
```

L'année `1600` est une année bissextile.

```c
    try_catch(leap_year(1600) == true);
```

L'année `2020` est une année bissextile.

```c
    try_catch(leap_year(2020) == true);
```

L'année `2000` est une année bissextile.

```c
    try_catch(leap_year(2000) == true);
```

L'année `2008` est une année bissextile.

```c
    try_catch(leap_year(2008) == true);
```

L'année `1521` n'est pas une année bissextile.

```c
    try_catch(leap_year(1521) == false);
```

L'année `1800` n'est pas une année bissextile.

```c
    try_catch(leap_year(1800) == false);
```

L'année `2007` n'est pas une année bissextile.

```c
    try_catch(leap_year(2007) == false);
```

L'année `2002` n'est pas une année bissextile.

```c
    try_catch(leap_year(2002) == false);
```

L'année `1979` n'est pas une année bissextile.

```c
    try_catch(leap_year(1979) == false);
```

L'année `2006` n'est pas une année bissextile.

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
