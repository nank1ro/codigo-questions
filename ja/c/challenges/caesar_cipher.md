---
language: c
exerciseType: 1
difficulty: 2
title: シーザー暗号
---

# --description--

ユリウス・カエサルは、暗号術の中でも最も古い手法の1つを使って、自分の私的な手紙を守っていました。その手法とは、メッセージのすべての文字を、アルファベットに沿って固定された数だけ先にある文字に置き換えるというものです。シフトが3の場合、`a`は`d`に、`b`は`e`に、`c`は`f`になります。

アルファベットは円のように振る舞うため、終わりの文字は先頭へ折り返します。シフトが3の場合、`x`は`a`に、`y`は`b`に、`z`は`c`になります。

スペース、カンマ、感嘆符、数字など、英字以外のものはすべて、暗号を通しても変更されずにそのまま通過します。

# --instructions--

メッセージ`text`と整数`shift`を受け取り、エンコードされたメッセージを返す関数`caesarCipher`を書いてください。

例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- メッセージは常に小文字なので、大文字を扱う必要はありません。
- 英字以外の文字は、その位置と値を保ちます。
- シフトが負になることはありません。シフト`0`ではメッセージはそのままになり、シフト`26`でも同じです。

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
char* caesarCipher(const char* text, int shift) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

シフト3で"hello"は"khoor"になります。

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

アルファベットの終わりが折り返されるため、"xyz"は"abc"になります。

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

シフト0ではメッセージは変わりません。

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

シフト26はアルファベットのちょうど1周なので、メッセージは変わりません。

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

句読点とスペースは変更されずに通過します。

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

空のメッセージは空のままです。

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

文字と文字の間のスペースはそのまま保持されます。

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

数字は、シフト25であっても置き換えられません。

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

シフト13で文全体がエンコードされます。

```c
    try_catch(strcmp(caesarCipher("the quick brown fox jumps over the lazy dog", 13), "gur dhvpx oebja sbk whzcf bire gur ynml qbt") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* caesarCipher(const char* text, int shift) {
    size_t length = strlen(text);
    char* result = malloc(length + 1);

    for (size_t i = 0; i < length; i++) {
        char c = text[i];
        if (c >= 'a' && c <= 'z') {
            result[i] = 'a' + (c - 'a' + shift) % 26;
        } else {
            result[i] = c;
        }
    }

    result[length] = '\0';
    return result;
}
```
