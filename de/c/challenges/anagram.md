---
language: c
exerciseType: 1
difficulty: 2
title: Anagramm
---

# --description--

Zwei Wörter sind Anagramme, wenn eines eine Umordnung des anderen ist: Sie verwenden exakt dieselben Buchstaben, jeden Buchstaben gleich oft, nur in einer anderen Reihenfolge. `listen` und `silent` sind Anagramme, und ebenso `stone` und `tones`.

Ein Wort ist nie ein Anagramm von sich selbst. Wenn die beiden Wörter exakt gleich sind, wurde nichts umgeordnet, daher ist die Antwort `false`. Beide Wörter sind in Kleinbuchstaben gegeben und enthalten nur die Buchstaben von `a` bis `z`.

# --instructions--

Schreiben Sie eine Funktion `isAnagram`, die zwei Wörter, `first` und `second`, entgegennimmt und `true` zurückgibt, wenn sie Anagramme voneinander sind, und andernfalls `false`.

Beispiele:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Zwei identische Wörter sind keine Anagramme.
- Wörter unterschiedlicher Länge sind nie Anagramme.
- Jeder Buchstabe muss in beiden Wörtern gleich oft vorkommen.

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
bool isAnagram(const char* first, const char* second) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Die Wörter "listen" und "silent" sind Anagramme

```c
    try_catch(isAnagram("listen", "silent") == true);
```

Die Wörter "stone" und "tones" sind Anagramme

```c
    try_catch(isAnagram("stone", "tones") == true);
```

Ein Wort ist kein Anagramm von sich selbst

```c
    try_catch(isAnagram("stone", "stone") == false);
```

Wörter unterschiedlicher Länge sind keine Anagramme

```c
    try_catch(isAnagram("abc", "abcd") == false);
```

Dieselben Buchstaben in unterschiedlicher Anzahl sind kein Anagramm

```c
    try_catch(isAnagram("aab", "abb") == false);
```

Die Wörter "anagram" und "nagaram" sind Anagramme

```c
    try_catch(isAnagram("anagram", "nagaram") == true);
```

Zwei Wörter derselben Länge mit unterschiedlichen Buchstaben sind keine Anagramme

```c
    try_catch(isAnagram("rat", "car") == false);
```

Zwei leere Wörter sind identisch, daher sind sie keine Anagramme

```c
    try_catch(isAnagram("", "") == false);
```

Zwei unterschiedliche einzelne Buchstaben sind keine Anagramme

```c
    try_catch(isAnagram("a", "b") == false);
```

Die Wörter "evil" und "vile" sind Anagramme

```c
    try_catch(isAnagram("evil", "vile") == true);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool isAnagram(const char* first, const char* second) {
    if (strcmp(first, second) == 0) {
        return false;
    }

    int counts[26] = {0};

    for (int i = 0; first[i] != '\0'; i++) {
        counts[first[i] - 'a']++;
    }

    for (int i = 0; second[i] != '\0'; i++) {
        counts[second[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (counts[i] != 0) {
            return false;
        }
    }

    return true;
}
```
