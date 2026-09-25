---
language: c
exerciseType: 1
difficulty: 2
title: Horloge
---

# --description--

Une horloge 24 heures affiche l'heure de la journée sous la forme `HH:MM`, commençant à `00:00` juste après minuit et se terminant à `23:59` une minute avant le minuit suivant. Les deux parties sont toujours écrites avec deux chiffres, ainsi neuf minutes après onze heures du matin se lit `11:09`.

Une journée entière dure 1440 minutes. Lorsque l'horloge dépasse `23:59`, elle repasse à `00:00` et recommence la journée, et la remonter en arrière avant `00:00` la fait atterrir sur `23:59`.

# --instructions--

Écrivez une fonction `clock_time` qui prend deux nombres entiers, `hours` et `minutes`, et retourne l'affichage d'une horloge 24 heures sous la forme de la chaîne `"HH:MM"`, les deux parties étant complétées sur deux chiffres.

Exemples :
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Chacun des deux nombres peut être négatif ou plus grand que ce qu'une véritable horloge permet.
- Calculez le nombre total de minutes avec `hours * 60 + minutes`, puis ramenez ce total dans la plage de `0` à `1439` afin que l'horloge boucle dans les deux sens.
- `clock_time(24, 0)` correspond exactement à une journée, donc l'affichage est `"00:00"`.

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

Huit heures du matin se lit `08:00`

```c
    try_catch(strcmp(clock_time(8, 0), "08:00") == 0);
```

Les chiffres uniques sont complétés sur deux chiffres, ainsi neuf minutes après onze heures se lit `11:09`

```c
    try_catch(strcmp(clock_time(11, 9), "11:09") == 0);
```

Exactement une journée entière d'heures repasse à `00:00`

```c
    try_catch(strcmp(clock_time(24, 0), "00:00") == 0);
```

Les minutes au-delà de 60 se reportent sur les heures

```c
    try_catch(strcmp(clock_time(25, 160), "03:40") == 0);
```

Une heure négative remonte l'horloge en arrière au-delà de minuit

```c
    try_catch(strcmp(clock_time(-1, 15), "23:15") == 0);
```

Un nombre de minutes négatif remonte également l'horloge en arrière

```c
    try_catch(strcmp(clock_time(0, -90), "22:30") == 0);
```

Plus d'une journée entière en arrière continue de boucler

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
