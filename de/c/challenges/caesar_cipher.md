---
language: c
exerciseType: 1
difficulty: 2
title: Caesar-Verschlüsselung
---

# --description--

Julius Caesar schützte seine privaten Briefe mit einem der ältesten Tricks der Kryptografie: Er ersetzte jeden Buchstaben einer Nachricht durch den Buchstaben, der eine feste Anzahl von Stellen weiter hinten im Alphabet steht. Bei einer Verschiebung von 3 wird `a` zu `d`, `b` zu `e` und `c` zu `f`.

Das Alphabet verhält sich wie ein Kreis, daher laufen die Buchstaben am Ende wieder zum Anfang zurück: Bei einer Verschiebung von 3 wird `x` zu `a`, `y` zu `b` und `z` zu `c`.

Alles, was kein Buchstabe ist, etwa ein Leerzeichen, ein Komma, ein Ausrufezeichen oder eine Ziffer, durchläuft die Verschlüsselung unverändert.

# --instructions--

Schreiben Sie eine Funktion `caesarCipher`, die eine Nachricht `text` und eine ganze Zahl `shift` entgegennimmt und die verschlüsselte Nachricht zurückgibt.

Beispiele:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Die Nachricht besteht immer aus Kleinbuchstaben, Sie müssen sich also nie um Großbuchstaben kümmern.
- Zeichen, die keine Buchstaben sind, behalten ihren Platz und ihren Wert.
- Die Verschiebung ist nie negativ. Eine Verschiebung von `0` lässt die Nachricht unverändert, und eine Verschiebung von `26` ebenfalls.

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

Eine Verschiebung von 3 macht aus "hello" "khoor"

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

Die Buchstaben am Ende des Alphabets laufen zum Anfang zurück, daher wird "xyz" zu "abc"

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

Eine Verschiebung von 0 lässt die Nachricht unverändert

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

Eine Verschiebung von 26 ist eine volle Runde durch das Alphabet, daher bleibt die Nachricht unverändert

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

Satzzeichen und Leerzeichen werden unverändert durchgereicht

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

Eine leere Nachricht bleibt leer

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

Leerzeichen zwischen einzelnen Buchstaben bleiben erhalten

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

Ziffern werden nicht verschoben, auch nicht bei einer Verschiebung von 25

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

Eine Verschiebung von 13 verschlüsselt einen ganzen Satz

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
