---
language: c
exerciseType: 1
difficulty: 2
title: Szyfr Cezara
---

# --description--

Juliusz Cezar chronił swoje prywatne listy jedną z najstarszych sztuczek kryptografii: zastępował każdą literę wiadomości literą oddaloną o stałą liczbę pozycji w alfabecie. Przy przesunięciu o 3 `a` staje się `d`, `b` staje się `e`, a `c` staje się `f`.

Alfabet zachowuje się jak okrąg, więc litery z końca zawijają się z powrotem do początku: przy przesunięciu o 3 `x` staje się `a`, `y` staje się `b`, a `z` staje się `c`.

Wszystko, co nie jest literą, na przykład spacja, przecinek, wykrzyknik albo cyfra, przechodzi przez szyfr bez zmian.

# --instructions--

Napisz funkcję `caesarCipher`, która przyjmuje wiadomość `text` i liczbę całkowitą `shift`, i zwraca zaszyfrowaną wiadomość.

Przykłady:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Wiadomość zawsze składa się z małych liter, więc nie musisz przejmować się wielkimi literami.
- Znaki, które nie są literami, zachowują swoje miejsce i swoją wartość.
- Przesunięcie nigdy nie jest ujemne. Przesunięcie o `0` pozostawia wiadomość bez zmian, podobnie jak przesunięcie o `26`.

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

Przesunięcie o 3 zamienia "hello" w "khoor"

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

Koniec alfabetu zawija się do początku, więc "xyz" staje się "abc"

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

Przesunięcie o 0 pozostawia wiadomość bez zmian

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

Przesunięcie o 26 to pełny obrót alfabetu, więc wiadomość pozostaje bez zmian

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

Znaki interpunkcyjne i spacje przechodzą bez zmian

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

Pusta wiadomość pozostaje pusta

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

Spacje między pojedynczymi literami są zachowane

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

Cyfry nie są przesuwane, nawet przy przesunięciu o 25

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

Przesunięcie o 13 szyfruje całe zdanie

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
