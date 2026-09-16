---
language: c
exerciseType: 1
difficulty: 1
title: हैमिंग दूरी
---

# --description--

DNA को न्यूक्लियोटाइडों के स्ट्रैंड के रूप में लिखा जाता है, जिनमें से प्रत्येक एक अक्षर होता है: `A`, `C`, `G` या `T`। जब समान लंबाई के दो स्ट्रैंड साथ-साथ पंक्तिबद्ध किए जाते हैं, तो कुछ स्थानों पर एक ही न्यूक्लियोटाइड होता है और कुछ स्थानों पर अलग-अलग।

जिन स्थानों पर दोनों स्ट्रैंड भिन्न होते हैं, उनकी संख्या हैमिंग दूरी कहलाती है, और जीववैज्ञानिक इसका उपयोग यह मापने के लिए करते हैं कि दो स्ट्रैंड कितनी दूर अलग हो गए हैं। `GAGCCTACTAACGGGAT` को `CATCGTAATGACGGCCT` के साथ पंक्तिबद्ध करने पर 7 स्थान भिन्न मिलते हैं, इसलिए उनकी हैमिंग दूरी 7 होती है।

# --instructions--

`hammingDistance` नाम का एक फ़ंक्शन लिखें जो समान लंबाई के दो DNA स्ट्रैंड लेता है और उन स्थानों की संख्या लौटाता है जहाँ वे भिन्न होते हैं।

उदाहरण:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- दोनों स्ट्रैंड हमेशा समान लंबाई के होते हैं, इसलिए आपको कभी अलग-अलग लंबाई वाले स्ट्रैंड संभालने की ज़रूरत नहीं है।
- दो खाली स्ट्रैंड कहीं भिन्न नहीं होते, इसलिए उनकी दूरी 0 होती है।

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
int hammingDistance(const char* left, const char* right) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

दो खाली स्ट्रैंड कहीं भिन्न नहीं होते

```c
    try_catch(hammingDistance("", "") == 0);
```

दो समान एकल-न्यूक्लियोटाइड स्ट्रैंड में कोई अंतर नहीं होता

```c
    try_catch(hammingDistance("A", "A") == 0);
```

दो भिन्न एकल-न्यूक्लियोटाइड स्ट्रैंड एक स्थान पर भिन्न होते हैं

```c
    try_catch(hammingDistance("A", "G") == 1);
```

दो छोटे स्ट्रैंड जो हर स्थान पर भिन्न होते हैं

```c
    try_catch(hammingDistance("AG", "CT") == 2);
```

दो छोटे स्ट्रैंड जो केवल पहले स्थान पर भिन्न होते हैं

```c
    try_catch(hammingDistance("AT", "CT") == 1);
```

स्ट्रैंडों के बीच में एक भिन्न न्यूक्लियोटाइड

```c
    try_catch(hammingDistance("GGACG", "GGTCG") == 1);
```

अलग-अलग स्थानों पर समान न्यूक्लियोटाइड भी अंतर में गिने जाते हैं

```c
    try_catch(hammingDistance("TAG", "GAT") == 2);
```

चार अंतरों वाले स्ट्रैंडों का एक लंबा जोड़ा

```c
    try_catch(hammingDistance("GATACA", "GCATAA") == 4);
```

एक स्ट्रैंड को एक स्थान खिसकाने पर लगभग हर स्थान भिन्न हो जाता है

```c
    try_catch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9);
```

विवरण वाले दोनों स्ट्रैंड की दूरी सात है

```c
    try_catch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
int hammingDistance(const char* left, const char* right) {
    int distance = 0;

    for (int i = 0; left[i] != '\0'; i++) {
        if (left[i] != right[i]) {
            distance++;
        }
    }

    return distance;
}
```
