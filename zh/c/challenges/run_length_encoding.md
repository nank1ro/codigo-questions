---
language: c
exerciseType: 1
difficulty: 2
title: 游程编码
---

# --description--

游程编码是最古老的压缩技巧之一：与其把同一个字符一遍又一遍地写出来，不如先写下它重复的次数，再写下这个字符本身。

一台传真机在扫描一张大部分空白的页面时，会遇到长长的相同像素段，因此一排十二个 `W` 在线路上传输时会变成短得多的 `12W`。当某个字符只出现一次时，统计次数毫无意义，所以它会被单独原样复制过去。

# --instructions--

编写一个函数 `encode_run`，它接收一个字符串 `text`，并返回其游程编码后的形式。

每一段由同一字符重复两次或更多次构成的游程，都会变成该游程长度的十进制数字，后面跟上这个字符。长度为一的游程则只复制为单个字符，前面不带任何数字。

示例：
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- 文本只包含从 `A` 到 `Z` 的大写字母和空格。
- 超过九个字符的游程会使用完整的十进制计数，因此十二个 `W` 会变成 `12W`，而绝不会写成 `9W3W`。
- 空格是普通字符：它们的计数和编码方式与字母完全相同。
- 空字符串编码后仍是空字符串。

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
char* encode_run(const char* text) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

空字符串编码后仍是空字符串

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

单个字符会被原样复制

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

没有重复字符的字符串会原样通过，不做任何改变

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

长度为二的游程会变成计数后跟字符

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

混合示例 "AABCCCDEEEE" 变成 "2AB3CD4E"

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

长度为十二的游程会使用完整的十进制计数，因此结果以 "12W" 开头

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

空格游程的编码方式与字母游程完全相同

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

长度为十的游程会写成 "10A"，绝不会写成两个更短的游程

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

交替出现的单个字符都会被原样复制

```c
    try_catch(strcmp(encode_run("ABABAB"), "ABABAB") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* encode_run(const char* text) {
    size_t length = strlen(text);
    char* result = malloc(length * 2 + 2);
    size_t out = 0;
    size_t i = 0;

    while (i < length) {
        size_t run = 1;
        while (i + run < length && text[i + run] == text[i]) {
            run++;
        }
        if (run > 1) {
            out += sprintf(result + out, "%d", (int)run);
        }
        result[out++] = text[i];
        i += run;
    }

    result[out] = '\0';
    return result;
}
```
