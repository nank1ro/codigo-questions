Decision making is required when we want to execute code only if a certain condition is satisfied.
Let's assume we want to play outside only if the weather is nice.
In programming, we can save a boolean variable `nice_weather` and perform the action of playing outside `if` this variable is `true`, like:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Let's continue with the previous example.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
We've seen that the `if` statement executes the block of code only if the condition is `true`.
Another important thing to consider is represented by the **curly brackets** `{}` which indicate a code block.

---

We just saw how to execute a block of code if a condition occurs, now let's see how to execute another block of code if the first condition fails.
We go to play outside if the weather is nice; otherwise, we stay home.
In C we can use the `else` statement, like:
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

Let's assume we have another condition to check, like in this example:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
and the output of this code is `the number is 3`.
First of all, let's check if the number is equal to 2, this is false.
So let's move on to the second statement and check if `num` is equal to 3, being true we execute the following block of code by printing `the number is 3`

---

We can add as many `else if` statements as we want, there are no limits
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
and the output of this code is `the number is 4`.

---

We can also nest a conditional statement (`if`, `else if` or `else`) inside another conditional statement, to create a more complex structure.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
and the output of this code is `the number is 4`.

---

Time to put the `if` statement's syntax into practice: the keyword, a condition in parentheses, and a code block wrapped in curly braces.
```c
if (condition) {
    // runs when condition is true
}
```

---

C's boolean literals are `true` and `false`: lowercase, unquoted, and defined by `<stdbool.h>` rather than being built into the language. Writing `True` won't compile as a condition — only the lowercase form works, and when it's `true` the block runs.

---

C has no separate boolean test: a condition is true whenever its value is anything other than zero. `false` from `<stdbool.h>` is simply `0`, so a block guarded by it never runs.

---

An `if` statement in C is made of three parts: the `if` keyword, a condition in parentheses, and a block in braces. The parentheses are required — they are how the compiler knows where the condition ends.

---

Every conditional statement starts with a keyword that tells the compiler a condition needs to be checked before deciding what runs next.

---

A literal `true` condition is always true, so the block runs and its `printf` executes exactly as written.

---

A literal `false` condition is never true, so the block is skipped completely and nothing inside it runs.

---

Conditions are the values an `if` statement checks: when a condition is `true` the block runs, when it's `false` it's skipped.

---

The opening brace may sit on the same line as the condition or on the line below it. C ignores the line break, so both styles compile to exactly the same program.

---

The parentheses around a condition are part of C's `if` syntax, not optional grouping: `if true { ... }` does not compile.

---

A quoted `"false"` is a string, not a boolean — and a string in a condition is a non-null address, which counts as true. Only the unquoted `false` keeps the block from running.

---

Spacing between the pieces of an `if` line is free in C: `if(true){` and `if (true) {` are the same statement to the compiler, so only the order of the pieces matters.

---

A code block isn't limited to one statement. Every statement between the braces runs, one after another, in the order it is written.

---

A boolean variable can be used directly as a condition, no comparison needed. Since `online` already holds `true`, writing `if (online)` on its own is enough to run the block.

---

A `bool` variable works as a condition because `if` looks only at the value stored in it at that moment. With `false` in `online`, `if (online)` behaves exactly like `if (false)`.

---

Only the code between an `if` statement's curly braces is conditional. Anything written after the closing brace runs unconditionally, no matter what the condition was.

---

There's no fixed limit on how many statements a code block can hold — one line or a hundred, they all run together when the condition is `true`.

---

Reading a boolean variable as a condition works just like a literal: since `online` holds `true`, the block executes and its `printf` runs.

---

When `online` holds `false` instead, the condition is false, so the block is skipped completely and nothing inside those braces gets printed.
