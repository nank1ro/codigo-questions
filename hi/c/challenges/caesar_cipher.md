---
language: c
exerciseType: 1
difficulty: 2
title: सीज़र सिफर
---

# --description--

जूलियस सीज़र ने क्रिप्टोग्राफी की सबसे पुरानी तरकीबों में से एक से अपनी निजी चिट्ठियों को सुरक्षित रखा था: वे किसी संदेश के हर अक्षर को वर्णमाला में एक निश्चित संख्या में आगे स्थित अक्षर से बदल देते थे। 3 के शिफ्ट पर `a`, `d` बन जाता है, `b`, `e` बन जाता है और `c`, `f` बन जाता है।

वर्णमाला एक वृत्त जैसा व्यवहार करती है, इसलिए अंत के अक्षर घूमकर वापस शुरुआत पर पहुँच जाते हैं: 3 के शिफ्ट पर `x`, `a` बन जाता है, `y`, `b` बन जाता है और `z`, `c` बन जाता है।

जो कुछ भी अक्षर नहीं है, जैसे रिक्त स्थान, अल्पविराम, विस्मयादिबोधक चिह्न या अंक, वह सिफर से बिना बदले गुज़र जाता है।

# --instructions--

एक फ़ंक्शन `caesarCipher` लिखें जो एक संदेश `text` और एक पूर्ण संख्या `shift` लेता है, और एन्कोड किया हुआ संदेश लौटाता है।

उदाहरण:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- संदेश हमेशा लोअरकेस में होता है, इसलिए आपको कभी भी अपरकेस अक्षरों से निपटना नहीं पड़ेगा।
- जो वर्ण अक्षर नहीं हैं, वे अपनी जगह और अपना मान बनाए रखते हैं।
- शिफ्ट कभी ऋणात्मक नहीं होता। `0` का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है, और `26` का शिफ्ट भी ऐसा ही करता है।

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

3 का शिफ्ट "hello" को "khoor" में बदल देता है

```c
    try_catch(strcmp(caesarCipher("hello", 3), "khoor") == 0);
```

वर्णमाला का अंत घूमकर शुरुआत पर वापस आ जाता है, इसलिए "xyz", "abc" बन जाता है

```c
    try_catch(strcmp(caesarCipher("xyz", 3), "abc") == 0);
```

0 का शिफ्ट संदेश को अपरिवर्तित छोड़ देता है

```c
    try_catch(strcmp(caesarCipher("abc", 0), "abc") == 0);
```

26 का शिफ्ट वर्णमाला का एक पूरा चक्र है, इसलिए संदेश अपरिवर्तित रहता है

```c
    try_catch(strcmp(caesarCipher("abc", 26), "abc") == 0);
```

विराम चिह्न और रिक्त स्थान बिना बदले गुज़र जाते हैं

```c
    try_catch(strcmp(caesarCipher("codigo, rocks!", 5), "htinlt, wthpx!") == 0);
```

खाली संदेश खाली ही रहता है

```c
    try_catch(strcmp(caesarCipher("", 4), "") == 0);
```

अक्षरों के बीच के रिक्त स्थान बने रहते हैं

```c
    try_catch(strcmp(caesarCipher("a b c", 1), "b c d") == 0);
```

25 के शिफ्ट पर भी अंक शिफ्ट नहीं होते

```c
    try_catch(strcmp(caesarCipher("abc 123!", 25), "zab 123!") == 0);
```

13 का शिफ्ट एक पूरे वाक्य को एन्कोड कर देता है

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
