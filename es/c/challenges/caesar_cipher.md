---
language: c
exerciseType: 1
difficulty: 2
title: Cifrado César
---

# --description--

Julio César protegía sus cartas privadas con uno de los trucos más antiguos de la criptografía: reemplazaba cada letra de un mensaje por la letra que está un número fijo de posiciones más adelante en el alfabeto. Con un desplazamiento de 3, la `a` se convierte en `d`, la `b` se convierte en `e` y la `c` se convierte en `f`.

El alfabeto se comporta como un círculo, así que las letras del final vuelven al principio: con un desplazamiento de 3, la `x` se convierte en `a`, la `y` se convierte en `b` y la `z` se convierte en `c`.

Todo lo que no sea una letra, como un espacio, una coma, un signo de exclamación o un dígito, atraviesa el cifrado sin modificarse.

# --instructions--

Escribe una función `caesarCipher` que reciba un mensaje `text` y un número entero `shift`, y devuelva el mensaje codificado.

Ejemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- El mensaje siempre está en minúsculas, así que nunca tienes que lidiar con letras mayúsculas.
- Los caracteres que no son letras conservan su lugar y su valor.
- El desplazamiento nunca es negativo. Un desplazamiento de `0` deja el mensaje sin cambios, y lo mismo ocurre con un desplazamiento de `26`.

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

Un desplazamiento de 3 convierte "hello" en "khoor"

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

El final del alfabeto da la vuelta, así que "xyz" se convierte en "abc"

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

Un desplazamiento de 0 deja el mensaje sin cambios

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

Un desplazamiento de 26 es una vuelta completa al alfabeto, así que el mensaje queda sin cambios

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

Los signos de puntuación y los espacios pasan sin cambios

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

Un mensaje vacío sigue estando vacío

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

Los espacios entre letras sueltas se conservan

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

Los dígitos no se desplazan, ni siquiera con un desplazamiento de 25

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

Un desplazamiento de 13 codifica una frase completa

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
