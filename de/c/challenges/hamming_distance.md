---
language: c
exerciseType: 1
difficulty: 1
title: Hamming-Abstand
---

# --description--

DNA wird als Strang von Nukleotiden geschrieben, jedes davon ein einzelner Buchstabe: `A`, `C`, `G` oder `T`. Werden zwei Stränge gleicher Länge Seite an Seite ausgerichtet, enthalten einige Positionen dasselbe Nukleotid und andere unterschiedliche.

Die Anzahl der Positionen, an denen sich die beiden Stränge unterscheiden, wird Hamming-Abstand genannt, und Biologen nutzen sie, um zu messen, wie weit zwei Stränge auseinandergegangen sind. Richtet man `GAGCCTACTAACGGGAT` mit `CATCGTAATGACGGCCT` aus, ergeben sich 7 Positionen mit Unterschieden, ihr Hamming-Abstand ist also 7.

# --instructions--

Schreiben Sie eine Funktion `hammingDistance`, die zwei DNA-Stränge gleicher Länge entgegennimmt und die Anzahl der Positionen zurückgibt, an denen sie sich unterscheiden.

Beispiele:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Die beiden Stränge haben immer die gleiche Länge, Sie müssen also niemals Stränge unterschiedlicher Länge behandeln.
- Zwei leere Stränge unterscheiden sich nirgends, ihr Abstand ist also 0.

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
int hammingDistance(const char* left, const char* right) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Zwei leere Stränge unterscheiden sich nirgends

```c
    try_catch(hammingDistance("", "") == 0);
```

Zwei identische Stränge aus einem einzelnen Nukleotid haben keinen Unterschied

```c
    try_catch(hammingDistance("A", "A") == 0);
```

Zwei unterschiedliche Stränge aus einem einzelnen Nukleotid unterscheiden sich an einer Position

```c
    try_catch(hammingDistance("A", "G") == 1);
```

Zwei kurze Stränge, die sich an jeder Position unterscheiden

```c
    try_catch(hammingDistance("AG", "CT") == 2);
```

Zwei kurze Stränge, die sich nur an der ersten Position unterscheiden

```c
    try_catch(hammingDistance("AT", "CT") == 1);
```

Ein einzelnes abweichendes Nukleotid in der Mitte der Stränge

```c
    try_catch(hammingDistance("GGACG", "GGTCG") == 1);
```

Dieselben Nukleotide an anderen Positionen zählen weiterhin als Unterschiede

```c
    try_catch(hammingDistance("TAG", "GAT") == 2);
```

Ein längeres Paar von Strängen mit vier Unterschieden

```c
    try_catch(hammingDistance("GATACA", "GCATAA") == 4);
```

Das Verschieben eines Strangs um eine Position bewirkt, dass sich fast jede Position unterscheidet

```c
    try_catch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9);
```

Die beiden Stränge aus der Beschreibung haben einen Abstand von sieben

```c
    try_catch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
int hammingDistance(const char* left, const char* right) {
    int distance = 0;

    for (int i = 0; left[i] != '\0'; i++) {
        if (left[i] != right[i]) {
            distance++;
        }
    }

    return distance;
}
```