---
language: c
exerciseType: 1
difficulty: 2
title: बाइनरी सर्च
---

# --description--

बाइनरी सर्च खोज की सीमा को बार-बार आधा करके किसी **क्रमबद्ध** कलेक्शन में एक मान ढूंढता है: बीच में स्थित तत्व को देखें, और यदि वही तत्व नहीं है जिसे आप चाहते हैं, तो जब लक्ष्य छोटा हो तो बाएं आधे हिस्से में और जब लक्ष्य बड़ा हो तो दाएं आधे हिस्से में खोज जारी रखें।

चूंकि हर चरण शेष तत्वों में से आधे तत्वों को छोड़ देता है, इसलिए बाइनरी सर्च बहुत बड़े कलेक्शन पर भी कुछ ही तुलनाओं में उत्तर तक पहुंच जाता है, जबकि तत्वों को एक-एक करके जांचने में उतने ही चरण लगते हैं जितने तत्व होते हैं।

# --instructions--

एक फ़ंक्शन `binarySearch` लिखें जो आरोही क्रम में क्रमबद्ध पूर्णांकों की एक सरणी, उसकी लंबाई और एक लक्ष्य पूर्णांक लेता है, और सरणी के भीतर लक्ष्य का इंडेक्स लौटाता है, या `-1` लौटाता है जब लक्ष्य मौजूद न हो।

सरणी में कभी डुप्लिकेट नहीं होते, इसलिए इंडेक्स हमेशा अद्वितीय होता है। सरणी खाली भी हो सकती है। आपके फ़ंक्शन को लीनियर स्कैन नहीं, बल्कि बाइनरी सर्च का उपयोग करना चाहिए, हर चरण में खोज की सीमा को आधा करते हुए।

फ़ंक्शन कॉल का उदाहरण:
```c
int numbers[] = {1, 3, 5, 7};
printf("%d\n", binarySearch(numbers, 4, 5));
// prints 2
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
```

# --seed--

```c
int binarySearch(int *arr, int length, int target) {
  
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

खाली सरणी में खोज करने पर -1 लौटाना चाहिए।

```c
    try_catch(binarySearch(NULL, 0, 7) == -1);
```

`[5]` में 5 खोजने पर 0 लौटाना चाहिए।

```c
    int single[] = {5};
    try_catch(binarySearch(single, 1, 5) == 0);
```

`[5]` में 9 खोजने पर -1 लौटाना चाहिए।

```c
    try_catch(binarySearch(single, 1, 9) == -1);
```

12 तत्वों वाली सरणी का पहला तत्व -9 इंडेक्स 0 पर मिलना चाहिए।

```c
    int numbers[] = {-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78};
    try_catch(binarySearch(numbers, 12, -9) == 0);
```

12 तत्वों वाली सरणी का अंतिम तत्व 78 इंडेक्स 11 पर मिलना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, 78) == 11);
```

तत्व 15 इंडेक्स 6 पर मिलना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, 15) == 6);
```

तत्व 22 इंडेक्स 7 पर मिलना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, 22) == 7);
```

मान 12, जो 11 और 15 के बीच स्थित है, -1 लौटाना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, 12) == -1);
```

हर तत्व से छोटा लक्ष्य -1 लौटाना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, -100) == -1);
```

हर तत्व से बड़ा लक्ष्य -1 लौटाना चाहिए।

```c
    try_catch(binarySearch(numbers, 12, 100) == -1);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
int binarySearch(int *arr, int length, int target) {
    int low = 0;
    int high = length - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] == target) {
            return mid;
        }
        if (arr[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}
```
