---
language: c
exerciseType: 1
difficulty: 2
title: Suma de verificación de Luhn
---

# --description--

El algoritmo de Luhn es una suma de verificación simple que se usa para validar números de identificación, como los números de tarjetas de crédito.

Antes de comprobar un número, elimina todos los espacios de la cadena. La cadena solo es válida si lo que queda tiene más de un carácter y la cadena original no contiene nada más que dígitos y espacios.

Para realizar la comprobación, comienza desde el dígito de más a la derecha y avanza hacia la izquierda, duplicando cada segundo dígito. Cuando duplicar produce un número mayor que 9, réstale 9. Luego suma todos los dígitos: el número solo es válido si la suma es divisible por 10.

Por ejemplo, `"059"` da `0`, luego `5` duplicado es `10`, que se convierte en `1`, luego `9`. Su suma es `10`, que es divisible por 10, por lo que el número es válido.

# --instructions--

Escribe una función `is_valid` que tome un `const char *` y devuelva `true` cuando el número sea válido, `false` en caso contrario.

- `"4539 3195 0343 6467"` pasa la suma de verificación, por lo que el resultado es `true`.
- `"8273 1232 7352 0569"` falla la suma de verificación, por lo que el resultado es `false`.
- `"0"` tiene solo un carácter de longitud, por lo que el resultado es `false`.
- `"055-444-285"` contiene un carácter que no es un dígito ni un espacio, por lo que el resultado es `false`.

Ejemplo de llamada de función:
```c
printf("%d\n", is_valid("095 245 88"));
// imprime true
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

Un solo dígito no es válido.

```c
    try_catch(is_valid("0") == false);
```

Un solo dígito con un espacio inicial no es válido.

```c
    try_catch(is_valid(" 0") == false);
```

El número `"059"` es válido.

```c
    try_catch(is_valid("059") == true);
```

El número `"59"` es válido.

```c
    try_catch(is_valid("59") == true);
```

El número `"055 444 285"` es válido.

```c
    try_catch(is_valid("055 444 285") == true);
```

El número `"055 444 286"` no es válido.

```c
    try_catch(is_valid("055 444 286") == false);
```

El número `"8273 1232 7352 0569"` no es válido.

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

El número `"4539 3195 0343 6467"` es válido.

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

El número `"1 2345 6789 1234 5678 9012"` no es válido.

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

El número `"095 245 88"` es válido.

```c
    try_catch(is_valid("095 245 88") == true);
```

Una letra hace que el número sea inválido.

```c
    try_catch(is_valid("055a 444 285") == false);
```

Los guiones hacen que el número sea inválido.

```c
    try_catch(is_valid("055-444-285") == false);
```

Un carácter de puntuación hace que el número sea inválido.

```c
    try_catch(is_valid(":9") == false);
```

Los símbolos hacen que el número sea inválido.

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

Una cadena vacía no es válida.

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
