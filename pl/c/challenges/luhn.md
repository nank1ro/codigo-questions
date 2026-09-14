---
language: c
exerciseType: 1
difficulty: 2
title: Suma kontrolna Luhna
---

# --description--

Algorytm Luhna to prosta suma kontrolna służąca do sprawdzania poprawności numerów identyfikacyjnych, takich jak numery kart kredytowych.

Przed sprawdzeniem numeru usuń wszystkie spacje z ciągu znaków. Ciąg znaków jest poprawny tylko wtedy, gdy to, co zostało, jest dłuższe niż jeden znak, a oryginalny ciąg znaków zawiera wyłącznie cyfry i spacje.

Aby wykonać sprawdzenie, zacznij od skrajnie prawej cyfry i przesuwaj się w lewo, podwajając co drugą cyfrę. Gdy podwojenie da liczbę większą niż 9, odejmij od niej 9. Następnie zsumuj wszystkie cyfry: numer jest poprawny tylko wtedy, gdy suma jest podzielna przez 10.

Na przykład `"059"` daje `0`, potem podwojone `5` to `10`, które staje się `1`, a następnie `9`. Ich suma wynosi `10`, czyli liczbę podzielną przez 10, więc numer jest poprawny.

# --instructions--

Napisz funkcję `is_valid`, która przyjmuje `const char *` i zwraca `true`, gdy numer jest poprawny, a `false` w przeciwnym razie.

- `"4539 3195 0343 6467"` przechodzi sumę kontrolną, więc wynik to `true`.
- `"8273 1232 7352 0569"` nie przechodzi sumy kontrolnej, więc wynik to `false`.
- `"0"` ma długość tylko jednego znaku, więc wynik to `false`.
- `"055-444-285"` zawiera znak, który nie jest cyfrą ani spacją, więc wynik to `false`.

Przykład wywołania funkcji:
```c
printf("%d\n", is_valid("095 245 88"));
// prints true
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

Pojedyncza cyfra nie jest poprawna.

```c
    try_catch(is_valid("0") == false);
```

Pojedyncza cyfra ze spacją na początku nie jest poprawna.

```c
    try_catch(is_valid(" 0") == false);
```

Numer `"059"` jest poprawny.

```c
    try_catch(is_valid("059") == true);
```

Numer `"59"` jest poprawny.

```c
    try_catch(is_valid("59") == true);
```

Numer `"055 444 285"` jest poprawny.

```c
    try_catch(is_valid("055 444 285") == true);
```

Numer `"055 444 286"` nie jest poprawny.

```c
    try_catch(is_valid("055 444 286") == false);
```

Numer `"8273 1232 7352 0569"` nie jest poprawny.

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

Numer `"4539 3195 0343 6467"` jest poprawny.

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

Numer `"1 2345 6789 1234 5678 9012"` nie jest poprawny.

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

Numer `"095 245 88"` jest poprawny.

```c
    try_catch(is_valid("095 245 88") == true);
```

Litera powoduje, że numer jest niepoprawny.

```c
    try_catch(is_valid("055a 444 285") == false);
```

Myślniki powodują, że numer jest niepoprawny.

```c
    try_catch(is_valid("055-444-285") == false);
```

Znak interpunkcyjny powoduje, że numer jest niepoprawny.

```c
    try_catch(is_valid(":9") == false);
```

Symbole powodują, że numer jest niepoprawny.

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

Pusty ciąg znaków nie jest poprawny.

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
