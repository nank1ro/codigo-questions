---
language: c
exerciseType: 1
difficulty: 2
title: Codifica run-length
---

# --description--

La codifica run-length è uno dei trucchi di compressione più antichi che esistano: invece di scrivere più e più volte lo stesso carattere, scrivi quante volte si ripete e poi il carattere stesso.

Un fax che scansiona una pagina quasi tutta bianca incontra lunghe distese di pixel identici, così una riga di dodici `W` viaggia lungo la linea come la ben più corta `12W`. Quando un carattere compare una sola volta, contarlo non porta nessun vantaggio, quindi viene copiato da solo.

# --instructions--

Scrivi una funzione `encode_run` che riceve una stringa `text` e restituisce la sua forma codificata run-length.

Ogni sequenza dello stesso carattere ripetuto due o più volte diventa la lunghezza della sequenza scritta in decimale, seguita da quel carattere. Una sequenza di lunghezza uno viene copiata come singolo carattere, senza nessun numero davanti.

Esempi:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Il testo contiene solo lettere maiuscole dalla `A` alla `Z` e spazi.
- Una sequenza più lunga di nove caratteri usa il suo conteggio decimale completo, quindi dodici `W` diventano `12W` e mai `9W3W`.
- Gli spazi sono caratteri normali: vengono contati e codificati esattamente come le lettere.
- La stringa vuota si codifica nella stringa vuota.

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
char* encode_run(const char* text) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

La stringa vuota si codifica nella stringa vuota

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

Un singolo carattere viene copiato così com'è

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

Una stringa senza ripetizioni attraversa il processo invariata

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

Una sequenza di due diventa il conteggio seguito dal carattere

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

L'esempio misto "AABCCCDEEEE" diventa "2AB3CD4E"

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

Una sequenza di dodici usa il suo conteggio decimale completo, quindi il risultato inizia con "12W"

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

Le sequenze di spazi vengono codificate esattamente come le sequenze di lettere

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

Una sequenza di dieci viene scritta come "10A", mai come due sequenze più corte

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

I caratteri singoli che si alternano vengono tutti copiati così come sono

```c
    try_catch(strcmp(encode_run("ABABAB"), "ABABAB") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* encode_run(const char* text) {
    size_t length = strlen(text);
    char* result = malloc(length * 2 + 2);
    size_t out = 0;
    size_t i = 0;

    while (i < length) {
        size_t run = 1;
        while (i + run < length && text[i + run] == text[i]) {
            run++;
        }
        if (run > 1) {
            out += sprintf(result + out, "%d", (int)run);
        }
        result[out++] = text[i];
        i += run;
    }

    result[out] = '\0';
    return result;
}
```
