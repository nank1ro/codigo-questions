---
language: c
exerciseType: 1
difficulty: 3
title: Passende Klammern
---

# --description--

Text, der Code, Formeln oder Markup enthält, ist voller Klammern, und jede öffnende Klammer braucht eine schließende derselben Art. Ein String ist ausgeglichen, wenn sich seine Klammern paarweise entsprechen und wie die Schichten einer Zwiebel verschachteln: `{[()]}` ist ausgeglichen, `{[(])}` dagegen nicht, weil das runde Paar vor dem eckigen Paar geschlossen wird, in dem es liegt.

Hier zählen drei Paare: runde `()`, eckige `[]` und geschweifte `{}`. Jedes andere Zeichen im String wird ignoriert. Eine schließende Klammer muss die zuletzt geöffnete Klammer schließen, die noch offen ist, und wenn der String endet, darf keine Klammer offen geblieben sein.

# --instructions--

Schreiben Sie eine Funktion `is_balanced`, die einen String entgegennimmt und `true` zurückgibt, wenn alle darin enthaltenen Klammern übereinstimmen und korrekt verschachtelt sind, und andernfalls `false`.

Beispiele:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- Ein leerer String ist ausgeglichen.
- Zeichen, die keine Klammern sind, werden ignoriert.
- Eine schließende Klammer muss zu der zuletzt geöffneten Klammer passen, die noch offen ist.
- Wenn der String endet, darf keine Klammer offen geblieben sein.

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
bool is_balanced(const char* text) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

Ein leerer String ist ausgeglichen

```c
    try_catch(is_balanced("") == true);
```

Ein einzelnes Paar runder Klammern ist ausgeglichen

```c
    try_catch(is_balanced("()") == true);
```

Die drei Arten von Paaren, ineinander verschachtelt, sind ausgeglichen

```c
    try_catch(is_balanced("{[()]}") == true);
```

Klammern, die mit anderem Text vermischt sind, sind weiterhin ausgeglichen

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

Nebeneinander stehende Paare sind ausgeglichen

```c
    try_catch(is_balanced("()[]{}") == true);
```

Ein String ohne jegliche Klammern ist ausgeglichen

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

Ein überkreuztes Paar ist nicht ausgeglichen

```c
    try_catch(is_balanced("{[(])}") == false);
```

Eine öffnende Klammer, die nie geschlossen wird, ist nicht ausgeglichen

```c
    try_catch(is_balanced("(") == false);
```

Eine schließende Klammer vor jeder öffnenden ist nicht ausgeglichen

```c
    try_catch(is_balanced(")(") == false);
```

Überkreuzte Paare tiefer im String sind nicht ausgeglichen

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

Eine am Ende übrig gebliebene schließende Klammer ist nicht ausgeglichen

```c
    try_catch(is_balanced("())") == false);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool is_balanced(const char* text) {
    size_t length = strlen(text);
    char stack[length + 1];
    size_t top = 0;

    for (size_t i = 0; i < length; i++) {
        char current = text[i];

        if (current == '(' || current == '[' || current == '{') {
            stack[top++] = current;
        } else if (current == ')' || current == ']' || current == '}') {
            if (top == 0) {
                return false;
            }

            char opening = stack[--top];
            if ((current == ')' && opening != '(') ||
                (current == ']' && opening != '[') ||
                (current == '}' && opening != '{')) {
                return false;
            }
        }
    }

    return top == 0;
}
```
