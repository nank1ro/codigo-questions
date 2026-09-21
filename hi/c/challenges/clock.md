---
language: c
exerciseType: 1
difficulty: 2
title: घड़ी
---

# --description--

24 घंटे की घड़ी दिन के समय को `HH:MM` के रूप में दिखाती है, जो आधी रात के ठीक बाद `00:00` से शुरू होती है और अगली आधी रात से एक मिनट पहले `23:59` पर समाप्त होती है। दोनों भाग हमेशा दो अंकों में लिखे जाते हैं, इसलिए सुबह ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है।

एक पूरे दिन में 1440 मिनट होते हैं। जैसे ही घड़ी `23:59` से आगे निकलती है, वह `00:00` पर लौट आती है और दिन को फिर से शुरू करती है, और इसे `00:00` से पीछे की ओर घुमाने पर `23:59` पर पहुँचती है।

# --instructions--

एक फ़ंक्शन `clock_time` लिखें जो दो पूर्ण संख्याएं, `hours` और `minutes`, लेता है और 24 घंटे की घड़ी का समय `"HH:MM"` स्ट्रिंग के रूप में लौटाता है, जिसमें दोनों भाग दो अंकों तक पैड किए गए होते हैं।

उदाहरण:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- कोई भी संख्या ऋणात्मक हो सकती है, या किसी असली घड़ी की अनुमति से बड़ी हो सकती है।
- मिनटों की कुल संख्या `hours * 60 + minutes` के रूप में निकालें, फिर उस कुल को `0` से `1439` की सीमा में लपेटें ताकि घड़ी दोनों दिशाओं में घूम जाए।
- `clock_time(24, 0)` ठीक एक पूरा दिन है, इसलिए उसे `"00:00"` पढ़ा जाता है।

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
char* clock_time(int hours, int minutes) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

सुबह के आठ बजे को `08:00` पढ़ा जाता है

```c
    try_catch(strcmp(clock_time(8, 0), "08:00") == 0);
```

एकल अंक दो अंकों तक पैड किए जाते हैं, इसलिए ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है

```c
    try_catch(strcmp(clock_time(11, 9), "11:09") == 0);
```

पूरे एक दिन के घंटे `00:00` पर घूम जाते हैं

```c
    try_catch(strcmp(clock_time(24, 0), "00:00") == 0);
```

60 से अधिक मिनट घंटों में जुड़ जाते हैं

```c
    try_catch(strcmp(clock_time(25, 160), "03:40") == 0);
```

ऋणात्मक घंटा घड़ी को आधी रात से पीछे की ओर घुमा देता है

```c
    try_catch(strcmp(clock_time(-1, 15), "23:15") == 0);
```

ऋणात्मक मिनट गिनती भी घड़ी को पीछे की ओर घुमा देती है

```c
    try_catch(strcmp(clock_time(0, -90), "22:30") == 0);
```

एक पूरे दिन से अधिक पीछे जाने पर भी घड़ी घूमती रहती है

```c
    try_catch(strcmp(clock_time(-25, 0), "23:00") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* clock_time(int hours, int minutes) {
    int total = (hours * 60 + minutes) % 1440;
    if (total < 0) {
        total += 1440;
    }

    char* result = malloc(6);
    sprintf(result, "%02d:%02d", total / 60, total % 60);
    return result;
}
```
