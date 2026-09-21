---
language: c
exerciseType: 1
difficulty: 3
title: 괄호 짝 맞추기
---

# --description--

코드, 수식 또는 마크업을 담는 텍스트에는 괄호가 가득하며, 모든 여는 괄호에는 같은 종류의 닫는 괄호가 필요합니다. 문자열의 괄호들이 양파의 겹처럼 쌍을 이루고 중첩될 때 그 문자열은 균형이 잡혀 있다고 합니다: `{[()]}`는 균형이 잡혀 있지만, `{[(])}`는 그렇지 않습니다. 이는 그 안에 있는 둥근 괄호 쌍이 자신을 감싸고 있는 대괄호 쌍보다 먼저 닫히기 때문입니다.

여기서는 세 쌍이 대상입니다: 둥근 괄호 `()`, 대괄호 `[]`, 그리고 중괄호 `{}`입니다. 문자열에 있는 다른 모든 문자는 무시합니다. 닫는 괄호는 아직 열려 있는 괄호 중 가장 최근에 열린 괄호를 닫아야 하며, 문자열이 끝날 때 열려 있는 괄호가 남아 있어서는 안 됩니다.

# --instructions--

문자열을 받아 그 안의 모든 괄호가 서로 맞고 올바르게 중첩되어 있으면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `is_balanced`를 작성하세요.

예시:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- 빈 문자열은 균형이 잡혀 있습니다.
- 괄호가 아닌 문자는 무시합니다.
- 닫는 괄호는 아직 열려 있는 괄호 중 가장 최근에 열린 괄호와 맞아야 합니다.
- 문자열이 끝날 때 열려 있는 괄호가 남아 있으면 안 됩니다.

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

빈 문자열은 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("") == true);
```

둥근 괄호 한 쌍은 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("()") == true);
```

세 종류의 쌍이 서로 중첩되어 있으면 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("{[()]}") == true);
```

다른 텍스트와 섞인 괄호도 여전히 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

나란히 놓인 쌍들은 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("()[]{}") == true);
```

괄호가 전혀 없는 문자열은 균형이 잡혀 있습니다

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

교차된 쌍은 균형이 잡혀 있지 않습니다

```c
    try_catch(is_balanced("{[(])}") == false);
```

끝까지 닫히지 않는 여는 괄호는 균형이 잡혀 있지 않습니다

```c
    try_catch(is_balanced("(") == false);
```

여는 괄호보다 먼저 나오는 닫는 괄호는 균형이 잡혀 있지 않습니다

```c
    try_catch(is_balanced(")(") == false);
```

문자열 깊은 곳에서 교차된 쌍들은 균형이 잡혀 있지 않습니다

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

끝에 남는 닫는 괄호는 균형이 잡혀 있지 않습니다

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
