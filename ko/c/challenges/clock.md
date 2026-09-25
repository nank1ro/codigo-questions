---
language: c
exerciseType: 1
difficulty: 2
title: 시계
---

# --description--

24시간 시계는 하루의 시각을 `HH:MM` 형태로 표시하며, 자정이 지나자마자 `00:00`에서 시작해 다음 자정 1분 전인 `23:59`에서 끝납니다. 두 부분은 항상 두 자리로 쓰이므로, 오전 11시 9분은 `11:09`로 표시됩니다.

하루 전체는 1440분입니다. 시계가 `23:59`를 지나면 `00:00`으로 넘어가 하루를 다시 시작하고, `00:00`에서 거꾸로 돌리면 `23:59`에 도착합니다.

# --instructions--

두 정수 `hours`와 `minutes`를 받아, 두 부분을 모두 두 자리로 채운 24시간 시계의 시각을 문자열 `"HH:MM"`으로 반환하는 함수 `clock_time`을 작성하세요.

예시:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- 두 숫자 중 하나는 음수이거나 실제 시계가 허용하는 값보다 클 수 있습니다.
- `hours * 60 + minutes`로 총 분 수를 구한 다음, 그 총합을 `0`부터 `1439` 범위로 감싸서 시계가 양방향으로 넘어가도록 하세요.
- `clock_time(24, 0)`은 정확히 하루이므로 `"00:00"`이 표시됩니다.

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

오전 8시는 `08:00`으로 표시됩니다

```c
    try_catch(strcmp(clock_time(8, 0), "08:00") == 0);
```

한 자리 숫자는 두 자리로 채워지므로, 오전 11시 9분은 `11:09`로 표시됩니다

```c
    try_catch(strcmp(clock_time(11, 9), "11:09") == 0);
```

정확히 하루 분의 시간이 지나면 `00:00`으로 넘어갑니다

```c
    try_catch(strcmp(clock_time(24, 0), "00:00") == 0);
```

60이 넘는 분은 시간으로 넘어갑니다

```c
    try_catch(strcmp(clock_time(25, 160), "03:40") == 0);
```

음수 시간은 시계를 자정 너머로 거꾸로 돌립니다

```c
    try_catch(strcmp(clock_time(-1, 15), "23:15") == 0);
```

음수 분 수도 시계를 거꾸로 돌립니다

```c
    try_catch(strcmp(clock_time(0, -90), "22:30") == 0);
```

하루 이상 거꾸로 돌아도 계속 넘어갑니다

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
