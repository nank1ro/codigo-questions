---
language: c
exerciseType: 1
difficulty: 1
title: बारिश की बूंदें
---

# --description--

आपका कार्य एक संख्या को एक स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूंदों की आवाज़ें हों।
गुणनखंड एक ऐसी संख्या है जो किसी अन्य संख्या को बिना शेषफल के समान रूप से विभाजित करती है।
यह जांचने का सबसे सरल तरीका कि कोई संख्या दूसरी की गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूंदों के नियम निम्नलिखित हैं:

- यदि 3 गुणनखंड है, तो परिणाम में 'Pling' जोड़ें।
- यदि 5 गुणनखंड है, तो परिणाम में 'Plang' जोड़ें।
- यदि 7 गुणनखंड है, तो परिणाम में 'Plong' जोड़ें।
- यदि 3, 5, या 7 में से कोई भी गुणनखंड नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 में 7 गुणनखंड है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 में 3 और 5 दोनों गुणनखंड हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 में 3, 5, या 7 कोई गुणनखंड नहीं है, इसलिए परिणाम `"34"` होगा।

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
char* convert(int number) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

1 के लिए ध्वनि "1" है

```c
    try_catch(strcmp(convert(1), "1") == 0);
```

3 के लिए ध्वनि "Pling" है

```c
    try_catch(strcmp(convert(3), "Pling") == 0);
```

5 के लिए ध्वनि "Plang" है

```c
    try_catch(strcmp(convert(5), "Plang") == 0);
```

7 के लिए ध्वनि "Plong" है

```c
    try_catch(strcmp(convert(7), "Plong") == 0);
```

6 के लिए ध्वनि "Pling" है

```c
    try_catch(strcmp(convert(6), "Pling") == 0);
```

8 के लिए ध्वनि "8" है

```c
    try_catch(strcmp(convert(8), "8") == 0);
```

9 के लिए ध्वनि "Pling" है

```c
    try_catch(strcmp(convert(9), "Pling") == 0);
```

10 के लिए ध्वनि "Plang" है

```c
    try_catch(strcmp(convert(10), "Plang") == 0);
```

14 के लिए ध्वनि "Plong" है

```c
    try_catch(strcmp(convert(14), "Plong") == 0);
```

15 के लिए ध्वनि "PlingPlang" है

```c
    try_catch(strcmp(convert(15), "PlingPlang") == 0);
```

21 के लिए ध्वनि "PlingPlong" है

```c
    try_catch(strcmp(convert(21), "PlingPlong") == 0);
```

25 के लिए ध्वनि "Plang" है

```c
    try_catch(strcmp(convert(25), "Plang") == 0);
```

27 के लिए ध्वनि "Pling" है

```c
    try_catch(strcmp(convert(27), "Pling") == 0);
```

35 के लिए ध्वनि "PlangPlong" है

```c
    try_catch(strcmp(convert(35), "PlangPlong") == 0);
```

49 के लिए ध्वनि "Plong" है

```c
    try_catch(strcmp(convert(49), "Plong") == 0);
```

52 के लिए ध्वनि "52" है

```c
    try_catch(strcmp(convert(52), "52") == 0);
```

105 के लिए ध्वनि "PlingPlangPlong" है

```c
    try_catch(strcmp(convert(105), "PlingPlangPlong") == 0);
```


3125 के लिए ध्वनि "Plang" है

```c
    try_catch(strcmp(convert(3125), "Plang") == 0);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
char* convert(int number) {
    char *result = malloc(sizeof(char) * 15);
    if (number % 3 == 0) {
        strcat(result, "Pling");
    }
    if (number % 5 == 0) {
        strcat(result, "Plang");
    }
    if (number % 7 == 0) {
        strcat(result, "Plong");
    }
    if (strlen(result) == 0) {
        sprintf(result, "%d", number);
    }
    return result;
}
```
