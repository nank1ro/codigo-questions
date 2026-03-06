---
language: c
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与某些潜在因数对应的雨滴声的字符串。
因数是能整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数，最简单的方法是使用取模运算。
雨滴的规则如下：

- 以 3 为因数，在结果中添加 'Pling'。
- 以 5 为因数，在结果中添加 'Plang'。
- 以 7 为因数，在结果中添加 'Plong'。
- 如果 3、5 或 7 都不是因数，则结果应为该数字本身。

# --instructions--

编写一个返回正确字符串的函数，示例：

- 28 以 7 为因数，但不以 3 或 5 为因数，所以结果为 `"Plong"`。
- 30 同时以 3 和 5 为因数，但不以 7 为因数，所以结果为 `"PlingPlang"`。
- 34 不能被 3、5 或 7 整除，所以结果为 `"34"`。

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
char* convert(int number) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

1 的声音是 "1"

```c
    try_catch(strcmp(convert(1), "1") == 0);
```

3 的声音是 "Pling"

```c
    try_catch(strcmp(convert(3), "Pling") == 0);
```

5 的声音是 "Plang"

```c
    try_catch(strcmp(convert(5), "Plang") == 0);
```

7 的声音是 "Plong"

```c
    try_catch(strcmp(convert(7), "Plong") == 0);
```

6 的声音是 "Pling"

```c
    try_catch(strcmp(convert(6), "Pling") == 0);
```

8 的声音是 "8"

```c
    try_catch(strcmp(convert(8), "8") == 0);
```

9 的声音是 "Pling"

```c
    try_catch(strcmp(convert(9), "Pling") == 0);
```

10 的声音是 "Plang"

```c
    try_catch(strcmp(convert(10), "Plang") == 0);
```

14 的声音是 "Plong"

```c
    try_catch(strcmp(convert(14), "Plong") == 0);
```

15 的声音是 "PlingPlang"

```c
    try_catch(strcmp(convert(15), "PlingPlang") == 0);
```

21 的声音是 "PlingPlong"

```c
    try_catch(strcmp(convert(21), "PlingPlong") == 0);
```

25 的声音是 "Plang"

```c
    try_catch(strcmp(convert(25), "Plang") == 0);
```

27 的声音是 "Pling"

```c
    try_catch(strcmp(convert(27), "Pling") == 0);
```

35 的声音是 "PlangPlong"

```c
    try_catch(strcmp(convert(35), "PlangPlong") == 0);
```

49 的声音是 "Plong"

```c
    try_catch(strcmp(convert(49), "Plong") == 0);
```

52 的声音是 "52"

```c
    try_catch(strcmp(convert(52), "52") == 0);
```

105 的声音是 "PlingPlangPlong"

```c
    try_catch(strcmp(convert(105), "PlingPlangPlong") == 0);
```


3125 的声音是 "Plang"

```c
    try_catch(strcmp(convert(3125), "Plang") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* convert(int number) {
    char *result = malloc(sizeof(char) * 15);
    if (number % 3 == 0) {
        strcat(result, "Pling");
    }
    if (number % 5 == 0) {
        strcat(result, "Plang");
    }
    if (number % 7 == 0) {
        strcat(result, "Plong");
    }
    if (strlen(result) == 0) {
        sprintf(result, "%d", number);
    }
    return result;
}
```
