---
language: c
exerciseType: 1
difficulty: 2
title: Шифр Цезаря
---

# --description--

Юлий Цезарь защищал свои личные письма одним из старейших приёмов криптографии: он заменял каждую букву сообщения буквой, отстоящей от исходной на фиксированное число позиций дальше по алфавиту. При сдвиге 3 `a` становится `d`, `b` становится `e`, а `c` становится `f`.

Алфавит замкнут в круг, поэтому буквы в его конце возвращаются к началу: при сдвиге 3 `x` становится `a`, `y` становится `b`, а `z` становится `c`.

Всё, что не является буквой — например, пробел, запятая, восклицательный знак или цифра, — проходит через шифр без изменений.

# --instructions--

Напишите функцию `caesarCipher`, которая принимает сообщение `text` и целое число `shift`, и возвращает закодированное сообщение.

Примеры:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Сообщение всегда записано строчными буквами, поэтому вам никогда не придётся иметь дело с заглавными буквами.
- Символы, не являющиеся буквами, сохраняют свою позицию и своё значение.
- Сдвиг никогда не бывает отрицательным. Сдвиг `0` оставляет сообщение без изменений, как и сдвиг `26`.

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

Сдвиг 3 превращает "hello" в "khoor"

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

Конец алфавита замыкается по кругу, поэтому "xyz" становится "abc"

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

Сдвиг 0 оставляет сообщение без изменений

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

Сдвиг 26 — это полный оборот алфавита, поэтому сообщение не меняется

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

Знаки препинания и пробелы проходят через шифр без изменений

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

Пустое сообщение остаётся пустым

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

Пробелы между отдельными буквами сохраняются

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

Цифры не сдвигаются, даже при сдвиге 25

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

Сдвиг 13 кодирует целое предложение

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
