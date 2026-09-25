---
language: c
exerciseType: 1
difficulty: 2
title: 런 렝스 인코딩
---

# --description--

런 렝스 인코딩은 가장 오래된 압축 기법 중 하나입니다: 같은 문자를 계속 반복해서 쓰는 대신, 몇 번 반복되는지를 먼저 쓰고 그다음에 문자 자신을 씁니다.

거의 빈 페이지를 스캔하는 팩스 기계는 길게 이어지는 동일한 픽셀을 만나므로, 열두 개의 `W`가 이룬 한 행은 훨씬 짧은 `12W`로 전송됩니다. 문자가 한 번만 나타나면 개수를 세서 얻는 것이 없으므로 문자 하나만 그대로 복사됩니다.

# --instructions--

문자열 `text`를 받아 런 렝스 인코딩된 형태를 반환하는 함수 `encode_run`을(를) 작성하세요.

같은 문자가 두 번 이상 반복되는 모든 런은 런의 길이를 십진수로 쓴 것 뒤에 그 문자를 붙인 형태가 됩니다. 길이가 1인 런은 앞에 숫자 없이 문자 하나만 그대로 복사됩니다.

예시:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- 텍스트에는 `A`부터 `Z`까지의 대문자와 공백만 포함됩니다.
- 아홉 글자보다 긴 런은 전체 십진수 개수를 사용하므로, 열두 개의 `W`는 `12W`가 되며 절대 `9W3W`가 되지 않습니다.
- 공백도 일반 문자입니다. 공백은 글자와 똑같이 개수를 세고 인코딩합니다.
- 빈 문자열은 빈 문자열로 인코딩됩니다.

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

빈 문자열은 빈 문자열로 인코딩됩니다

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

문자 하나는 그대로 자기 자신으로 복사됩니다

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

반복이 없는 문자열은 아무 변화 없이 그대로 통과합니다

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

길이가 2인 런은 개수 뒤에 문자를 붙인 형태가 됩니다

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

뒤섞인 예시 "AABCCCDEEEE"는 "2AB3CD4E"가 됩니다

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

길이가 12인 런은 전체 십진수 개수를 사용하므로 결과는 "12W"로 시작합니다

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

공백의 런도 글자의 런과 똑같이 인코딩됩니다

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

길이가 10인 런은 "10A"로 쓰이며 두 개의 더 짧은 런으로 쓰이지 않습니다

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

번갈아 나타나는 문자들은 하나하나 모두 그대로 자기 자신으로 복사됩니다

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
