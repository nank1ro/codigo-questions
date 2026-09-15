---
language: c
exerciseType: 1
difficulty: 2
title: Binäre Suche
---

# --description--

Die binäre Suche findet einen Wert in einer **sortierten** Sammlung, indem sie den Suchbereich wiederholt halbiert: Sieh dir das Element in der Mitte an, und wenn es nicht das gesuchte ist, mach in der linken Hälfte weiter, wenn der gesuchte Wert kleiner ist, oder in der rechten Hälfte, wenn er größer ist.

Da jeder Schritt die Hälfte der verbleibenden Elemente verwirft, erreicht die binäre Suche die Antwort selbst bei sehr großen Sammlungen mit einer Handvoll Vergleichen, während das Prüfen der Elemente eines nach dem anderen so viele Schritte kosten würde, wie es Elemente gibt.

# --instructions--

Schreibe eine Funktion `binarySearch`, die ein aufsteigend sortiertes Array von ganzen Zahlen, dessen Länge und eine gesuchte ganze Zahl entgegennimmt und den Index der gesuchten Zahl im Array zurückgibt oder `-1`, wenn die Zahl nicht vorhanden ist.

Das Array enthält niemals Duplikate, der Index ist also immer eindeutig. Das Array kann auch leer sein. Deine Funktion muss die binäre Suche verwenden und den Suchbereich bei jedem Schritt halbieren, statt linear zu suchen.

Beispiel für einen Funktionsaufruf:
```c
int numbers[] = {1, 3, 5, 7};
printf("%d\n", binarySearch(numbers, 4, 5));
// gibt 2 aus
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
#include <stdlib.h>
```

# --seed--

```c
int binarySearch(int *arr, int length, int target) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Die Suche in einem leeren Array muss -1 zurückgeben

```c
    try_catch(binarySearch(NULL, 0, 7) == -1);
```

Die Suche nach 5 in `[5]` muss 0 zurückgeben

```c
    int single[] = {5};
    try_catch(binarySearch(single, 1, 5) == 0);
```

Die Suche nach 9 in `[5]` muss -1 zurückgeben

```c
    try_catch(binarySearch(single, 1, 9) == -1);
```

Das erste Element -9 des 12-elementigen Arrays muss am Index 0 gefunden werden

```c
    int numbers[] = {-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78};
    try_catch(binarySearch(numbers, 12, -9) == 0);
```

Das letzte Element 78 des 12-elementigen Arrays muss am Index 11 gefunden werden

```c
    try_catch(binarySearch(numbers, 12, 78) == 11);
```

Das Element 15 muss am Index 6 gefunden werden

```c
    try_catch(binarySearch(numbers, 12, 15) == 6);
```

Das Element 22 muss am Index 7 gefunden werden

```c
    try_catch(binarySearch(numbers, 12, 22) == 7);
```

Der Wert 12, der zwischen 11 und 15 liegt, muss -1 zurückgeben

```c
    try_catch(binarySearch(numbers, 12, 12) == -1);
```

Ein gesuchter Wert, der kleiner als jedes Element ist, muss -1 zurückgeben

```c
    try_catch(binarySearch(numbers, 12, -100) == -1);
```

Ein gesuchter Wert, der größer als jedes Element ist, muss -1 zurückgeben

```c
    try_catch(binarySearch(numbers, 12, 100) == -1);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
int binarySearch(int *arr, int length, int target) {
    int low = 0;
    int high = length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```
