---
language: c
exerciseType: 1
difficulty: 2
title: लूह्न चेकसम
---

# --description--

लूह्न एल्गोरिदम एक सरल चेकसम है जिसका उपयोग क्रेडिट कार्ड नंबरों जैसी पहचान संख्याओं को मान्य करने के लिए किया जाता है।

किसी संख्या की जांच करने से पहले, स्ट्रिंग से हर स्पेस हटा दें। स्ट्रिंग तभी मान्य है जब शेष बचा हिस्सा एक कैरेक्टर से लंबा हो और मूल स्ट्रिंग में अंकों और स्पेस के अलावा कुछ और न हो।

जांच करने के लिए, सबसे दाईं ओर के अंक से शुरू करें और बाईं ओर बढ़ते हुए हर दूसरे अंक को दोगुना करें। जब दोगुना करने पर 9 से बड़ी संख्या बनती है, तो उसमें से 9 घटा दें। फिर सभी अंकों का योग करें: संख्या तभी मान्य होती है जब योग 10 से विभाज्य हो।

उदाहरण के लिए, `"059"` देता है `0`, फिर `5` का दोगुना `10` होता है जो `1` बन जाता है, फिर `9`। उनका योग `10` है, जो 10 से विभाज्य है, इसलिए संख्या मान्य है।

# --instructions--

एक फ़ंक्शन `is_valid` लिखें जो एक `const char *` लेता है और संख्या मान्य होने पर `true` लौटाता है, अन्यथा `false`।

- `"4539 3195 0343 6467"` चेकसम पास करता है, इसलिए परिणाम `true` है।
- `"8273 1232 7352 0569"` चेकसम में विफल होता है, इसलिए परिणाम `false` है।
- `"0"` केवल एक कैरेक्टर लंबा है, इसलिए परिणाम `false` है।
- `"055-444-285"` में ऐसा कैरेक्टर है जो अंक या स्पेस नहीं है, इसलिए परिणाम `false` है।

फ़ंक्शन कॉल का उदाहरण:
```c
printf("%d\n", is_valid("095 245 88"));
// true प्रिंट करता है
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

एक अकेला अंक मान्य नहीं है।

```c
    try_catch(is_valid("0") == false);
```

शुरुआत में स्पेस के साथ एक अकेला अंक मान्य नहीं है।

```c
    try_catch(is_valid(" 0") == false);
```

संख्या `"059"` मान्य है।

```c
    try_catch(is_valid("059") == true);
```

संख्या `"59"` मान्य है।

```c
    try_catch(is_valid("59") == true);
```

संख्या `"055 444 285"` मान्य है।

```c
    try_catch(is_valid("055 444 285") == true);
```

संख्या `"055 444 286"` मान्य नहीं है।

```c
    try_catch(is_valid("055 444 286") == false);
```

संख्या `"8273 1232 7352 0569"` मान्य नहीं है।

```c
    try_catch(is_valid("8273 1232 7352 0569") == false);
```

संख्या `"4539 3195 0343 6467"` मान्य है।

```c
    try_catch(is_valid("4539 3195 0343 6467") == true);
```

संख्या `"1 2345 6789 1234 5678 9012"` मान्य नहीं है।

```c
    try_catch(is_valid("1 2345 6789 1234 5678 9012") == false);
```

संख्या `"095 245 88"` मान्य है।

```c
    try_catch(is_valid("095 245 88") == true);
```

एक अक्षर संख्या को अमान्य बना देता है।

```c
    try_catch(is_valid("055a 444 285") == false);
```

डैश संख्या को अमान्य बना देते हैं।

```c
    try_catch(is_valid("055-444-285") == false);
```

एक विराम चिह्न कैरेक्टर संख्या को अमान्य बना देता है।

```c
    try_catch(is_valid(":9") == false);
```

प्रतीक संख्या को अमान्य बना देते हैं।

```c
    try_catch(is_valid("055# 444$ 285") == false);
```

खाली स्ट्रिंग मान्य नहीं है।

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
