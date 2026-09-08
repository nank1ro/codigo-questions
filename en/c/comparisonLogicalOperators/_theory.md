**Comparison operators** compare two values and produce an answer: `1` when the comparison holds and `0` when it does not.
The **equal** operator `==` checks whether two values are the same, the **not equal** operator `!=` checks whether they differ:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// prints "0"
printf("%d\n", a != b);
// prints "1"
```
Be careful: `==` (two signs) compares, while a single `=` assigns a value.

---

The other comparison operators check the order of two values:
- `<` less than, `>` greater than
- `<=` less than or equal to, `>=` greater than or equal to
```c
printf("%d\n", 3 < 5);  // prints "1"
printf("%d\n", 5 >= 6); // prints "0"
```
A function can return a comparison directly, because the result is a plain `int`:
```c
int is_big(int n) {
    return n > 100;
}
```

---

In C the result of a comparison is not a special type: it is an `int` whose value is exactly `1` (true) or `0` (false).
That means you can store it in an `int` variable like any other number:
```c
int n = 42;
int big = n > 100; // big is 0
```
There is no `true`/`false` word in the output: `printf("%d", 2 == 2)` prints `1`.

---

**Logical operators** combine comparisons. The **and** operator `&&` gives `1` only when both sides are true:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // prints "1"
```
Do not chain comparisons like in math: `1 <= x <= 10` is evaluated as `(1 <= x) <= 10`, which compares a `0` or `1` with `10` and is always true.
Always write the two comparisons explicitly and join them with `&&`.

---

The **or** operator `||` gives `1` when at least one side is true, and `0` only when both sides are false:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // prints "1"
```
Each side must be a complete comparison: `day == 6 || 7` does not mean "6 or 7" (you will see why later).

---

The **not** operator `!` flips a result: `!1` is `0` and `!0` is `1`.
It is placed in front of the expression, so use parentheses to negate a whole comparison:
```c
int n = 5;
printf("%d\n", !(n > 3)); // prints "0"
```
Without the parentheses, `!n > 3` would first compute `!n` and then compare it with `3`.

---

Logical operators do not only work on `0` and `1`: in C **any non-zero value counts as true** and only `0` counts as false.
So `5 && 1` is `1`, `0 || -3` is `1`, and `!` turns any non-zero value into `0`:
```c
printf("%d\n", !7); // prints "0"
printf("%d\n", !0); // prints "1"
```
This is why `day == 6 || 7` is always true: `7` on its own is a true value.

---

`&&` and `||` use **short-circuit evaluation**: they stop as soon as the result is known.
- with `&&`, if the left side is `0` the right side is never evaluated
- with `||`, if the left side is true the right side is never evaluated

This lets you guard a dangerous operation with a check placed on its left:
```c
int safe = divisor != 0 && value / divisor > 2;
```
When `divisor` is `0`, the division is never executed.

---

Short-circuit evaluation also skips function calls: in `0 && check()` the function `check` is never called, so any side effect it has (like updating a counter) does not happen.

---

Operators have a **precedence** that decides what is computed first:
1. `!` is applied first
2. then the relational comparisons `<`, `>`, `<=`, `>=`
3. then the equality comparisons `==`, `!=`
4. then `&&`
5. then `||`

So `a > 0 && a < 10` needs no parentheses: both comparisons are computed before `&&`.
And `x == 1 || y == 2 && z == 3` means `x == 1 || (y == 2 && z == 3)`, because `&&` binds tighter than `||`.

---

A `char` is a small integer, so characters can be compared with the same operators.
Compare against a character literal in single quotes:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Double quotes would create a string, which cannot be compared this way.

---

Because characters are numbers, `<` and `>` compare their codes, and consecutive characters like `'a'`, `'b'`, `'c'` or `'0'`, `'1'`, `'2'` have consecutive codes.
A range check on characters therefore works exactly like one on numbers:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

A classic C mistake is writing `=` where `==` was intended. The code still compiles, because an assignment is an expression whose value is the value assigned:
```c
int x = 5;
if (x = 0) { ... } // assigns 0 to x, the condition is 0 (false)
if (x = 3) { ... } // assigns 3 to x, the condition is 3 (true)
```
Most compilers warn about this, so read the warnings when a condition behaves strangely.

---

The condition of an `if` is just an expression that is treated as true when non-zero, so comparisons and logical operators fit naturally:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
You can also store the result first and test the variable: `int ok = n > 0; if (ok) { ... }`.

---

A `while` loop keeps running as long as its condition is non-zero, so a comparison decides when it stops:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// prints 0, 1, 2
```
Choosing between `<` and `<=` changes whether the last value is included.

---

Since C99, the header `stdbool.h` provides the type `bool` and the constants `true` (`1`) and `false` (`0`):
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
A `bool` is still an integer underneath: printing it with `%d` shows `1` or `0`, and it works with `&&`, `||` and `!` like any comparison result.
Using `bool` makes the intent of a function clearer than returning a plain `int`.

---

A `bool` parameter can be used directly as an operand of `&&` or `||`, without comparing it to `true`: write `age >= 18 && citizen`, not `citizen == true`.

---

When a condition mixes `&&` and `||`, add parentheses around each group even when precedence would already do the right thing: it makes the rule readable at a glance.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
