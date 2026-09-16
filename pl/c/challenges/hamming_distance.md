---
language: c
exerciseType: 1
difficulty: 1
title: Odległość Hamminga
---

# --description--

DNA zapisuje się jako nić nukleotydów, z których każdy jest pojedynczą literą: `A`, `C`, `G` lub `T`. Gdy dwie nici o tej samej długości ustawimy obok siebie, niektóre pozycje mają ten sam nukleotyd, a niektóre różne.

Liczba pozycji, w których dwie nici różnią się między sobą, nazywana jest odległością Hamminga, a biolodzy używają jej do mierzenia, jak bardzo dwie nici się od siebie oddaliły. Ustawienie `GAGCCTACTAACGGGAT` obok `CATCGTAATGACGGCCT` daje 7 różniących się pozycji, więc ich odległość Hamminga wynosi 7.

# --instructions--

Napisz funkcję `hammingDistance`, która przyjmuje dwie nici DNA o tej samej długości i zwraca liczbę pozycji, w których się różnią.

Przykłady:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Obie nici zawsze mają tę samą długość, więc nigdy nie musisz obsługiwać nici o różnych długościach.
- Dwie puste nici nie różnią się nigdzie, więc ich odległość wynosi 0.

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

Dwie puste nici nie różnią się nigdzie

```c
    try_catch(hammingDistance("", "") == 0);
```

Dwie identyczne nici z pojedynczym nukleotydem nie mają żadnej różnicy

```c
    try_catch(hammingDistance("A", "A") == 0);
```

Dwie różne nici z pojedynczym nukleotydem różnią się w jednej pozycji

```c
    try_catch(hammingDistance("A", "G") == 1);
```

Dwie krótkie nici różniące się w każdej pozycji

```c
    try_catch(hammingDistance("AG", "CT") == 2);
```

Dwie krótkie nici różniące się tylko w pierwszej pozycji

```c
    try_catch(hammingDistance("AT", "CT") == 1);
```

Pojedynczy różniący się nukleotyd w środku nici

```c
    try_catch(hammingDistance("GGACG", "GGTCG") == 1);
```

Te same nukleotydy w różnych pozycjach nadal liczą się jako różnice

```c
    try_catch(hammingDistance("TAG", "GAT") == 2);
```

Dłuższa para nici z czterema różnicami

```c
    try_catch(hammingDistance("GATACA", "GCATAA") == 4);
```

Przesunięcie nici o jedną pozycję powoduje, że prawie każda pozycja się różni

```c
    try_catch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9);
```

Dwie nici z opisu mają odległość równą siedem

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
