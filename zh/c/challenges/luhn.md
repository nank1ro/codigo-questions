---
language: c
exerciseType: 1
difficulty: 2
title: Luhn 校验和
---

# --description--

Luhn 算法是一种简单的校验和，用于验证身份识别号码，例如信用卡号。

在检查一个号码之前，先去掉字符串中的所有空格。只有当剩下的部分长度超过一个字符，并且原始字符串只包含数字和空格时，该字符串才是有效的。

执行检查时，从最右边的数字开始向左移动，将每隔一位的数字加倍。当加倍后得到大于 9 的数时，将其减去 9。然后把所有数字相加：只有当总和能被 10 整除时，该号码才有效。

例如，`"059"` 得到 `0`，然后 `5` 加倍为 `10`，它变成 `1`，再是 `9`。它们的和是 `10`，能被 10 整除，所以这个号码是有效的。

# --instructions--

编写一个函数 `is_valid`，它接收一个 `const char *`，当号码有效时返回 `true`，否则返回 `false`。

- `"4539 3195 0343 6467"` 通过校验和，所以结果是 `true`。
- `"8273 1232 7352 0569"` 未通过校验和，所以结果是 `false`。
- `"0"` 只有一个字符长，所以结果是 `false`。
- `"055-444-285"` 包含既不是数字也不是空格的字符，所以结果是 `false`。

函数调用示例：
```c
printf("%d\n", is_valid("095 245 88"));
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
#include <stdlib.h>
#include <string.h>
```


# --seed--

```c
bool is_valid(const char *value) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

单个数字是无效的。

```c
    try_catch(is_valid("0") == false);
```

前面带一个空格的单个数字是无效的。

```c
    try_catch(is_valid(" 0") == false);
```

号码 `"059"` 是有效的。

```c
    try_catch(is_valid("059") == true);
```

号码 `"59"` 是有效的。

```c
    try_catch(is_valid("59") == true);
```

号码 `"055 444 285"` 是有效的。

```c
    try_catch(is_valid("055 444 285") == true);
```

号码 `"055 444 286"` 是无效的。

```c
    try_catch(is_valid("055 444 286") == false);
```

号码 `"8273 1232 7352 0569"` 是无效的。

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

号码 `"4539 3195 0343 6467"` 是有效的。

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

号码 `"1 2345 6789 1234 5678 9012"` 是无效的。

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

号码 `"095 245 88"` 是有效的。

```c
    try_catch(is_valid("095 245 88") == true);
```

字母会使号码无效。

```c
    try_catch(is_valid("055a 444 285") == false);
```

短横线会使号码无效。

```c
    try_catch(is_valid("055-444-285") == false);
```

标点符号字符会使号码无效。

```c
    try_catch(is_valid(":9") == false);
```

符号会使号码无效。

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

空字符串是无效的。

```c
    try_catch(is_valid("") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool is_valid(const char *value) {
    int sum = 0;
    int count = 0;
    for (int i = (int)strlen(value) - 1; i >= 0; i--) {
        char c = value[i];
        if (c == ' ') {
            continue;
        }
        if (c < '0' || c > '9') {
            return false;
        }
        int digit = c - '0';
        if (count % 2 == 1) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        count++;
    }
    return count > 1 && sum % 10 == 0;
}
```
