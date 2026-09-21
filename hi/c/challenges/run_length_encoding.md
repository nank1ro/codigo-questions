---
language: c
exerciseType: 1
difficulty: 2
title: रन लंबाई एन्कोडिंग
---

# --description--

रन लंबाई एन्कोडिंग संपीड़न की सबसे पुरानी तरकीबों में से एक है: एक ही अक्षर को बार-बार लिखने के बजाय, आप लिख देते हैं कि वह अक्षर कितनी बार दोहराया गया है और फिर उस अक्षर को स्वयं लिख देते हैं।

ज़्यादातर खाली पन्ने को स्कैन करती एक फ़ैक्स मशीन को एक जैसे पिक्सेल के लंबे खिंचाव मिलते हैं, इसलिए बारह `W` की एक पंक्ति लाइन के नीचे बहुत छोटे `12W` के रूप में यात्रा करती है। जब कोई अक्षर केवल एक बार आता है तो उसे गिनने से कुछ हासिल नहीं होता, इसलिए उसे जैसा है वैसा ही अकेले कॉपी कर दिया जाता है।

# --instructions--

एक फ़ंक्शन `encode_run` लिखें जो एक स्ट्रिंग `text` लेता है और उसका रन लंबाई एन्कोडेड रूप लौटाता है।

एक ही अक्षर के दो या दो से अधिक बार दोहराए जाने वाला हर रन उस रन की दशमलव में लिखी गई लंबाई और उसके बाद वह अक्षर बन जाता है। एक की लंबाई वाला रन केवल उस एक अक्षर के रूप में कॉपी होता है, उसके आगे कोई संख्या नहीं लिखी जाती।

उदाहरण:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- टेक्स्ट में केवल `A` से `Z` तक के अपरकेस अक्षर और रिक्त स्थान होते हैं।
- नौ से लंबा कोई रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए बारह `W`, `12W` बन जाते हैं, कभी भी `9W3W` नहीं।
- रिक्त स्थान साधारण अक्षर हैं: उन्हें भी अक्षरों की तरह ही गिना और एन्कोड किया जाता है।
- खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है।

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

खाली स्ट्रिंग का एन्कोडिंग खाली स्ट्रिंग ही होता है

```c
    try_catch(strcmp(encode_run(""), "") == 0);
```

एक अकेला अक्षर जैसा है वैसा ही कॉपी हो जाता है

```c
    try_catch(strcmp(encode_run("A"), "A") == 0);
```

बिना दोहराव वाली स्ट्रिंग बिना बदले आगे बढ़ जाती है

```c
    try_catch(strcmp(encode_run("ABCDE"), "ABCDE") == 0);
```

दो की लंबाई वाला रन गिनती और उसके बाद अक्षर बन जाता है

```c
    try_catch(strcmp(encode_run("AA"), "2A") == 0);
```

मिश्रित उदाहरण "AABCCCDEEEE", "2AB3CD4E" बन जाता है

```c
    try_catch(strcmp(encode_run("AABCCCDEEEE"), "2AB3CD4E") == 0);
```

बारह की लंबाई वाला रन अपनी पूरी दशमलव गिनती इस्तेमाल करता है, इसलिए परिणाम "12W" से शुरू होता है

```c
    try_catch(strcmp(encode_run("WWWWWWWWWWWWBWW"), "12WB2W") == 0);
```

रिक्त स्थानों के रन भी अक्षरों के रनों की तरह ही एन्कोड होते हैं

```c
    try_catch(strcmp(encode_run("  HI  "), "2 HI2 ") == 0);
```

दस की लंबाई वाला रन "10A" लिखा जाता है, कभी भी दो छोटे रनों के रूप में नहीं

```c
    try_catch(strcmp(encode_run("AAAAAAAAAA"), "10A") == 0);
```

बारी-बारी से आने वाले अकेले अक्षर सभी जैसे हैं वैसे ही कॉपी होते हैं

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
