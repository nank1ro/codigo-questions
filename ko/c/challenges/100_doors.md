---
language: c
exerciseType: 1
difficulty: 1
title: 100개의 문
compilerOptions: -lm
---

# --description--

일렬로 놓인 100개의 문이 모두 닫혀 있습니다.
문 앞을 100번 지나갑니다.
첫 번째에는 모든 문을 방문하여 '토글'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째에는 2번째 문마다 (즉, 문 #2, #4, #6, ...) 방문하여 토글합니다.
세 번째에는 3번째 문마다 (즉, 문 #3, #6, #9, ...) 방문하며, 100번째 문만 방문할 때까지 계속합니다.

# --instructions--

마지막 통과 후 문의 상태를 결정하는 함수를 구현하십시오.
최종 결과를 배열로 반환하되, 열려 있는 문의 번호만 배열에 포함하십시오.
> 이 메서드는 가변적인 수의 문에서도 작동할 수 있어야 합니다.

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

100개의 문이 주어지면, 열린 문의 올바른 목록을 반환합니다

```c
    int sol1[50] = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100};
    try_catch(arrays_match(get_final_opened_doors(100), sol1));
```

10개의 문이 주어지면, 열린 문의 올바른 목록을 반환합니다

```c
    int sol2[50] = {1, 4, 9};
    try_catch(arrays_match(get_final_opened_doors(10), sol2));
```

950개의 문이 주어지면, 열린 문의 올바른 목록을 반환합니다

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
