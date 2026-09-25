---
language: c
exerciseType: 1
difficulty: 2
title: Uhr
---

# --description--

Eine 24-Stunden-Uhr zeigt die Tageszeit als `HH:MM` an, beginnend mit `00:00` direkt nach Mitternacht und endend mit `23:59` eine Minute vor der nächsten Mitternacht. Beide Teile werden immer zweistellig geschrieben, daher zeigt neun Minuten nach elf Uhr morgens `11:09` an.

Ein ganzer Tag dauert 1440 Minuten. Sobald die Uhr über `23:59` hinausgeht, springt sie auf `00:00` und beginnt den Tag von vorne, und dreht man sie über `00:00` zurück, landet sie auf `23:59`.

# --instructions--

Schreiben Sie eine Funktion `clock_time`, die zwei ganze Zahlen, `hours` und `minutes`, entgegennimmt und die Anzeige einer 24-Stunden-Uhr als Zeichenkette `"HH:MM"` zurückgibt, wobei beide Teile zweistellig aufgefüllt sind.

Beispiele:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Eine der beiden Zahlen darf negativ sein oder größer, als es eine echte Uhr erlaubt.
- Berechnen Sie die Gesamtzahl der Minuten als `hours * 60 + minutes` und rechnen Sie diese Summe in den Bereich von `0` bis `1439` um, damit die Uhr in beide Richtungen überläuft.
- `clock_time(24, 0)` ist genau ein Tag, daher zeigt die Uhr `"00:00"` an.

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

Acht Uhr morgens zeigt `08:00` an

```c
    try_catch(strcmp(clock_time(8, 0), "08:00") == 0);
```

Einzelne Ziffern werden zweistellig aufgefüllt, daher zeigt neun Minuten nach elf `11:09` an

```c
    try_catch(strcmp(clock_time(11, 9), "11:09") == 0);
```

Genau ein ganzer Tag Stunden springt auf `00:00` zurück

```c
    try_catch(strcmp(clock_time(24, 0), "00:00") == 0);
```

Minuten über 60 werden in die Stunden übertragen

```c
    try_catch(strcmp(clock_time(25, 160), "03:40") == 0);
```

Eine negative Stunde dreht die Uhr über Mitternacht hinaus zurück

```c
    try_catch(strcmp(clock_time(-1, 15), "23:15") == 0);
```

Eine negative Minutenanzahl dreht die Uhr ebenfalls zurück

```c
    try_catch(strcmp(clock_time(0, -90), "22:30") == 0);
```

Mehr als ein ganzer Tag zurück läuft immer weiter über

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
