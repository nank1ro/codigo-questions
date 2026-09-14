---
language: c
exerciseType: 1
difficulty: 1
title: パングラム
---

# --description--

パングラムとは、英語のアルファベットのすべての文字を少なくとも1回使う文のことです。最もよく知られている例は "the quick brown fox jumps over the lazy dog" で、26文字すべてを9つの短い単語に収めています。

この判定は大文字と小文字を区別しないため、`A` と `a` は同じ文字として数えます。数字、句読点、スペースは無視されます。これらは文字ではありませんが、文を却下する理由にもなりません。

# --instructions--

文を受け取り、その文がパングラムなら `true` を、そうでなければ `false` を返す関数 `isPangram` を書いてください。

例:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 空の文はパングラムではありません。
- `a` から `z` までの26文字だけが数えられます。

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
bool isPangram(const char* sentence) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

空の文はパングラムではない

```c
    try_catch(isPangram("") == false);
```

古典的な文 "the quick brown fox jumps over the lazy dog" はパングラムである

```c
    try_catch(isPangram("the quick brown fox jumps over the lazy dog") == true);
```

文字 `x` が欠けている文はパングラムではない

```c
    try_catch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false);
```

文 "the five boxing wizards jump quickly" はパングラムである

```c
    try_catch(isPangram("the five boxing wizards jump quickly") == true);
```

アンダースコアは無視されるので、その文は依然としてパングラムである

```c
    try_catch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true);
```

数字は無視されるので、その文は依然としてパングラムである

```c
    try_catch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true);
```

数字は文字 `e`、`i`、`t` の代わりにはならない

```c
    try_catch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false);
```

大文字の文もパングラムである

```c
    try_catch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true);
```

アルファベットの同じ半分の大文字と小文字を混ぜるだけでは足りない

```c
    try_catch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool isPangram(const char* sentence) {
    bool seen[26] = {false};
    int found = 0;

    for (int i = 0; sentence[i] != '\0'; i++) {
        char c = sentence[i];
        if (c >= 'A' && c <= 'Z') {
            c = c + ('a' - 'A');
        }
        if (c >= 'a' && c <= 'z' && !seen[c - 'a']) {
            seen[c - 'a'] = true;
            found++;
        }
    }

    return found == 26;
}
```
