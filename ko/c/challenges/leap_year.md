---
language: c
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

역년에는 정확히 365.25일이 있습니다. 하지만 인간은 보통 소수점이 아닌 정수로 나누어 떨어지는 것을 기준으로 세기 때문에, 결국 이것은 혼란을 초래합니다. 이를 방지하기 위해, 4년 주기마다 0.25일을 모두 합산하여 해당 연도를 366일로 만들고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 3년은 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 챌린지에서는 한 단계 더 나아가, `time.h` 임포트, `switch` 문, __if 블록__, __if-else 블록__ 또는 __삼항 연산__ (`x ? a : b`)을 사용하지 않고, 또한 __NOT__ (`!`) 연산자를 제외한 논리 연산자 __AND__ (`&&`)와 __OR__ (`||`)도 사용하지 않고 윤년인지 아닌지를 판별해야 합니다.

윤년이면 `true`를, 그렇지 않으면 `false`를 반환하십시오.

함수 호출 예시:
```c
printf("%d\n", leap_year(2000));
// prints true
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
bool leap_year(int year) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

`time.h`, `switch`, `if`, `else`, `&&`, `||` 또는 `?`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```c
    try_catch(leap_year(2016) == true);
```

`1996`년은 윤년입니다.

```c
    try_catch(leap_year(1996) == true);
```

`1600`년은 윤년입니다.

```c
    try_catch(leap_year(1600) == true);
```

`2020`년은 윤년입니다.

```c
    try_catch(leap_year(2020) == true);
```

`2000`년은 윤년입니다.

```c
    try_catch(leap_year(2000) == true);
```

`2008`년은 윤년입니다.

```c
    try_catch(leap_year(2008) == true);
```

`1521`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(1521) == false);
```

`1800`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(1800) == false);
```

`2007`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(2007) == false);
```

`2002`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(2002) == false);
```

`1979`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(1979) == false);
```

`2006`년은 윤년이 아닙니다.

```c
    try_catch(leap_year(2006) == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool leap_year(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```c
bool leap_year(int year) {
  while (year % 100 == 0) {
    year = year / 100;
  }
  return year % 4 == 0;
}
```
