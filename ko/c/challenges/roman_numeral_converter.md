---
language: c
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 포함하는 문자열을 반환하는 함수를 만드십시오. 현대 로마 숫자는 가장 왼쪽 자릿수부터 시작하여 각 자릿수를 개별적으로 표현하며, 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환되어야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 숫자는 3,999입니다.

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
char* convert_to_roman(int n) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

숫자 `2`는 `II`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(2), "II") == 0);
```

숫자 `12`는 `XII`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(12), "XII") == 0);
```

숫자 `16`은 `XVI`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(16), "XVI") == 0);
```

숫자 `44`는 `XLIV`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(44), "XLIV") == 0);
```

숫자 `68`은 `LXVIII`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(68), "LXVIII") == 0);
```

숫자 `400`은 `CD`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(400), "CD") == 0);
```

숫자 `798`은 `DCCXCVIII`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(798), "DCCXCVIII") == 0);
```

숫자 `1000`은 `M`과 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(1000), "M") == 0);
```

숫자 `3999`는 `MMMCMXCIX`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(3999), "MMMCMXCIX") == 0);
```

숫자 `649`는 `DCXLIX`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(649), "DCXLIX") == 0);
```

숫자 `1666`은 `MDCLXVI`와 같아야 합니다

```c
    try_catch(strcmp(convert_to_roman(1666), "MDCLXVI") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* convert_to_roman(int n) {
    char* result = (char*)malloc(100 * sizeof(char));

    int values[13][2] = {
        {1000, "M"},
        {900, "CM"},
        {500, "D"},
        {400, "CD"},
        {100, "C"},
        {90, "XC"},
        {50, "L"},
        {40, "XL"},
        {10, "X"},
        {9, "IX"},
        {5, "V"},
        {4, "IV"},
        {1, "I"}
    };

    for (int i = 0; i < 13; i++) {
        int value = values[i][0];
        char* letter = values[i][1];

        while (n >= value) {
            strcat(result, letter);
            n -= value;
        }
    }

    return result;
}
```
