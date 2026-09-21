---
language: c
exerciseType: 1
difficulty: 3
title: 括弧の対応
---

# --description--

コードや数式、マークアップを含むテキストには括弧が数多く登場し、開き括弧にはどれも同じ種類の閉じ括弧が必要です。括弧が対をなして玉ねぎの層のように入れ子になっていくとき、その文字列はバランスが取れています。`{[()]}` はバランスが取れていますが、`{[(])}` はバランスが取れていません。丸括弧の組が、その丸括弧が内側に収まっている角括弧の組よりも先に閉じられているからです。

ここで数えるのは、丸括弧 `()`、角括弧 `[]`、波括弧 `{}` の3組です。文字列内のそれ以外の文字はすべて無視されます。閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧を閉じなければならず、文字列が終わるときに開いたままの括弧が残っていてはいけません。

# --instructions--

文字列を受け取り、その中のすべての括弧が対応して正しく入れ子になっていれば `true` を、そうでなければ `false` を返す関数 `isBalanced` を書いてください。

例:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- 空の文字列はバランスが取れています。
- 括弧以外の文字は無視されます。
- 閉じ括弧は、まだ開いている括弧の中で最も新しく開かれた括弧と対応しなければなりません。
- 文字列が終わるとき、開いたままの括弧が残っていてはいけません。

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
bool is_balanced(const char* text) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

空の文字列はバランスが取れている

```c
    try_catch(is_balanced("") == true);
```

丸括弧1組だけの文字列はバランスが取れている

```c
    try_catch(is_balanced("()") == true);
```

3種類の組が互いに入れ子になった文字列はバランスが取れている

```c
    try_catch(is_balanced("{[()]}") == true);
```

括弧が他のテキストと混ざっていてもバランスが取れている

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

組が横に並んでいてもバランスが取れている

```c
    try_catch(is_balanced("()[]{}") == true);
```

括弧をまったく含まない文字列はバランスが取れている

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

交差した組はバランスが取れていない

```c
    try_catch(is_balanced("{[(])}") == false);
```

閉じられないままの開き括弧はバランスが取れていない

```c
    try_catch(is_balanced("(") == false);
```

開き括弧より先に来る閉じ括弧はバランスが取れていない

```c
    try_catch(is_balanced(")(") == false);
```

文字列の奥で交差した組はバランスが取れていない

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

最後に余った閉じ括弧はバランスが取れていない

```c
    try_catch(is_balanced("())") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool is_balanced(const char* text) {
    size_t length = strlen(text);
    char stack[length + 1];
    size_t top = 0;

    for (size_t i = 0; i < length; i++) {
        char current = text[i];

        if (current == '(' || current == '[' || current == '{') {
            stack[top++] = current;
        } else if (current == ')' || current == ']' || current == '}') {
            if (top == 0) {
                return false;
            }

            char opening = stack[--top];
            if ((current == ')' && opening != '(') ||
                (current == ']' && opening != '[') ||
                (current == '}' && opening != '{')) {
                return false;
            }
        }
    }

    return top == 0;
}
```
