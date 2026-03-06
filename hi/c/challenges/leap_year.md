---
language: c
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, इससे भ्रम पैदा होगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं, दशमलव बिंदुओं से नहीं। इसलिए, इससे बचने के लिए, यह तय किया गया कि हर चार साल के चक्र में सभी 0.25 दिनों को जोड़ दिया जाए और उस वर्ष को 366 दिन दिए जाएं (29 फरवरी को एक अधिवर्ष दिवस के रूप में शामिल करते हुए) और इसे __लीप वर्ष__ कहा जाए। चार साल के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और वे __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहां आपको `time.h` इम्पोर्ट, `switch` स्टेटमेंट, __if ब्लॉक__, __if-else ब्लॉक__ या __टर्नरी ऑपरेशन__ (`x ? a : b`) और न ही लॉजिकल ऑपरेटर __AND__ (`&&`) और __OR__ (`||`) का उपयोग किए बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`!`) ऑपरेटर की छूट के साथ।

यदि यह लीप वर्ष है तो `true` लौटाएं, अन्यथा `false`।

फ़ंक्शन कॉल का उदाहरण:
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

`time.h`, `switch`, `if`, `else`, `&&`, `||` या `?` का उपयोग अनुमति नहीं है।

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||time\\.h",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```c
    try_catch(leap_year(2016) == true);
```

वर्ष `1996` एक लीप वर्ष है।

```c
    try_catch(leap_year(1996) == true);
```

वर्ष `1600` एक लीप वर्ष है।

```c
    try_catch(leap_year(1600) == true);
```

वर्ष `2020` एक लीप वर्ष है।

```c
    try_catch(leap_year(2020) == true);
```

वर्ष `2000` एक लीप वर्ष है।

```c
    try_catch(leap_year(2000) == true);
```

वर्ष `2008` एक लीप वर्ष है।

```c
    try_catch(leap_year(2008) == true);
```

वर्ष `1521` लीप वर्ष नहीं है।

```c
    try_catch(leap_year(1521) == false);
```

वर्ष `1800` लीप वर्ष नहीं है।

```c
    try_catch(leap_year(1800) == false);
```

वर्ष `2007` लीप वर्ष नहीं है।

```c
    try_catch(leap_year(2007) == false);
```

वर्ष `2002` लीप वर्ष नहीं है।

```c
    try_catch(leap_year(2002) == false);
```

वर्ष `1979` लीप वर्ष नहीं है।

```c
    try_catch(leap_year(1979) == false);
```

वर्ष `2006` लीप वर्ष नहीं है।

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
