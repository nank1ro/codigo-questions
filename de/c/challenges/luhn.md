---
language: c
exerciseType: 1
difficulty: 2
title: Luhn-Prüfsumme
---

# --description--

Der Luhn-Algorithmus ist eine einfache Prüfsumme, die zur Überprüfung von Identifikationsnummern wie Kreditkartennummern verwendet wird.

Bevor Sie eine Zahl überprüfen, entfernen Sie alle Leerzeichen aus dem String. Der String ist nur gültig, wenn der übrig gebliebene Teil länger als ein Zeichen ist und der ursprüngliche String nichts außer Ziffern und Leerzeichen enthält.

Um die Überprüfung durchzuführen, beginnen Sie bei der äußersten rechten Ziffer und bewegen Sie sich nach links, wobei Sie jede zweite Ziffer verdoppeln. Wenn das Verdoppeln eine Zahl größer als 9 ergibt, subtrahieren Sie 9 davon. Addieren Sie dann alle Ziffern: Die Zahl ist nur gültig, wenn die Summe durch 10 teilbar ist.

Zum Beispiel ergibt `"059"` `0`, dann ergibt `5` verdoppelt `10`, was zu `1` wird, dann `9`. Ihre Summe ist `10`, was durch 10 teilbar ist, also ist die Zahl gültig.

# --instructions--

Schreiben Sie eine Funktion `is_valid`, die einen `const char *` entgegennimmt und `true` zurückgibt, wenn die Zahl gültig ist, andernfalls `false`.

- `"4539 3195 0343 6467"` besteht die Prüfsumme, also ist das Ergebnis `true`.
- `"8273 1232 7352 0569"` besteht die Prüfsumme nicht, also ist das Ergebnis `false`.
- `"0"` ist nur ein Zeichen lang, also ist das Ergebnis `false`.
- `"055-444-285"` enthält ein Zeichen, das weder eine Ziffer noch ein Leerzeichen ist, also ist das Ergebnis `false`.

Beispiel eines Funktionsaufrufs:
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

Eine einzelne Ziffer ist nicht gültig.

```c
    try_catch(is_valid("0") == false);
```

Eine einzelne Ziffer mit einem führenden Leerzeichen ist nicht gültig.

```c
    try_catch(is_valid(" 0") == false);
```

Die Zahl `"059"` ist gültig.

```c
    try_catch(is_valid("059") == true);
```

Die Zahl `"59"` ist gültig.

```c
    try_catch(is_valid("59") == true);
```

Die Zahl `"055 444 285"` ist gültig.

```c
    try_catch(is_valid("055 444 285") == true);
```

Die Zahl `"055 444 286"` ist not gültig.

```c
    try_catch(is_valid("055 444 286") == false);
```

Die Zahl `"8273 1232 7352 0569"` ist not gültig.

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

Die Zahl `"4539 3195 0343 6467"` ist gültig.

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

Die Zahl `"1 2345 6789 1234 5678 9012"` ist not gültig.

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

Die Zahl `"095 245 88"` ist gültig.

```c
    try_catch(is_valid("095 245 88") == true);
```

Ein Buchstabe macht die Zahl ungültig.

```c
    try_catch(is_valid("055a 444 285") == false);
```

Bindestriche machen die Zahl ungültig.

```c
    try_catch(is_valid("055-444-285") == false);
```

Ein Satzeichen macht die Zahl ungültig.

```c
    try_catch(is_valid(":9") == false);
```

Symbole machen die Zahl ungültig.

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

Ein leerer String ist nicht gültig.

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
