---
language: c
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In a calendar year there are exactly 365.25 days. But, eventually, this will lead to confusion because humans normally count by exact divisibility of 1 and not with decimal points. So, to avoid the latter, it was decided to add up all 0.25 days every four-year cycle and give that year 366 days (including February 29 as an intercalary day) and call it a __leap year__. The other three years in the four-year cycle would only contain 365 days and __wouldn't be leap years__.

# --instructions--

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `time.h` import, `switch` statements, __if blocks__, __if-else blocks__ or __ternary operation__ (`x ? a : b`) nor the logical operators __AND__ (`&&`) and __OR__ (`||`) with the exemption of the __NOT__ (`!`) operator.

Return `true` if it's a leap year, `false` otherwise.

Example of function call:
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

The use of `time.h`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```c
    try_catch(leap_year(2016) == true);
```

The year `1996` is a leap year.

```c
    try_catch(leap_year(1996) == true);
```

The year `1600` is a leap year.

```c
    try_catch(leap_year(1600) == true);
```

The year `2020` is a leap year.

```c
    try_catch(leap_year(2020) == true);
```

The year `2000` is a leap year.

```c
    try_catch(leap_year(2000) == true);
```

The year `2008` is a leap year.

```c
    try_catch(leap_year(2008) == true);
```

The year `1521` is not a leap year.

```c
    try_catch(leap_year(1521) == false);
```

The year `1800` is not a leap year.

```c
    try_catch(leap_year(1800) == false);
```

The year `2007` is not a leap year.

```c
    try_catch(leap_year(2007) == false);
```

The year `2002` is not a leap year.

```c
    try_catch(leap_year(2002) == false);
```

The year `1979` is not a leap year.

```c
    try_catch(leap_year(1979) == false);
```

The year `2006` is not a leap year.

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
