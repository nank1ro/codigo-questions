---
language: c
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Allerdings wird dies letztendlich zu Verwirrung führen, da Menschen normalerweise mit exakter Teilbarkeit durch 1 zählen und nicht mit Dezimalstellen. Um dies zu vermeiden, wurde beschlossen, alle 0,25 Tage alle vier Jahre zusammenzuzählen und diesem Jahr 366 Tage zu geben (einschließlich 29. Februar als Schalttag) und es als __Schaltjahr__ zu bezeichnen. Die anderen drei Jahre des Vier-Jahres-Zyklus hätten nur 365 Tage und __wären keine Schaltjahre__.

# --instructions--

In dieser Aufgabe bringen wir es auf die nächste Stufe, wo Sie bestimmen müssen, ob es sich um ein Schaltjahr handelt oder nicht, ohne die `time.h`-Importierung, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __ternäre Operation__ (`x ? a : b`) zu verwenden, und auch nicht die logischen Operatoren __AND__ (`&&`) und __OR__ (`||`), mit Ausnahme des __NOT__-Operators (`!`).

Geben Sie `true` zurück, wenn es sich um ein Schaltjahr handelt, `false` andernfalls.

Beispiel eines Funktionsaufrufs:
```c
printf("%d\n", leap_year(2000));
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
```

# --seed--

```c
bool leap_year(int year) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Die Verwendung von `time.h`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht zulässig.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```c
    try_catch(leap_year(2016) == true);
```

Das Jahr `1996` ist ein Schaltjahr.

```c
    try_catch(leap_year(1996) == true);
```

Das Jahr `1600` ist ein Schaltjahr.

```c
    try_catch(leap_year(1600) == true);
```

Das Jahr `2020` ist ein Schaltjahr.

```c
    try_catch(leap_year(2020) == true);
```

Das Jahr `2000` ist ein Schaltjahr.

```c
    try_catch(leap_year(2000) == true);
```

Das Jahr `2008` ist ein Schaltjahr.

```c
    try_catch(leap_year(2008) == true);
```

Das Jahr `1521` ist kein Schaltjahr.

```c
    try_catch(leap_year(1521) == false);
```

Das Jahr `1800` ist kein Schaltjahr.

```c
    try_catch(leap_year(1800) == false);
```

Das Jahr `2007` ist kein Schaltjahr.

```c
    try_catch(leap_year(2007) == false);
```

Das Jahr `2002` ist kein Schaltjahr.

```c
    try_catch(leap_year(2002) == false);
```

Das Jahr `1979` ist kein Schaltjahr.

```c
    try_catch(leap_year(1979) == false);
```

Das Jahr `2006` ist kein Schaltjahr.

```c
    try_catch(leap_year(2006) == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool leap_year(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```c
bool leap_year(int year) {
  while (year % 100 == 0) {
    year = year / 100;
  }
  return year % 4 == 0;
}
```
