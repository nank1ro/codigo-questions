---
language: c
exerciseType: 1
difficulty: 3
title: कोष्ठकों का मिलान
---

# --description--

कोड, गणित या मार्कअप ले जाने वाला टेक्स्ट कोष्ठकों से भरा होता है, और हर खोलने वाले कोष्ठक को उसी किस्म का एक बंद करने वाला कोष्ठक चाहिए। एक स्ट्रिंग तब संतुलित होती है जब उसके कोष्ठक जोड़े बनाते हैं और प्याज की परतों की तरह एक-दूसरे के भीतर नेस्ट होते हैं: `{[()]}` संतुलित है, जबकि `{[(])}` संतुलित नहीं है, क्योंकि गोल जोड़ा उस वर्ग जोड़े से पहले बंद हो जाता है जिसके भीतर वह स्थित है।

यहाँ तीन जोड़े मायने रखते हैं: गोल `()`, वर्ग `[]` और कर्ली `{}`। स्ट्रिंग का बाकी हर कैरेक्टर नज़रअंदाज़ कर दिया जाता है। एक बंद करने वाले कोष्ठक को सबसे हाल में खोले गए उस कोष्ठक को बंद करना चाहिए जो अभी भी खुला है, और जब स्ट्रिंग समाप्त हो जाए तो कोई कोष्ठक खुला नहीं रहना चाहिए।

# --instructions--

एक फ़ंक्शन `is_balanced` लिखें जो एक स्ट्रिंग लेता है और तब `true` लौटाता है जब उसके सभी कोष्ठक मेल खाते हों और ठीक से नेस्ट होते हों, अन्यथा `false`।

उदाहरण:
```
is_balanced("") ➞ true
is_balanced("{[()]}") ➞ true
is_balanced("{what is (42)}[?]") ➞ true
is_balanced("{[(])}") ➞ false
is_balanced("(") ➞ false
is_balanced(")(") ➞ false
```

- खाली स्ट्रिंग संतुलित होती है।
- जो कैरेक्टर कोष्ठक नहीं हैं उन्हें नज़रअंदाज़ कर दिया जाता है।
- एक बंद करने वाला कोष्ठक सबसे हाल में खोले गए उस कोष्ठक से मेल खाना चाहिए जो अभी भी खुला है।
- जब स्ट्रिंग समाप्त हो तब कोई कोष्ठक खुला नहीं रहना चाहिए।

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

खाली स्ट्रिंग संतुलित होती है

```c
    try_catch(is_balanced("") == true);
```

गोल कोष्ठकों का एक जोड़ा संतुलित होता है

```c
    try_catch(is_balanced("()") == true);
```

एक-दूसरे के भीतर नेस्ट किए गए तीनों किस्म के जोड़े संतुलित होते हैं

```c
    try_catch(is_balanced("{[()]}") == true);
```

दूसरे टेक्स्ट के साथ मिले कोष्ठक भी संतुलित होते हैं

```c
    try_catch(is_balanced("{what is (42)}[?]") == true);
```

बगल में रखे गए जोड़े संतुलित होते हैं

```c
    try_catch(is_balanced("()[]{}") == true);
```

बिना किसी कोष्ठक वाली स्ट्रिंग संतुलित होती है

```c
    try_catch(is_balanced("no brackets in here at all") == true);
```

क्रॉस हो चुका जोड़ा संतुलित नहीं होता

```c
    try_catch(is_balanced("{[(])}") == false);
```

कभी बंद न होने वाला खोलने वाला कोष्ठक संतुलित नहीं होता

```c
    try_catch(is_balanced("(") == false);
```

किसी खोलने वाले कोष्ठक से पहले आया बंद करने वाला कोष्ठक संतुलित नहीं होता

```c
    try_catch(is_balanced(")(") == false);
```

स्ट्रिंग में गहराई में क्रॉस हो चुके जोड़े संतुलित नहीं होते

```c
    try_catch(is_balanced("(([]{[}]))") == false);
```

अंत में बचा हुआ बंद करने वाला कोष्ठक संतुलित नहीं होता

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
