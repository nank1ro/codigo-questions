---
language: c
exerciseType: 1
difficulty: 3
title: Matching brackets
---

# --description--

Text that carries code, maths or markup is full of brackets, and every opening bracket needs a closing one of the same kind. A string is balanced when its brackets pair up and nest like the layers of an onion: `{[()]}` is balanced, while `{[(])}` is not, because the round pair is closed before the square pair it sits inside.

Three pairs count here: round `()`, square `[]` and curly `{}`. Every other character in the string is ignored. A closing bracket must close the most recently opened bracket that is still open, and when the string ends no bracket may be left open.

# --instructions--

Write a function `is_balanced` that takes a string and returns `true` when all the brackets in it are matched and properly nested, and `false` otherwise.

Examples:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- An empty string is balanced.
- Characters that are not brackets are ignored.
- A closing bracket must match the most recently opened bracket that is still open.
- No bracket may be left open when the string ends.

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

An empty string is balanced

```c
    try_catch(is_balanced("") == true);
```

A single pair of round brackets is balanced

```c
    try_catch(is_balanced("()") == true);
```

The three kinds of pair nested inside each other are balanced

```c
    try_catch(is_balanced("{[()]}") == true);
```

Brackets mixed with other text are still balanced

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

Pairs placed side by side are balanced

```c
    try_catch(is_balanced("()[]{}") == true);
```

A string without any brackets is balanced

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

A crossed pair is not balanced

```c
    try_catch(is_balanced("{[(])}") == false);
```

An opening bracket that is never closed is not balanced

```c
    try_catch(is_balanced("(") == false);
```

A closing bracket before any opening one is not balanced

```c
    try_catch(is_balanced(")(") == false);
```

Crossed pairs deeper in the string are not balanced

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

A closing bracket left over at the end is not balanced

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
