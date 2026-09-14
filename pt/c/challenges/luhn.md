---
language: c
exerciseType: 1
difficulty: 2
title: Checksum de Luhn
---

# --description--

O algoritmo de Luhn é um checksum simples usado para validar números de identificação, como números de cartão de crédito.

Antes de verificar um número, remova todos os espaços da string. A string só é válida se o que restar tiver mais de um caractere e se a string original contiver nada além de dígitos e espaços.

Para fazer a verificação, comece pelo dígito mais à direita e avance para a esquerda, dobrando cada segundo dígito. Quando a duplicação produzir um número maior que 9, subtraia 9 dele. Em seguida, some todos os dígitos: o número só é válido se a soma for divisível por 10.

Por exemplo, `"059"` resulta em `0`, depois `5` dobrado é `10`, que se torna `1`, e depois `9`. A soma deles é `10`, que é divisível por 10, então o número é válido.

# --instructions--

Escreva uma função `is_valid` que recebe um `const char *` e retorna `true` quando o número é válido, `false` caso contrário.

- `"4539 3195 0343 6467"` passa no checksum, então o resultado é `true`.
- `"8273 1232 7352 0569"` falha no checksum, então o resultado é `false`.
- `"0"` tem apenas um caractere, então o resultado é `false`.
- `"055-444-285"` contém um caractere que não é um dígito nem um espaço, então o resultado é `false`.

Exemplo de chamada de função:
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

Um único dígito não é válido.

```c
    try_catch(is_valid("0") == false);
```

Um único dígito com um espaço à esquerda não é válido.

```c
    try_catch(is_valid(" 0") == false);
```

O número `"059"` é válido.

```c
    try_catch(is_valid("059") == true);
```

O número `"59"` é válido.

```c
    try_catch(is_valid("59") == true);
```

O número `"055 444 285"` é válido.

```c
    try_catch(is_valid("055 444 285") == true);
```

O número `"055 444 286"` não é válido.

```c
    try_catch(is_valid("055 444 286") == false);
```

O número `"8273 1232 7352 0569"` não é válido.

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

O número `"4539 3195 0343 6467"` é válido.

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

O número `"1 2345 6789 1234 5678 9012"` não é válido.

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

O número `"095 245 88"` é válido.

```c
    try_catch(is_valid("095 245 88") == true);
```

Uma letra torna o número inválido.

```c
    try_catch(is_valid("055a 444 285") == false);
```

Travessões tornam o número inválido.

```c
    try_catch(is_valid("055-444-285") == false);
```

Um caractere de pontuação torna o número inválido.

```c
    try_catch(is_valid(":9") == false);
```

Símbolos tornam o número inválido.

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

Uma string vazia não é válida.

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
