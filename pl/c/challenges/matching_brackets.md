---
language: c
exerciseType: 1
difficulty: 3
title: Pasujące nawiasy
---

# --description--

Tekst zawierający kod, zapis matematyczny czy znaczniki jest pełen nawiasów, a każdy nawias otwierający potrzebuje nawiasu zamykającego tego samego rodzaju. Ciąg znaków jest zrównoważony, gdy jego nawiasy tworzą pary i zagnieżdżają się jak warstwy cebuli: `{[()]}` jest zrównoważony, natomiast `{[(])}` już nie, ponieważ para okrągła zostaje zamknięta przed parą kwadratową, wewnątrz której się znajduje.

Liczą się tutaj trzy pary: okrągła `()`, kwadratowa `[]` i klamrowa `{}`. Każdy inny znak w ciągu jest ignorowany. Nawias zamykający musi zamykać ostatnio otwarty nawias, który wciąż jest otwarty, a gdy ciąg się kończy, żaden nawias nie może pozostać otwarty.

# --instructions--

Napisz funkcję `is_balanced`, która przyjmuje ciąg znaków i zwraca `true`, gdy wszystkie zawarte w niej nawiasy są sparowane i poprawnie zagnieżdżone, a w przeciwnym razie zwraca `false`.

Przykłady:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- Pusty ciąg znaków jest zrównoważony.
- Znaki, które nie są nawiasami, są ignorowane.
- Nawias zamykający musi pasować do ostatnio otwartego nawiasu, który wciąż jest otwarty.
- Żaden nawias nie może pozostać otwarty, gdy ciąg znaków się kończy.

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

Pusty ciąg znaków jest zrównoważony

```c
    try_catch(is_balanced("") == true);
```

Pojedyncza para nawiasów okrągłych jest zrównoważona

```c
    try_catch(is_balanced("()") == true);
```

Trzy rodzaje par zagnieżdżone jeden w drugim są zrównoważone

```c
    try_catch(is_balanced("{[()]}") == true);
```

Nawiasy przeplatane innym tekstem nadal są zrównoważone

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

Pary ustawione obok siebie są zrównoważone

```c
    try_catch(is_balanced("()[]{}") == true);
```

Ciąg znaków bez żadnych nawiasów jest zrównoważony

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

Skrzyżowana para nawiasów nie jest zrównoważona

```c
    try_catch(is_balanced("{[(])}") == false);
```

Nawias otwierający, który nigdy nie zostaje zamknięty, nie jest zrównoważony

```c
    try_catch(is_balanced("(") == false);
```

Nawias zamykający pojawiający się przed jakimkolwiek nawiasem otwierającym nie jest zrównoważony

```c
    try_catch(is_balanced(")(") == false);
```

Skrzyżowane pary głębiej w ciągu znaków nie są zrównoważone

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

Nawias zamykający pozostawiony na końcu nie jest zrównoważony

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
