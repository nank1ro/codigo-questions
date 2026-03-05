---
language: c
exerciseType: 1
difficulty: 3
title: Conversor de números romanos
---

# --description--

Crie uma função que receba um inteiro positivo como parâmetro e retorne uma string contendo a representação em números romanos desse inteiro. Os números romanos modernos são escritos expressando cada dígito separadamente, começando pelo dígito mais à esquerda e pulando qualquer dígito com valor zero.

# --instructions--

Exemplos:
```
convert_to_roman(2) ➞ "II"
convert_to_roman(12) ➞ "XII"
convert_to_roman(16) ➞ "XVI"
```

- Todos os números romanos devem ser retornados em maiúsculas.
- O maior número que pode ser representado nesta notação é 3.999.

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

O número `2` deve ser igual a `II`

```c
    try_catch(strcmp(convert_to_roman(2), "II") == 0);
```

O número `12` deve ser igual a `XII`

```c
    try_catch(strcmp(convert_to_roman(12), "XII") == 0);
```

O número `16` deve ser igual a `XVI`

```c
    try_catch(strcmp(convert_to_roman(16), "XVI") == 0);
```

O número `44` deve ser igual a `XLIV`

```c
    try_catch(strcmp(convert_to_roman(44), "XLIV") == 0);
```

O número `68` deve ser igual a `LXVIII`

```c
    try_catch(strcmp(convert_to_roman(68), "LXVIII") == 0);
```

O número `400` deve ser igual a `CD`

```c
    try_catch(strcmp(convert_to_roman(400), "CD") == 0);
```

O número `798` deve ser igual a `DCCXCVIII`

```c
    try_catch(strcmp(convert_to_roman(798), "DCCXCVIII") == 0);
```

O número `1000` deve ser igual a `M`

```c
    try_catch(strcmp(convert_to_roman(1000), "M") == 0);
```

O número `3999` deve ser igual a `MMMCMXCIX`

```c
    try_catch(strcmp(convert_to_roman(3999), "MMMCMXCIX") == 0);
```

O número `649` deve ser igual a `DCXLIX`

```c
    try_catch(strcmp(convert_to_roman(649), "DCXLIX") == 0);
```

O número `1666` deve ser igual a `MDCLXVI`

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
