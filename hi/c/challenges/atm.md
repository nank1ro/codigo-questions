---
language: c
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

जेम्स एक ATM से N डॉलर निकालना चाहता है।
कैश मशीन केवल तभी लेनदेन स्वीकार करेगी जब N 5 का गुणज हो, और जेम्स के खाते में निकासी लेनदेन करने के लिए पर्याप्त नकदी हो (बैंक शुल्क सहित)।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद जेम्स के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. जेम्स जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. जेम्स की प्रारंभिक शेष राशि दो अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएं, दो अंकों की सटीकता वाली संख्या के रूप में।
यदि लेनदेन पूरा करने के लिए खाते में पर्याप्त पैसा नहीं है, तो वर्तमान बैंक शेष राशि लौटाएं।

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
float account_balance() {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

एक सफल लेनदेन करें

```c
    try_catch(account_balance(50, 120.00) == 69.50);
```

अपर्याप्त धनराशि

```c
    try_catch(account_balance(200, 120.00) == 120.00);
```

अस्वीकृत लेनदेन, अमान्य राशि

```c
    try_catch(account_balance(22, 120.00) == 120.00);
```

सभी पैसे सफलतापूर्वक निकालें

```c
    try_catch(account_balance(95, 95.50) == 0.00);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
float account_balance(int withdraw, float balance) {
    if ((withdraw % 5 == 0) && (balance >= (withdraw + 0.50))) {
        return balance - withdraw - 0.50;
    }
    return balance;
}
```
