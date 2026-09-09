Every variable lives somewhere in memory, and that place has a number called its **address**. The `&` operator, read "address of", gives the address of a variable:
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
The `%p` specifier prints an address; the exact number changes from one run to the next, so programs never rely on it.
An address is stored in a **pointer** variable. A pointer is declared with the type it points to followed by `*`:
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
`p` is now said to **point to** `x`. Two pointers are equal when they hold the same address, so `p == &x` is true.

---

A pointer on its own is just an address. To read the value stored at that address you **dereference** the pointer with the `*` operator:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` means "the value that `p` points to", and it is an `int` like `x` itself. The same symbol `*` has two roles: in a declaration `int *p` it says "this is a pointer", in an expression `*p` it follows the pointer to the value.

---

A dereferenced pointer can also be **assigned**. Writing to `*p` stores the new value at the address held by `p`, so the variable it points to changes:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` and `*p` are two names for the same memory. Assigning to `p` without the `*` would instead change **which address** the pointer holds, not the value stored there.

---

A pointer that does not point to anything yet should hold `NULL`, a special constant defined in `stdio.h` and `stddef.h` that means "no address":
```c
int *p = NULL;
```
Dereferencing a `NULL` pointer is a runtime error that crashes the program, so a pointer that may be `NULL` is checked before use:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Since `NULL` is zero, `if (p)` is a common shorthand for `if (p != NULL)`. A pointer declared without an initialiser holds garbage, not `NULL`, so always initialise pointers.

---

A pointer can point to any type: `double *`, `char *`, `bool *` and so on. The type in the declaration tells the compiler how many bytes to read when the pointer is dereferenced and what they mean:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
A pointer must match the type of the variable it points to; `int *p = &price;` is rejected by the compiler. `NULL` is the only value that fits a pointer of any type.

---

A pointer to `char` works like any other pointer: it holds the address of a single character, and `*p` reads or writes that character:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
Reading through a pointer and writing through it can be mixed freely: `*p = *p + 1` turns `'A'` into `'B'`.

---

A pointer stores an address, and every address has the same size on a given machine, no matter what type is stored there. `sizeof` a pointer is therefore the same for `char *`, `int *` and `double *`: `8` bytes on a 64-bit system, `4` on a 32-bit one:
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
Do not confuse the size of the pointer with the size of what it points to: `sizeof(p)` is the size of the address, `sizeof(*p)` is the size of the value.

---

An array name used in an expression gives the address of its **first element**, so it can be assigned to a pointer directly:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
Adding an integer to a pointer moves it forward by that many **elements**, not bytes: `p + 1` is the address of `numbers[1]`, and `*(p + 1)` is `20`. The compiler scales the step by the size of the type.
Indexing works on pointers too: `p[i]` is defined as `*(p + i)`, so `p[2]` is `30`. This is called **pointer arithmetic**.

---

Since `p + 1` is the next element, `p++` moves a pointer to the next element in place. A loop can walk an array by advancing a pointer instead of an index:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
Each turn prints the element `p` points to, then moves `p` one element forward.

---

When an array is passed to a function it **decays** to a pointer to its first element. This is why the parameters `int values[]` and `int *values` mean exactly the same thing, and why the function cannot know the length on its own: it only receives an address.
Pointers into the same array can be compared and subtracted. `end - start` is the number of elements between them, and a loop can run a pointer from one address to another:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Passing `numbers` and `numbers + 3` describes the first three elements without a separate size parameter.

---

Function arguments are passed **by value**: the function receives a copy, and assigning to a parameter never changes the caller's variable. To let a function change a variable, pass the variable's address and dereference the pointer inside:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
The classic example is swapping two variables, which needs a temporary copy of one value while the other is overwritten.

---

A function can `return` only one value. To hand back more, it takes pointers to variables owned by the caller and writes the results through them. Such parameters are called **output parameters**:
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo is 4, hi is 9
```
The caller declares the variables, passes their addresses, and finds them filled in after the call. Many standard functions use this pattern, which is why `scanf("%d", &n)` needs the `&`.

---

A pointer to a struct reaches the members with the arrow `->`, and the address of a struct stored in an array is taken with `&items[i]`. A function can also **return** a pointer, for example to the element it found:
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
The caller then reads members through the returned pointer with `->`, after checking that it is not `NULL`. Returning a pointer avoids copying the struct and lets the caller modify the original element.

---

`const` can protect either the value or the pointer, depending on where it is written:
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
Read the declaration from right to left: `p` is a pointer to a constant `int`; `q` is a constant pointer to an `int`. A pointer to const is the usual way to promise that a function only **reads** what it receives, as in `int sum(const int *values, int size)`. A normal variable can be passed to it; the promise only limits what the function can do.

---

A pointer is a variable, so it has an address of its own, and that address can be stored in a **pointer to pointer**, declared with two stars:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` is `p`, the address of `x`, and `**pp` follows both steps to reach `7`. Pointers to pointers let a function change which address a pointer holds: it receives `&p` and assigns to `*pp`.

---

Putting it together: a function that walks an array with a pointer, keeps a pointer to the best element seen so far and returns it, or `NULL` when there is nothing to return:
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
The caller compares the result with `NULL` before dereferencing it, and can use `result - values` to recover the index of the element.
