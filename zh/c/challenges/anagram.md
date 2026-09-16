---
language: c
exerciseType: 1
difficulty: 2
title: 变位词
---

# --description--

如果一个单词是另一个单词的重新排列，那么这两个单词就互为变位词：它们使用的字母完全相同，每个字母出现的次数也相同，只是顺序不同。`listen` 和 `silent` 是变位词，`stone` 和 `tones` 也是变位词。

一个单词永远不会是它自身的变位词。如果两个单词完全相同，就没有任何东西被重新排列，所以答案是 `false`。两个单词都以小写形式给出，并且只包含从 `a` 到 `z` 的字母。

# --instructions--

编写一个函数 `isAnagram`，它接收两个单词 `first` 和 `second`，当它们互为变位词时返回 `true`，否则返回 `false`。

示例：
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- 两个完全相同的单词不是变位词。
- 长度不同的单词永远不会是变位词。
- 每个字母在两个单词中出现的次数必须相同。

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
bool isAnagram(const char* first, const char* second) {
    
}
```

# --before-asserts--

```c
int main() {
```

# --asserts--

单词 "listen" 和 "silent" 互为变位词

```c
    try_catch(isAnagram("listen", "silent") == true);
```

单词 "stone" 和 "tones" 互为变位词

```c
    try_catch(isAnagram("stone", "tones") == true);
```

一个单词不是它自身的变位词

```c
    try_catch(isAnagram("stone", "stone") == false);
```

长度不同的单词不是变位词

```c
    try_catch(isAnagram("abc", "abcd") == false);
```

字母相同但出现次数不同则不是变位词

```c
    try_catch(isAnagram("aab", "abb") == false);
```

单词 "anagram" 和 "nagaram" 互为变位词

```c
    try_catch(isAnagram("anagram", "nagaram") == true);
```

长度相同但字母不同的两个单词不是变位词

```c
    try_catch(isAnagram("rat", "car") == false);
```

两个空单词是完全相同的，所以它们不是变位词

```c
    try_catch(isAnagram("", "") == false);
```

两个不同的单个字母不是变位词

```c
    try_catch(isAnagram("a", "b") == false);
```

单词 "evil" 和 "vile" 互为变位词

```c
    try_catch(isAnagram("evil", "vile") == true);
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _test_count, _test_failed_count);
    return 0;
}
```

# --solutions--

```c
bool isAnagram(const char* first, const char* second) {
    if (strcmp(first, second) == 0) {
        return false;
    }

    int counts[26] = {0};

    for (int i = 0; first[i] != '\0'; i++) {
        counts[first[i] - 'a']++;
    }

    for (int i = 0; second[i] != '\0'; i++) {
        counts[second[i] - 'a']--;
    }

    for (int i = 0; i < 26; i++) {
        if (counts[i] != 0) {
            return false;
        }
    }

    return true;
}
```
