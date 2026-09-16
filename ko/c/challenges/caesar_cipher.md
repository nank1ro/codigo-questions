---
language: c
exerciseType: 1
difficulty: 2
title: 카이사르 암호
---

# --description--

율리우스 카이사르는 암호학에서 가장 오래된 기법 중 하나로 자신의 개인 편지를 보호했습니다. 그는 메시지의 모든 글자를 알파벳에서 고정된 칸수만큼 뒤에 있는 글자로 바꿨습니다. 이동 거리가 3이면 `a`는 `d`가 되고, `b`는 `e`가 되며, `c`는 `f`가 됩니다.

알파벳은 원처럼 동작하기 때문에 끝에 있는 글자는 다시 처음으로 돌아갑니다. 이동 거리가 3이면 `x`는 `a`가 되고, `y`는 `b`가 되며, `z`는 `c`가 됩니다.

공백, 쉼표, 느낌표, 숫자처럼 글자가 아닌 것들은 이 암호를 거쳐도 그대로 남습니다.

# --instructions--

메시지 `text`와 정수 `shift`를 받아 암호화된 메시지를 반환하는 함수 `caesarCipher`를 작성하세요.

예시:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 메시지는 항상 소문자이므로 대문자를 다룰 필요는 없습니다.
- 글자가 아닌 문자는 자리와 값을 그대로 유지합니다.
- 이동 거리는 절대 음수가 아닙니다. 이동 거리가 `0`이면 메시지는 바뀌지 않으며, `26`이어도 마찬가지입니다.

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

이동 거리가 3이면 "hello"는 "khoor"가 됩니다

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

알파벳의 끝은 처음으로 돌아가므로 "xyz"는 "abc"가 됩니다

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

이동 거리가 0이면 메시지는 바뀌지 않습니다

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

이동 거리가 26이면 알파벳을 한 바퀴 도는 것이므로 메시지는 바뀌지 않습니다

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

문장 부호와 공백은 바뀌지 않고 그대로 통과합니다

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

빈 메시지는 빈 상태로 남습니다

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

글자 사이의 공백은 그대로 유지됩니다

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

이동 거리가 25여도 숫자는 이동하지 않습니다

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

이동 거리가 13이면 문장 전체가 암호화됩니다

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
