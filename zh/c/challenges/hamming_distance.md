---
language: c
exerciseType: 1
difficulty: 1
title: 汉明距离
---

# --description--

DNA 写成一条由核苷酸组成的链，每个核苷酸是单个字母：`A`、`C`、`G` 或 `T`。当两条等长的链并排排列时，有些位置上的核苷酸相同，有些位置上的核苷酸则不同。

两条链上不同位置的数目称为汉明距离，生物学家用它来衡量两条链已经分化得有多远。将 `GAGCCTACTAACGGGAT` 与 `CATCGTAATGACGGCCT` 并排对齐后有 7 个位置不同，因此它们的汉明距离是 7。

# --instructions--

编写一个函数 `hammingDistance`，它接收两条等长的 DNA 链，并返回它们不同位置的数目。

示例：
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 两条链的长度总是相同的，所以你无需处理长度不同的链。
- 两条空链没有任何不同，所以它们的距离是 0。

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

两条空链没有任何不同

```c
    try_catch(hammingDistance("", "") == 0);
```

两条相同的单核苷酸链没有差异

```c
    try_catch(hammingDistance("A", "A") == 0);
```

两条不同的单核苷酸链在一个位置上不同

```c
    try_catch(hammingDistance("A", "G") == 1);
```

两条在每个位置都不同的短链

```c
    try_catch(hammingDistance("AG", "CT") == 2);
```

两条只在第一个位置不同的短链

```c
    try_catch(hammingDistance("AT", "CT") == 1);
```

链的中间有一个不同的核苷酸

```c
    try_catch(hammingDistance("GGACG", "GGTCG") == 1);
```

相同核苷酸出现在不同位置也算作差异

```c
    try_catch(hammingDistance("TAG", "GAT") == 2);
```

一对有四个差异的较长的链

```c
    try_catch(hammingDistance("GATACA", "GCATAA") == 4);
```

将一条链移动一个位置会使几乎所有位置都不同

```c
    try_catch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9);
```

描述中的两条链的距离为 7

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
