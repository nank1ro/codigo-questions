C is a **statically typed** language: every variable is declared with a type that decides what it can store and how much memory it takes.
The three types you will use most are:
- `int` for whole numbers, like `30` or `-4`
- `double` for numbers with a decimal part, like `1.75`
- `char` for a single character, written in single quotes like `'A'`

Each type has its own `printf` **format specifier**: `%d` prints an `int`, `%f` prints a `double` (with six decimals by default) and `%c` prints a `char`:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// prints "30 1.750000 A"
```
Using the wrong specifier for a type prints garbage, so always match them.

---

C has two floating-point types: `float` (single precision, about 7 significant digits) and `double` (double precision, about 15 significant digits).
A decimal literal like `1.75` is a `double`; to write a `float` literal add the suffix `f`, as in `1.75f`.
Prefer `double` unless memory is tight: it is the default and it is more precise.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
A function that returns a decimal result should declare `double` as its return type, and `double` parameters accept both whole and decimal arguments:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` prints six decimals, which is rarely what you want. Put a precision between `%` and `f` to choose how many decimals to show: `%.2f` prints two decimals, `%.1f` prints one, and the value is **rounded**, not cut:
```c
double price = 9.987;
printf("%.2f\n", price); // prints "9.99"
printf("%.1f\n", price); // prints "10.0"
```
A `float` is printed with the same specifiers as a `double`: when passed to `printf` it is converted to `double` automatically.

---

The result of `/` depends on the types of its operands.
When **both** operands are integers the result is an integer and the decimal part is thrown away: `7 / 2` is `3`, not `3.5`.
When **at least one** operand is a floating-point value the division keeps the decimals: `7 / 2.0` is `3.5`.
```c
printf("%d\n", 7 / 2);     // prints "3"
printf("%f\n", 7 / 2.0);   // prints "3.500000"
```
Writing the literal as `2.0` instead of `2` is the simplest way to force a floating-point division.

---

C converts between numeric types **implicitly** when a value is assigned to a variable of a different type.
- an `int` stored in a `double` is widened without loss: `double d = 3;` makes `d` equal to `3.0`
- a `double` stored in an `int` is **truncated**: `int n = 3.99;` makes `n` equal to `3` (compilers usually warn about this)

The conversion happens only at the moment of the assignment. The expression on the right is computed first, with its own types:
```c
double d = 7 / 2;
```
Here `7 / 2` is an integer division that gives `3`, and only then `3` is converted to `3.0`.

---

When the implicit conversion is not what you want, or you want to make it visible, use an **explicit cast**: write the target type in parentheses before the value.
```c
double x = 3.99;
int n = (int) x;   // n is 3
```
Casting a floating-point value to `int` **truncates toward zero**: `(int) 3.99` is `3` and `(int) -2.5` is `-2`, no rounding takes place.
The cast applies only to the value right after it, so `(int) x * 2` casts `x` first and then multiplies.

---

A cast is the standard way to get a floating-point division from two `int` variables: cast **one operand** to `double` before dividing.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Casting the whole result instead, as in `(double) (total / count)`, is a common mistake: the integer division has already happened and the decimals are lost.

---

A `char` is really a small integer: it stores the **ASCII code** of the character.
`'A'` is `65`, `'a'` is `97` and `'0'` is `48`, and consecutive characters have consecutive codes.
That is why you can do arithmetic on characters:
- `'a' + 1` is `98`, the code of `'b'`
- `'7' - '0'` is `55 - 48`, that is the number `7`

The same value can be printed as a character with `%c` or as a number with `%d`:
```c
char c = 'A';
printf("%c %d\n", c, c); // prints "A 65"
```

---

Uppercase and lowercase letters are `32` positions apart in the ASCII table: `'A'` is `65` and `'a'` is `97`.
Subtracting `32` from a lowercase letter therefore gives its uppercase version, and the result can be stored back in a `char`:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` is not the only integer type. Modifiers change its size and range:
- `short` uses less memory and holds a smaller range (usually -32768 to 32767)
- `long` holds a larger range (on 64-bit systems about ±9 quintillion)
- `unsigned` removes the sign: `unsigned int` goes from `0` to about 4 billion, but can never be negative

A literal that must be `long` takes the suffix `L`, an `unsigned` one the suffix `U`, and each type has its own specifier:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // prints "8000000000 40"
```
`%ld` prints a `long`, `%u` an `unsigned int` and `%lu` an `unsigned long`. A plain `int` on most systems holds values up to about 2 billion, so `5000000000` does not fit in it.

---

The `sizeof` operator tells how many **bytes** a type or a variable occupies. Its result has the type `size_t`, which is printed with `%zu`:
```c
printf("%zu\n", sizeof(int));  // prints "4" on most systems
```
The standard only guarantees that `sizeof(char)` is `1` and that `short <= int <= long`, but on a typical 64-bit system the sizes are: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` is often used to check how much memory a variable takes without hard-coding the number.

---

Every integer type has a limited range, and the header `limits.h` gives those limits a name: `INT_MAX` and `INT_MIN` for `int`, `LONG_MAX` for `long`, `UINT_MAX` for `unsigned int`, and so on.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // prints "2147483647" on most systems
```
Going past `INT_MAX` with a signed type is **undefined behavior**: the program may wrap around, crash, or do anything else. Check before you compute:
```c
if (a <= INT_MAX - b) { /* a + b is safe */ }
```
Note that the check subtracts instead of adding, because `a + b` itself could already overflow.

---

Unlike signed types, **unsigned** arithmetic is well defined when it goes out of range: the value **wraps around** like an odometer.
Adding `1` to `UINT_MAX` gives `0`, and subtracting `1` from `0` gives `UINT_MAX` (`4294967295` when `unsigned int` has 32 bits):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // prints "0"
```
This is why a loop that counts an `unsigned` variable down "until it is negative" never stops: an unsigned value is never below `0`.

---

Since C99 the header `stdbool.h` provides the type `bool` with the constants `true` (`1`) and `false` (`0`).
A `bool` is an integer type with only two values, so converting any number to `bool` gives `true` for every non-zero value and `false` for `0`. This is different from converting to `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, because 0.5 is not zero
int n = 0.5;   // 0, because the decimals are truncated
```
Comparisons like `x != 0` already produce a `bool`-compatible result, and a function returning `bool` documents that it answers a yes/no question.

---

An arithmetic operation is performed in the type of its operands, **not** in the type of the variable that receives the result.
So `long big = n * n;` with an `int` `n` multiplies two `int` values, overflows if the product is too large, and only then stores the (already wrong) result in the `long`.
Cast one operand **before** the operation to compute in the wider type:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, computed as long
```
The same rule explains why `(double) total / count` works: the cast changes the type of the operand, and the division follows.

---

Putting it together: choose the type from the kind of value, match every `printf` specifier to its argument type, and cast when a computation must happen in a different type than its operands.
