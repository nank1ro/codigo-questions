---
language: c
exerciseType: 1
difficulty: 1
title: 팬그램
---

# --description--

팬그램은 영어 알파벳의 모든 문자를 적어도 한 번씩 사용하는 문장입니다. 가장 잘 알려진 예는 "the quick brown fox jumps over the lazy dog"이며, 26개의 문자를 모두 아홉 개의 짧은 단어에 담고 있습니다.

이 검사는 대소문자를 구분하지 않으므로 `A`와 `a`는 같은 문자로 셉니다. 숫자, 문장 부호, 공백은 무시됩니다. 이들은 문자가 아니지만, 문장을 거부할 이유도 되지 않습니다.

# --instructions--

문장을 받아 그 문장이 팬그램이면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isPangram`를 작성하세요.

예시:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- 빈 문장은 팬그램이 아닙니다.
- `a`부터 `z`까지의 26개 문자만 셉니다.

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

빈 문장은 팬그램이 아니다

```c
    try_catch(isPangram("") == false);
```

고전적인 문장 "the quick brown fox jumps over the lazy dog"는 팬그램이다

```c
    try_catch(isPangram("the quick brown fox jumps over the lazy dog") == true);
```

문자 `x`가 빠진 문장은 팬그램이 아니다

```c
    try_catch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false);
```

문장 "the five boxing wizards jump quickly"는 팬그램이다

```c
    try_catch(isPangram("the five boxing wizards jump quickly") == true);
```

밑줄은 무시되므로 그 문장은 여전히 팬그램이다

```c
    try_catch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true);
```

숫자는 무시되므로 그 문장은 여전히 팬그램이다

```c
    try_catch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true);
```

숫자는 문자 `e`, `i`, `t`를 대신하지 않는다

```c
    try_catch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false);
```

대문자로 된 문장도 팬그램이다

```c
    try_catch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true);
```

알파벳의 같은 절반의 대소문자를 섞는 것만으로는 충분하지 않다

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
