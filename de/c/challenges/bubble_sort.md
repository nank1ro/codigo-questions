---
language: c
exerciseType: 1
difficulty: 2
title: Bubblesort
---

# --description--

Bubblesort ist einer der einfachsten Sortieralgorithmen. Er durchläuft eine Liste und vergleicht jedes Paar benachbarter Elemente, wobei er sie vertauscht, sobald sie in der falschen Reihenfolge stehen. Nach jedem vollständigen Durchlauf ist der größte verbleibende Wert an seine endgültige Position „aufgestiegen“, und die Liste ist sortiert, sobald ein Durchlauf ohne einen einzigen Tausch endet.

# --instructions--

Schreiben Sie eine Funktion namens `bubbleSort`, die ein Array von ganzen Zahlen in aufsteigender Reihenfolge sortiert.

Das Array wird an Ort und Stelle sortiert: `bubbleSort` erhält einen Zeiger auf das Array und dessen Länge und ordnet die Elemente genau dieses Arrays um.

Sie müssen den Bubblesort-Algorithmus selbst implementieren, indem Sie benachbarte Elemente vergleichen und vertauschen. Verwenden Sie keine Sortierfunktion aus der Standardbibliothek.

Ihre Funktion muss auch mit einem leeren Array, einem Array mit einem einzigen Element, einem bereits sortierten Array, wiederholten Werten und negativen Zahlen funktionieren.

Beispiel eines Funktionsaufrufs:
```c
int numbers[] = {3, 1, 2};
bubbleSort(numbers, 3);
printf("%d %d %d\n", numbers[0], numbers[1], numbers[2]);
// prints 1 2 3
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
void bubbleSort(int *arr, int length) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Ein leeres Array muss unverändert bleiben

```c
    int arr1[1] = {7};
    bubbleSort(arr1, 0);
    try_catch(arr1[0] == 7);
```

Ein Array mit einem einzigen Element muss gleich bleiben

```c
    int arr2[] = {42};
    bubbleSort(arr2, 1);
    try_catch(arr2[0] == 42);
```

Ein bereits sortiertes Array muss in derselben Reihenfolge bleiben

```c
    int arr3[] = {1, 2, 3, 4, 5};
    bubbleSort(arr3, 5);
    try_catch(arr3[0] == 1 && arr3[1] == 2 && arr3[2] == 3 && arr3[3] == 4 && arr3[4] == 5);
```

Ein absteigend sortiertes Array muss in aufsteigende Reihenfolge gebracht werden

```c
    int arr4[] = {5, 4, 3, 2, 1};
    bubbleSort(arr4, 5);
    try_catch(arr4[0] == 1 && arr4[1] == 2 && arr4[2] == 3 && arr4[3] == 4 && arr4[4] == 5);
```

Wiederholte Werte müssen alle erhalten bleiben

```c
    int arr5[] = {3, 1, 3, 2, 1};
    bubbleSort(arr5, 5);
    try_catch(arr5[0] == 1 && arr5[1] == 1 && arr5[2] == 2 && arr5[3] == 3 && arr5[4] == 3);
```

Negative Zahlen müssen vor den positiven sortiert werden

```c
    int arr6[] = {-5, 3, -1, 0, -9};
    bubbleSort(arr6, 5);
    try_catch(arr6[0] == -9 && arr6[1] == -5 && arr6[2] == -1 && arr6[3] == 0 && arr6[4] == 3);
```

Ein längeres gemischtes Array muss in aufsteigender Reihenfolge sortiert werden

```c
    int arr7[] = {9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6};
    int expected7[] = {-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14};
    bubbleSort(arr7, 12);
    bool ok7 = true;
    for (int i = 0; i < 12; i++) {
        if (arr7[i] != expected7[i]) ok7 = false;
    }
    try_catch(ok7);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
void bubbleSort(int *arr, int length) {
    bool swapped = true;
    while (swapped) {
        swapped = false;
        for (int i = 1; i < length; i++) {
            if (arr[i - 1] > arr[i]) {
                int temp = arr[i - 1];
                arr[i - 1] = arr[i];
                arr[i] = temp;
                swapped = true;
            }
        }
        length--;
    }
}
```
