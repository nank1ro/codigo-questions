---
language: c
exerciseType: 1
difficulty: 1
title: Гипотеза Коллатца
---

# --description--

Гипотеза Коллатца начинается с любого положительного целого числа `n` и повторяет одно простое правило: если `n` чётное, разделите его пополам; если `n` нечётное, замените его на `3n + 1`. Рано или поздно последовательность достигает 1.

Например, если начать с 16, последовательность будет `16 -> 8 -> 4 -> 2 -> 1`, то есть потребуется 4 шага.

Никто никогда не доказывал, что это происходит всегда, но это выполняется для каждого проверенного числа.

# --instructions--

Напишите функцию `collatzSteps`, которая принимает положительное целое число `n` и возвращает количество шагов, необходимое, чтобы достичь 1.

`collatzSteps(1)` — это 0, потому что 1 уже является концом последовательности. `collatzSteps(12)` — это 9, а `collatzSteps(27)` — 111.

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
```

# --seed--

```c
int collatzSteps(int n) {

}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

`collatzSteps(1)` должна возвращать 0, потому что 1 уже является концом последовательности.

```c
    try_catch(collatzSteps(1) == 0);
```

`collatzSteps(2)` должна возвращать 1.

```c
    try_catch(collatzSteps(2) == 1);
```

`collatzSteps(6)` должна возвращать 8.

```c
    try_catch(collatzSteps(6) == 8);
```

`collatzSteps(7)` должна возвращать 16.

```c
    try_catch(collatzSteps(7) == 16);
```

`collatzSteps(16)` должна возвращать 4.

```c
    try_catch(collatzSteps(16) == 4);
```

`collatzSteps(12)` должна возвращать 9.

```c
    try_catch(collatzSteps(12) == 9);
```

`collatzSteps(27)` должна возвращать 111.

```c
    try_catch(collatzSteps(27) == 111);
```

`collatzSteps(97)` должна возвращать 118.

```c
    try_catch(collatzSteps(97) == 118);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
int collatzSteps(int n) {
    long value = n;
    int steps = 0;
    while (value != 1) {
        if (value % 2 == 0) {
            value = value / 2;
        } else {
            value = 3 * value + 1;
        }
        steps++;
    }
    return steps;
}
```
