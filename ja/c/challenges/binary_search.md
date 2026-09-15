---
language: c
exerciseType: 1
difficulty: 2
title: 二分探索
---

# --description--

二分探索は、**ソート済み**のコレクションの中から値を見つける手法で、探索範囲を繰り返し半分にしていきます。中央の要素を調べ、それが目的の値でない場合は、ターゲットがより小さければ左半分へ、より大きければ右半分へと探索を続けます。

各ステップで残りの要素の半分が捨てられるため、二分探索は非常に大きなコレクションでもわずかな比較回数で答えにたどり着けます。一方、要素を1つずつ確認する方法では、要素の数と同じステップ数がかかってしまいます。

# --instructions--

昇順にソートされた整数の配列、その長さ、ターゲットの整数を受け取り、配列の中のターゲットのインデックス、ターゲットが存在しない場合は `-1` を返す関数 `binarySearch` を書いてください。

配列に重複は含まれないため、インデックスは常に一意です。配列が空の場合もあります。関数は線形走査ではなく、毎ステップで探索範囲を半分にしていく二分探索を使用しなければなりません。

関数呼び出しの例:
```c
int numbers[] = {1, 3, 5, 7};
printf("%d\n", binarySearch(numbers, 4, 5));
// 2 を出力する
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

空の配列での検索は-1を返す必要があります。

```c
    try_catch(binarySearch(NULL, 0, 7) == -1);
```

配列 `[5]` の中で 5 を検索した場合、0 を返す必要があります。

```c
    int single[] = {5};
    try_catch(binarySearch(single, 1, 5) == 0);
```

配列 `[5]` の中で 9 を検索した場合、-1 を返す必要があります。

```c
    try_catch(binarySearch(single, 1, 9) == -1);
```

12要素の配列の最初の要素-9はインデックス0で見つかる必要があります。

```c
    int numbers[] = {-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78};
    try_catch(binarySearch(numbers, 12, -9) == 0);
```

12要素の配列の最後の要素78はインデックス11で見つかる必要があります。

```c
    try_catch(binarySearch(numbers, 12, 78) == 11);
```

要素15はインデックス6で見つかる必要があります。

```c
    try_catch(binarySearch(numbers, 12, 15) == 6);
```

要素22はインデックス7で見つかる必要があります。

```c
    try_catch(binarySearch(numbers, 12, 22) == 7);
```

11と15の間にある値12は-1を返す必要があります。

```c
    try_catch(binarySearch(numbers, 12, 12) == -1);
```

すべての要素より小さいターゲットは-1を返す必要があります。

```c
    try_catch(binarySearch(numbers, 12, -100) == -1);
```

すべての要素より大きいターゲットは-1を返す必要があります。

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
