---
language: c
exerciseType: 1
difficulty: 1
title: Addition
---

# --description--

Given two integers `num1` and `num2`, write a program to add these two numbers

# --instructions--

Write a function that returns the sum of two numbers

# --before-seed--

```c
// DO NOT EDIT FROM HERE
// ----------------------
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    unsigned int  id;
    char         *name;
    char         *msg;
} error;

#define _printerr(e, s, ...) fprintf(stderr, "\033[1m\033[37m" "%s:%d: " "\033[1m\033[31m" e ":" "\033[1m\033[37m" " ‘%s_error’ " "\033[0m" s "\n", __FILE__, __LINE__, (*__err)->name, ##__VA_ARGS__)
#define printerr(s, ...) _printerr("error", s, ##__VA_ARGS__)
#define printuncaughterr() _printerr("uncaught error", "%s", (*__err)->msg)

#define _errordef(n, _id) \
error* new_##n##_error_msg(char* msg) { \
    error* self = malloc(sizeof(error)); \
    self->id = _id; \
    self->name = #n; \
    self->msg = msg; \
    return self; \
} \
error* new_##n##_error() { return new_##n##_error_msg(""); }

#define errordef(n) _errordef(n, __COUNTER__ +1)

#define try(try_block, err, err_name, catch_block) { \
    error * err_name = NULL; \
    error ** __err = & err_name; \
    void __try_fn() try_block \
    __try_fn(); \
    void __catch_fn() { \
        if (err_name == NULL) return; \
        unsigned int __##err_name##_id = new_##err##_error()->id; \
        if (__##err_name##_id != 0 && __##err_name##_id != err_name->id) \
            printuncaughterr(); \
        else if (__##err_name##_id != 0 || __##err_name##_id != err_name->id) \
            catch_block \
    } \
    __catch_fn(); \
}

#define throw(e) { *__err = e; return; }

_errordef(any, 0)
errordef(c_err)
// ----------------------
// DO NOT EDIT UNTIL HERE
```

# --seed--

```c
int addition() {

}
```

# --before-asserts--

```c
int main() {
    int _testsPassed = 0;
    int _testsFailed = 0;
    
```

# --asserts--

The sum of 1 and 3 must equal 4

```c
    try ({
        if (addition(1, 3) != 4) {
            throw(new_c_err_error_msg("--err-t1--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sum of 200 and 210 must equal 410

```c
    try ({
        if (addition(200, 210) != 410) {
            throw(new_c_err_error_msg("--err-t2--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sum of 15 and 35 must equal 50

```c
    try ({
        if (addition(15, 35) != 50) {
            throw(new_c_err_error_msg("--err-t3--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

# --after-asserts--

```c
    printf("Executed %d tests, with %d failures", _testsPassed + _testsFailed, _testsFailed);
    return 0;
}
```

# --solutions--

```c
int addition(int num1, int num2) {
    return num1 + num2;
}
```
