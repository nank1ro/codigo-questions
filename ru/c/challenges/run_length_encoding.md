---
language: c
exerciseType: 1
difficulty: 2
title: Кодирование длин серий
---

# --description--

Кодирование длин серий — один из старейших приёмов сжатия: вместо того чтобы писать один и тот же символ снова и снова, вы записываете, сколько раз он повторяется, а затем сам символ.

Факсимильный аппарат, сканирующий почти пустую страницу, встречает длинные участки одинаковых пикселей, поэтому ряд из двенадцати `W` передаётся по линии как гораздо более короткое `12W`. Когда символ встречается лишь однажды, считать его незачем, поэтому он копируется сам по себе.

# --instructions--

Напишите функцию `encode_run`, которая принимает строку `text` и возвращает её закодированное представление.

Каждая серия одного и того же символа, повторённого два или более раз, превращается в длину серии, записанную в десятичном виде, за которой следует сам символ. Серия длины один копируется как одиночный символ, без числа перед ним.

Примеры:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Текст содержит только заглавные буквы от `A` до `Z` и пробелы.
- Серия длиннее девяти символов записывается своим полным десятичным количеством, поэтому двенадцать `W` превращаются в `12W`, но никогда в `9W3W`.
- Пробелы — обычные символы: они считаются и кодируются точно так же, как буквы.
- Пустая строка кодируется в пустую строку.

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

Пустая строка кодируется в пустую строку

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

Одиночный символ копируется без изменений

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

Строка без повторов проходит через кодирование без изменений

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

Серия из двух символов превращается в число, за которым следует символ

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

Смешанный пример "AABCCCDEEEE" превращается в "2AB3CD4E"

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

Серия из двенадцати записывается своим полным десятичным количеством, поэтому результат начинается с "12W"

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

Серии пробелов кодируются точно так же, как серии букв

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

Серия из десяти записывается как "10A", но никогда как две более короткие серии

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

Чередующиеся одиночные символы копируются без изменений

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
