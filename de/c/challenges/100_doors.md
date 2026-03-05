---
language: c
exerciseType: 1
difficulty: 1
title: 100 doors
compilerOptions: -lm
---

# --description--

Es gibt 100 Türen in einer Reihe, die alle anfangs geschlossen sind.
Sie machen 100 Durchgänge an den Türen vorbei.
Beim ersten Mal besuchen Sie jede Tür und schalten die Tür um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tür (d.h. Tür #2, #4, #6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie jede 3. Tür (d.h. Tür #3, #6, #9, ...), usw., bis Sie nur noch die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das endgültige Ergebnis in einem Array zurück, wobei nur die Türnummer enthalten ist, wenn die Tür offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen funktionieren.

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

// Returns true if two arrays are equal and in the same order
bool arrays_match(int *arr1, int *arr2) {
    // Check if the arrays are the same length
    int size1 = sizeof arr1 / sizeof *arr1;
    int size2 = sizeof arr2 / sizeof *arr2;
    if (size1 != size2) return false;

    // Check if all items exist and are in the same order
    for (int i = 0; i < sizeof(arr1); i++) {
        if (arr1[i] != arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```c
#include <math.h>
#include <stdlib.h>

int * get_final_opened_doors(int num_doors) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Bei 100 Türen die richtige Liste der offenen Türen zurückgeben

```c
    int sol1[50] = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100};
    try_catch(arrays_match(get_final_opened_doors(100), sol1));
```

Bei 10 Türen die richtige Liste der offenen Türen zurückgeben

```c
    int sol2[50] = {1, 4, 9};
    try_catch(arrays_match(get_final_opened_doors(10), sol2));
```

Bei 950 Türen die richtige Liste der offenen Türen zurückgeben

```c
    int sol3[50] = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900};
    try_catch(arrays_match(get_final_opened_doors(950), sol3));
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
#include <math.h>
#include <stdlib.h>

int * get_final_opened_doors(int num_doors) {
   int* open_doors = malloc(sizeof(int) * num_doors); 
   int arr_size = 0;
   int i = 1;
   while (pow(i, 2) <= num_doors) {
        open_doors[arr_size] = pow(i, 2);
        arr_size++;
        i++;
   }
   return open_doors;
}
```
