---
language: c
exerciseType: 1
difficulty: 3
title: Convertitore numerico romano
---

# --description--

Crea una funzione che prenda come parametro un numero intero positivo e restituisca una stringa contenente la rappresentazione in numeri romani di quel numero intero. I numeri romani moderni sono scritti esprimendo ogni cifra separatamente, partendo dalla cifra più a sinistra e saltando qualsiasi cifra con valore zero.

# --instructions--

Esempi:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Tutti i numeri romani devono essere riportati in maiuscolo.
- Il numero più grande che può essere rappresentato con questa notazione è 3.999.

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

Il numero `2` deve essere uguale a `II` 

```c
    try_catch(strcmp(convert_to_roman(2), "II") == 0);
```

Il numero `12` deve essere uguale a `XII`

```c
    try_catch(strcmp(convert_to_roman(12), "XII") == 0);
```

Il numero `16` deve essere uguale a `XVI`

```c
    try_catch(strcmp(convert_to_roman(16), "XVI") == 0);
```

Il numero `44` deve essere uguale a `XLIV`

```c
    try_catch(strcmp(convert_to_roman(44), "XLIV") == 0);
```

Il numero `68` deve essere uguale a `LXVIII`

```c
    try_catch(strcmp(convert_to_roman(68), "LXVIII") == 0);
```

Il numero `400` deve essere uguale a `CD`

```c
    try_catch(strcmp(convert_to_roman(400), "CD") == 0);
```

Il numero `798` deve essere uguale a `DCCXCVIII`

```c
    try_catch(strcmp(convert_to_roman(798), "DCCXCVIII") == 0);
```

Il numero `1000` deve essere uguale a `M`

```c
    try_catch(strcmp(convert_to_roman(1000), "M") == 0);
```

Il numero `3999` deve essere uguale a `MMMCMXCIX`

```c
    try_catch(strcmp(convert_to_roman(3999), "MMMCMXCIX") == 0);
```

Il numero `649` deve essere uguale a `DCXLIX`

```c
    try_catch(strcmp(convert_to_roman(649), "DCXLIX") == 0);
```

Il numero `1666` deve essere uguale a `MDCLXVI`

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
