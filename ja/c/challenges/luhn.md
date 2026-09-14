---
language: c
exerciseType: 1
difficulty: 2
title: Luhnチェックサム
---

# --description--

Luhnアルゴリズムは、クレジットカード番号などの識別番号を検証するために使われるシンプルなチェックサムです。

数をチェックする前に、文字列からすべてのスペースを取り除きます。残った部分が1文字より長く、元の文字列が数字とスペースのみを含んでいる場合にのみ、その文字列は有効です。

チェックを行うには、一番右の桁から始めて左へ進み、1つおきの桁を2倍していきます。2倍した結果が9より大きい数になった場合は、そこから9を引きます。次にすべての桁を合計します。その合計が10で割り切れる場合にのみ、数は有効です。

たとえば、`"059"`は`0`、次に`5`を2倍した`10`が`1`になり、そして`9`となります。合計は`10`で10で割り切れるので、この数は有効です。

# --instructions--

`const char *`を受け取り、数が有効な場合には`true`を、そうでない場合には`false`を返す関数`is_valid`を書いてください。

- `"4539 3195 0343 6467"`はチェックサムを満たすため、結果は`true`です。
- `"8273 1232 7352 0569"`はチェックサムを満たさないため、結果は`false`です。
- `"0"`は長さが1文字しかないため、結果は`false`です。
- `"055-444-285"`には数字でもスペースでもない文字が含まれているため、結果は`false`です。

関数呼び出しの例：
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

1桁の数字は有効ではありません。

```c
    try_catch(is_valid("0") == false);
```

先頭にスペースが付いた1桁の数字は有効ではありません。

```c
    try_catch(is_valid(" 0") == false);
```

数`"059"`は有効です。

```c
    try_catch(is_valid("059") == true);
```

数`"59"`は有効です。

```c
    try_catch(is_valid("59") == true);
```

数`"055 444 285"`は有効です。

```c
    try_catch(is_valid("055 444 285") == true);
```

数`"055 444 286"`は有効ではありません。

```c
    try_catch(is_valid("055 444 286") == false);
```

数`"8273 1232 7352 0569"`は有効ではありません。

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

数`"4539 3195 0343 6467"`は有効です。

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

数`"1 2345 6789 1234 5678 9012"`は有効ではありません。

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

数`"095 245 88"`は有効です。

```c
    try_catch(is_valid("095 245 88") == true);
```

英字が1つあるだけで数は無効になります。

```c
    try_catch(is_valid("055a 444 285") == false);
```

ダッシュがあると数は無効になります。

```c
    try_catch(is_valid("055-444-285") == false);
```

句読点があると数は無効になります。

```c
    try_catch(is_valid(":9") == false);
```

記号があると数は無効になります。

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

空の文字列は有効ではありません。

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
