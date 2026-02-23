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
