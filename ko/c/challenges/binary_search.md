---
language: c
exerciseType: 1
difficulty: 2
title: 이진 탐색
---

# --description--

이진 탐색은 **정렬된** 컬렉션 안에서 값을 찾는 방법으로, 탐색 범위를 계속 절반으로 나눕니다. 가운데 원소를 확인하고, 그것이 찾는 값이 아니라면 찾는 값이 더 작을 때는 왼쪽 절반을, 더 클 때는 오른쪽 절반을 계속 탐색합니다.

매 단계마다 남은 원소의 절반을 버리기 때문에, 이진 탐색은 아주 큰 컬렉션에서도 몇 번의 비교만으로 답에 도달합니다. 반면 원소를 하나씩 확인하는 방식은 원소의 개수만큼 단계가 필요합니다.

# --instructions--

오름차순으로 정렬된 정수 배열과 그 길이, 타깃 정수를 받아, 타깃이 배열 안에 있으면 그 인덱스를, 없으면 `-1`을 반환하는 함수 `binarySearch`를 작성하세요.

배열에는 중복이 없으므로 인덱스는 항상 유일합니다. 배열이 비어 있을 수도 있습니다. 함수는 선형 탐색이 아니라 매 단계마다 탐색 범위를 절반으로 줄이는 이진 탐색을 사용해야 합니다.

함수 호출 예시:
```c
int numbers[] = {1, 3, 5, 7};
printf("%d\n", binarySearch(numbers, 4, 5));
// prints 2
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

빈 배열에서 탐색하면 -1을 반환해야 합니다

```c
    try_catch(binarySearch(NULL, 0, 7) == -1);
```

`[5]`에서 5를 탐색하면 0을 반환해야 합니다

```c
    int single[] = {5};
    try_catch(binarySearch(single, 1, 5) == 0);
```

`[5]`에서 9를 탐색하면 -1을 반환해야 합니다

```c
    try_catch(binarySearch(single, 1, 9) == -1);
```

12개의 원소를 가진 배열의 첫 번째 원소 -9는 인덱스 0에서 찾아야 합니다

```c
    int numbers[] = {-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78};
    try_catch(binarySearch(numbers, 12, -9) == 0);
```

12개의 원소를 가진 배열의 마지막 원소 78은 인덱스 11에서 찾아야 합니다

```c
    try_catch(binarySearch(numbers, 12, 78) == 11);
```

원소 15는 인덱스 6에서 찾아야 합니다

```c
    try_catch(binarySearch(numbers, 12, 15) == 6);
```

원소 22는 인덱스 7에서 찾아야 합니다

```c
    try_catch(binarySearch(numbers, 12, 22) == 7);
```

11과 15 사이에 있는 값 12는 -1을 반환해야 합니다

```c
    try_catch(binarySearch(numbers, 12, 12) == -1);
```

모든 원소보다 작은 타깃은 -1을 반환해야 합니다

```c
    try_catch(binarySearch(numbers, 12, -100) == -1);
```

모든 원소보다 큰 타깃은 -1을 반환해야 합니다

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
