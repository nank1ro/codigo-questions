---
language: c
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
A factor is a number that evenly divides into another number, leaving no remainder.
The simplest way to test if a number is a factor of another is to use the modulo operation.
The rules of raindrops are the followings:

- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

# --instructions--

Write a function that returns the correct string, examples:

- 28 has 7 as a factor, but not 3 or 5, so the result would be `"Plong"`.
- 30 has both 3 and 5 as factors, but not 7, so the result would be `"PlingPlang"`.
- 34 is not factored by 3, 5, or 7, so the result would be `"34"`.

# --before-seed--

```c
#include <string.h>
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
char* convert(int number) {
    
}
```

# --before-asserts--

```c
int main() {
    int _testsPassed = 0;
    int _testsFailed = 0;
```

# --asserts--

The sound for 1 is "1"

```c
    try ({
        if (strcmp(convert(1), "1") != 0) {
            throw(new_c_err_error_msg("--err-t1--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 3 is "Pling"

```c
    try ({
        if (strcmp(convert(3), "Pling") != 0) {
            throw(new_c_err_error_msg("--err-t2--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 5 is "Plang"

```c
    try ({
        if (strcmp(convert(5), "Plang") != 0) {
            throw(new_c_err_error_msg("--err-t3--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 7 is "Plong"

```c
    try ({
        if (strcmp(convert(7), "Plong") != 0) {
            throw(new_c_err_error_msg("--err-t4--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 6 is "Pling"

```c
    try ({
        if (strcmp(convert(6), "Pling") != 0) {
            throw(new_c_err_error_msg("--err-t5--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 8 is "8"

```c
    try ({
        if (strcmp(convert(8), "8") != 0) {
            throw(new_c_err_error_msg("--err-t6--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 9 is "Pling"

```c
    try ({
        if (strcmp(convert(9), "Pling") != 0) {
            throw(new_c_err_error_msg("--err-t7--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 10 is "Plang"

```c
    try ({
        if (strcmp(convert(10), "Plang") != 0) {
            throw(new_c_err_error_msg("--err-t8--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 14 is "Plong"

```c
    try ({
        if (strcmp(convert(14), "Plong") != 0) {
            throw(new_c_err_error_msg("--err-t9--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 15 is "PlingPlang"

```c
    try ({
        if (strcmp(convert(15), "PlingPlang") != 0) {
            throw(new_c_err_error_msg("--err-t10--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 21 is "PlingPlong"

```c
    try ({
        if (strcmp(convert(21), "PlingPlong") != 0) {
            throw(new_c_err_error_msg("--err-t11--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 25 is "Plang"

```c
    try ({
        if (strcmp(convert(25), "Plang") != 0) {
            throw(new_c_err_error_msg("--err-t12--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 27 is "Pling"

```c
    try ({
        if (strcmp(convert(27), "Pling") != 0) {
            throw(new_c_err_error_msg("--err-t13--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 35 is "PlangPlong"

```c
    try ({
        if (strcmp(convert(35), "PlangPlong") != 0) {
            throw(new_c_err_error_msg("--err-t14--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 49 is "Plong"

```c
    try ({
        if (strcmp(convert(49), "Plong") != 0) {
            throw(new_c_err_error_msg("--err-t15--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 52 is "52"

```c
    try ({
        if (strcmp(convert(52), "52") != 0) {
            throw(new_c_err_error_msg("--err-t16--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

The sound for 105 is "PlingPlangPlong"

```c
    try ({
        if (strcmp(convert(105), "PlingPlangPlong") != 0) {
            throw(new_c_err_error_msg("--err-t17--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```


The sound for 3125 is "Plang"

```c
    try ({
        if (strcmp(convert(3125), "Plang") != 0) {
            throw(new_c_err_error_msg("--err-t18--"));
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
