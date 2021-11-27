---
language: c
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James would like to withdraw N dollars from an ATM.
The cash machine will only accept the transaction if N is a multiple of 5, and James' account has enough cash to perform the withdrawal transaction (including bank charges).
For each successful withdrawal the bank charges `0.50$`.
Calculate James' account balance after an attempted transaction.
The inputs are in the following order:
1. the amount of cash which James wishes to withdraw is in the following range: `0 < N <= 2000`.
2. James' initial balance is given with two digits of precision and is in the following range: `0 < B <= 2000`.

# --instructions--

Return the account balance after the attempted transaction, given as a number with two digits of precision.
If there is not enough money in the account to complete the transaction, return the current bank balance.

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
float account_balance() {
    
}
```

# --before-asserts--

```c
int main() {
    int _testsPassed = 0;
    int _testsFailed = 0;
```

# --asserts--

Perform a successful transaction

```c
    try ({
        if (account_balance(50, 120.00) != 69.50) {
            throw(new_c_err_error_msg("--err-t1--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

Insufficient funds

```c
    try ({
        if (account_balance(200, 120.00) != 120.00) {
            throw(new_c_err_error_msg("--err-t2--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

Refused transaction, invalid amount

```c
    try ({
        if (account_balance(22, 120.00) != 120.00) {
            throw(new_c_err_error_msg("--err-t3--"));
        }
        _testsPassed += 1;
    }, any, e, {
        _testsFailed += 1;
        printf("Test Case '%s' failed\n", e->msg);
    })
```

Withdraw all money successfully

```c
    try ({
        if (account_balance(95, 95.50) != 0.00) {
            throw(new_c_err_error_msg("--err-t4--"));
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
float account_balance(int withdraw, float balance) {
    if ((withdraw % 5 == 0) && (balance >= (withdraw + 0.50))) {
		return balance - withdraw - 0.50;
    }
	return balance;
}
```
