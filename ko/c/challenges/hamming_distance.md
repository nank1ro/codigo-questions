---
language: c
exerciseType: 1
difficulty: 1
title: 해밍 거리
---

# --description--

DNA는 각각 한 글자인 뉴클레오터드 가닥으로 표기합니다: `A`, `C`, `G` 또는 `T`. 같은 길이의 두 가닥을 나란히 놓으면 어떤 위치에는 같은 뉴클레오터드가 있고 어떤 위치에는 다른 뉴클레오터드가 있습니다.

두 가닥이 서로 다른 위치의 개수를 해밍 거리라고 하며, 생물학자들은 이를 이용해 두 가닥이 얼마나 멀어졌는지 측정합니다. `GAGCCTACTAACGGGAT`를 `CATCGTAATGACGGCCT`와 나란히 놓으면 서로 다른 위치가 7개이므로 두 가닥의 해밍 거리는 7입니다.

# --instructions--

같은 길이의 두 DNA 가닥을 받아 서로 다른 위치의 개수를 반환하는 함수 `hammingDistance`를 작성하세요.

예시:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 두 가닥은 항상 길이가 같으므로 길이가 다른 가닥을 처리할 필요는 없습니다.
- 두 빈 가닥은 어디에서도 다르지 않으므로 거리는 0입니다.

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

두 빈 가닥은 어디에서도 다르지 않습니다

```c
    try_catch(hammingDistance("", "") == 0);
```

같은 뉴클레오터드 하나를 가진 두 가닥에는 차이가 없습니다

```c
    try_catch(hammingDistance("A", "A") == 0);
```

다른 뉴클레오터드 하나를 가진 두 가닥은 한 위치에서 다릅니다

```c
    try_catch(hammingDistance("A", "G") == 1);
```

모든 위치에서 다른 두 짧은 가닥

```c
    try_catch(hammingDistance("AG", "CT") == 2);
```

첫 번째 위치에서만 다른 두 짧은 가닥

```c
    try_catch(hammingDistance("AT", "CT") == 1);
```

가닥 중간에 하나의 다른 뉴클레오터드

```c
    try_catch(hammingDistance("GGACG", "GGTCG") == 1);
```

위치가 다른 같은 뉴클레오터드도 차이로 계산됩니다

```c
    try_catch(hammingDistance("TAG", "GAT") == 2);
```

네 군데가 다른 더 긴 가닥 쌍

```c
    try_catch(hammingDistance("GATACA", "GCATAA") == 4);
```

가닥을 한 칸 밀면 거의 모든 위치가 달라집니다

```c
    try_catch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9);
```

설명에 나온 두 가닥의 거리는 7입니다

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
