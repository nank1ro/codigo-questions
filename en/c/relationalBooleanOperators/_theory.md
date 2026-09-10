**Relational operators** compare two values. The result is not a special type: it is an `int` that is `1` when the comparison holds and `0` when it does not. C has six of them:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Because the result is an `int`, it is printed with `%d` and can be stored in an `int` variable like any other number.

---

A function can return a comparison directly: the caller receives `1` or `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Choosing between `>` and `>=` (or `<` and `<=`) decides whether the boundary value counts: `n >= 100` is `1` for `100`, `n > 100` is `0`.

---

The most common C mistake is writing `=` where `==` was intended. A single `=` is an **assignment**, and in C an assignment is an expression whose value is the value that was assigned:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
The code with `=` still compiles, so a condition written as `if (x = 0)` silently sets `x` to `0` instead of testing it. Most compilers print a warning for this: read it.

---

**Logical operators** combine conditions. The **and** operator `&&` gives `1` only when both sides are true, the **or** operator `||` gives `1` when at least one side is true:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
In C **any non-zero value counts as true** and only `0` counts as false, so `5 && 1` is `1` and `0 || -3` is `1`. The result of `&&` and `||` is always exactly `1` or `0`.

---

A variable that holds `0` or a non-zero value can be used as a condition on its own: `holiday` alone means "holiday is non-zero", there is no need to write `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
The **not** operator `!` flips a condition: `!0` is `1` and `!` of any non-zero value is `0`.

---

Since `!` turns any non-zero value into `0` and `0` into `1`, applying it twice normalizes a value to exactly `0` or `1`: `!!42` is `1`, `!!0` is `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
This is handy when a function returns an arbitrary non-zero number and you want a clean `1`.

---

Since C99 the header `stdbool.h` provides the type `bool` and the constants `true` (which is `1`) and `false` (which is `0`):
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
A `bool` is still an integer underneath: it is printed with `%d`, and it works with `&&`, `||` and `!` exactly like a comparison result. It just makes the intent clearer than a plain `int`.

---

A function that answers a yes/no question should return `bool`. A `bool` parameter is already a condition, so use it directly as an operand of `&&` or `||`: write `age >= 18 && citizen`, not `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` is already included above your code in these exercises.

---

`&&` and `||` use **short-circuit evaluation**: they stop as soon as the result is known.
- with `&&`, if the left side is `0` the right side is never evaluated
- with `||`, if the left side is non-zero the right side is never evaluated

This lets a check on the left guard a dangerous operation on the right:
```c
int ok = count != 0 && total / count > 2;
```
When `count` is `0`, the division is never executed, so the program does not crash.

---

Short-circuit evaluation also skips function calls. In `1 || check()` the function `check` is never called, so any side effect it has, like updating a counter, does not happen.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Keep this in mind when a function on the right side of `&&` or `||` does something you rely on.

---

Operators have a **precedence** that decides what is computed first:
1. `!` is applied first
2. then the relational comparisons `<`, `>`, `<=`, `>=`
3. then the equality comparisons `==`, `!=`
4. then `&&`
5. then `||`

So `a > 0 && a < 10` needs no parentheses, and `a && b || c` means `(a && b) || c` because `&&` binds tighter than `||`. Use parentheses to force a different grouping or simply to make the intent readable.

---

A `char` is a small integer, so characters are compared with the same operators. Compare against a character literal in single quotes: `"a"` with double quotes is a string, which cannot be compared this way.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Consecutive characters like `'0'`, `'1'`, ... `'9'` or `'a'`, `'b'`, ... `'z'` have consecutive codes, so a range check on characters works exactly like one on numbers:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Do not chain comparisons like in math. `1 <= x <= 10` compiles, but it is evaluated as `(1 <= x) <= 10`: the first comparison gives `0` or `1`, and that is then compared with `10`, so the whole expression is always `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Always write both comparisons explicitly and join them with `&&`.

---

When a condition mixes `&&` and `||`, group each part with parentheses even when precedence would already do the right thing: the rule becomes readable at a glance.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
The remainder operator `%` pairs naturally with `==`: `n % 4 == 0` is `1` when `n` is divisible by `4`.
