---
language: c
exerciseType: 1
difficulty: 2
title: ランレングス符号化
---

# --description--

ランレングス符号化は、圧縮のテクニックの中でも最も古いものの1つです。同じ文字を何度も書き連ねる代わりに、その文字が何回繰り返されるかを書き、その後に文字そのものを書きます。

ほとんどが空白のページをスキャンするファックスは、同じピクセルが長く続く部分に出会います。そのため、`W` が12個並んだ1行は、はるかに短い `12W` となって回線を流れていきます。文字が1度しか現れない場合は、数えても得るものがないため、その文字だけがそのままコピーされます。

# --instructions--

文字列 `text` を受け取り、ランレングス符号化した形式を返す関数 `encode_run` を書いてください。

同じ文字が2回以上続く連続した並びは、その長さを十進数で書いたものに、その文字を付けた形になります。長さ1の並びは、前に数字を付けずに、その1文字だけがそのままコピーされます。

例:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- テキストには `A` から `Z` までの大文字とスペースだけが含まれます。
- 9文字より長い並びは、十進数の回数をすべて使うため、`W` が12個なら `12W` となり、`9W3W` にはなりません。
- スペースも普通の文字です。文字とまったく同じように数えられ、エンコードされます。
- 空の文字列は空の文字列にエンコードされます。

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

空の文字列は空の文字列にエンコードされる

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

1文字だけの文字はそのままコピーされる

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

繰り返しのない文字列は変化せずにそのまま通る

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

長さ2の並びは、回数の後に文字が付いた形になる

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

並びが混ざった例 "AABCCCDEEEE" は "2AB3CD4E" になる

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

長さ12の並びは十進数の回数をすべて使うため、結果は "12W" で始まる

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

スペースの並びも文字の並びと同じようにエンコードされる

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

長さ10の並びは "10A" と書かれ、より短い2つの並びに分けられることはない

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

交互に現れる1文字はすべてそのままコピーされる

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
