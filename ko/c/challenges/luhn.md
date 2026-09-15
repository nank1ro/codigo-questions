---
language: c
exerciseType: 1
difficulty: 2
title: Luhn 체크섬
---

# --description--

Luhn 알고리즘은 신용카드 번호와 같은 식별 번호를 검증하는 데 사용되는 간단한 체크섬입니다.

수를 검사하기 전에 문자열에서 모든 공백을 제거합니다. 남은 부분이 한 문자보다 길고 원래 문자열이 숫자와 공백만을 담고 있을 때만 그 문자열은 유효합니다.

검사를 수행하려면 가장 오른쪽 자릿수부터 시작하여 왼쪽으로 이동하면서 한 칸 건너있는 자릿수마다 2배를 합니다. 2배한 값이 9보다 크면 9를 뺍니다. 그다음 모든 자릿수를 더합니다. 이 합계가 10으로 나누어떨어질 때만 그 수는 유효합니다.

예를 들어 `"059"`는 `0`이고, 그다음 `5`를 2배한 `10`은 `1`이 되며, 마지막은 `9`입니다. 이들의 합은 `10`이고 10으로 나누어떨어지므로 이 수는 유효합니다.

# --instructions--

`const char *`를 받아 수가 유효하면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `is_valid`를 작성하세요.

- `"4539 3195 0343 6467"`은 체크섬을 통과하므로 결과는 `true`입니다.
- `"8273 1232 7352 0569"`는 체크섬을 통과하지 못하므로 결과는 `false`입니다.
- `"0"`은 길이가 한 문자뿐이므로 결과는 `false`입니다.
- `"055-444-285"`에는 숫자나 공백이 아닌 문자가 포함되어 있으므로 결과는 `false`입니다.

함수 호출 예시:
```c
printf("%d\n", is_valid("095 245 88"));
// true 출력
```

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
bool is_valid(const char *value) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

한 자리 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid("0") == false);
```

앞에 공백이 있는 한 자리 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid(" 0") == false);
```

숫자 `"059"`는 유효합니다.

```c
    try_catch(is_valid("059") == true);
```

숫자 `"59"`는 유효합니다.

```c
    try_catch(is_valid("59") == true);
```

숫자 `"055 444 285"`는 유효합니다.

```c
    try_catch(is_valid("055 444 285") == true);
```

숫자 `"055 444 286"`은 유효하지 않습니다.

```c
    try_catch(is_valid("055 444 286") == false);
```

숫자 `"8273 1232 7352 0569"`는 유효하지 않습니다.

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

숫자 `"4539 3195 0343 6467"`은 유효합니다.

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

숫자 `"1 2345 6789 1234 5678 9012"`는 유효하지 않습니다.

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

숫자 `"095 245 88"`는 유효합니다.

```c
    try_catch(is_valid("095 245 88") == true);
```

영문자가 있으면 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid("055a 444 285") == false);
```

대시가 있으면 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid("055-444-285") == false);
```

문장 부호가 있으면 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid(":9") == false);
```

기호가 있으면 숫자는 유효하지 않습니다.

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

빈 문자열은 유효하지 않습니다.

```c
    try_catch(is_valid("") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool is_valid(const char *value) {
    int sum = 0;
    int count = 0;
    for (int i = (int)strlen(value) - 1; i >= 0; i--) {
        char c = value[i];
        if (c == ' ') {
            continue;
        }
        if (c < '0' || c > '9') {
            return false;
        }
        int digit = c - '0';
        if (count % 2 == 1) {
            digit *= 2;
            if (digit > 9) {
                digit -= 9;
            }
        }
        sum += digit;
        count++;
    }
    return count > 1 && sum % 10 == 0;
}
```
