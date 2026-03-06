---
language: c
exerciseType: 1
difficulty: 3
title: 闰年
---

# --description--

一个日历年恰好有 365.25 天。但最终，这会导致混乱，因为人类通常按整除 1 来计数，而不是用小数点。因此，为了避免这种情况，决定每四年周期将所有 0.25 天累加，给那一年 366 天（包括 2 月 29 日作为闰日），并称之为__闰年__。四年周期中的其他三年只有 365 天，__不是闰年__。

# --instructions--

在这个挑战中，我们将提升难度，你需要在不使用 `time.h` 导入、`switch` 语句、__if 代码块__、__if-else 代码块__或__三元运算符__（`x ? a : b`）以及逻辑运算符 __AND__（`&&`）和 __OR__（`||`）的情况下判断是否为闰年，但可以使用 __NOT__（`!`）运算符。

如果是闰年返回 `true`，否则返回 `false`。

函数调用示例：
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

不允许使用 `time.h`、`switch`、`if`、`else`、`&&`、`||` 或 `?`。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016` 年是闰年。

```c
    try_catch(leap_year(2016) == true);
```

`1996` 年是闰年。

```c
    try_catch(leap_year(1996) == true);
```

`1600` 年是闰年。

```c
    try_catch(leap_year(1600) == true);
```

`2020` 年是闰年。

```c
    try_catch(leap_year(2020) == true);
```

`2000` 年是闰年。

```c
    try_catch(leap_year(2000) == true);
```

`2008` 年是闰年。

```c
    try_catch(leap_year(2008) == true);
```

`1521` 年不是闰年。

```c
    try_catch(leap_year(1521) == false);
```

`1800` 年不是闰年。

```c
    try_catch(leap_year(1800) == false);
```

`2007` 年不是闰年。

```c
    try_catch(leap_year(2007) == false);
```

`2002` 年不是闰年。

```c
    try_catch(leap_year(2002) == false);
```

`1979` 年不是闰年。

```c
    try_catch(leap_year(1979) == false);
```

`2006` 年不是闰年。

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
