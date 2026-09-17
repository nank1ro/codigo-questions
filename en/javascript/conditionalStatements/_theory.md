Decision making is required when we want to execute code only if a certain condition is satisfied.
Let's assume we want to play outside only if the weather is nice.
In programming, we can save a boolean variable `niceWeather` and perform the action of playing outside `if` this variable is `true`, like:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

Let's continue with the previous example.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```
We've seen that the `if` statement executes the block of code only if the condition is `true`.
Another important thing to consider is represented by the **curly brackets** `{}` which indicate a code block.

---

We just saw how to execute a block of code if a condition occurs, now let's see how to execute another block of code if the first condition fails.
We go to play outside if the weather is nice; otherwise, we stay home.
In JavaScript we can use the `else` statement, like:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Let's assume we have another condition to check, like in this example:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
and the output of this code is `the number is 3`.
First of all, let's check if the number is equal to 2, this is false.
So let's move on to the second statement and check if `num` is equal to 3, being true we execute the following block of code by printing `the number is 3`

---

We can add as many `else if` statements as we want, there are no limits
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
and the output of this code is `the number is 4`.

---

We can also nest a conditional statement (`if`, `else if` or `else`) inside another conditional statement, to create a more complex structure.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
and the output of this code is `the number is 4`.

---

The ternary conditional operator is a special operator with three parts, which takes the form `question ? answer1 : answer2`.
It's a shortcut for evaluating one of two expressions based on whether `question` is true or false.
If `question` is true, it evaluates `answer1` and returns its value; otherwise, it evaluates `answer2` and returns its value.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// prints 10
```
The shortand code for the above code is:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
```
`c` is set equal to `a`, because the condition `a < b` was true

---

The _nil-coalescing operator_ `a ?? b` unwraps an optional `a` if it contains a value, or returns a default value `b` if `a` is `nil`.
The expression `a` is always of an optional type.
The expression `b` must match the type that is stored inside a.
The nil-coalescing operator is shorthand for the code below:
```javascript
a != nil ? a! : b;
```

---

`if` is the keyword that introduces a conditional statement in JavaScript. There is no `elif` keyword here — a second condition is introduced with `else if`, written as two separate words.

---

JavaScript's boolean literals are lowercase: `true` and `false`, not `True`/`False`, and not the strings `"true"`/`"false"`.

---

To keep a code block from running, the condition inside the parentheses must evaluate to `false`.

---

The space between `if` and its parentheses is purely cosmetic: `if(true)` and `if (true)` are the same statement to JavaScript.

---

The curly braces are what group several statements into one block. Without them an `if` controls only the single statement that follows it, so `if (true) console.log("Hello!");` is valid JavaScript.

---

The condition is evaluated once, before the block starts. JavaScript doesn't look at it again while the statements between the braces are running.

---

A `false` condition skips the block entirely, and the program continues at the first statement after the closing brace.

---

A condition doesn't have to be a boolean: JavaScript converts whatever it finds to one, so `if (1)` runs its block and `if (0)` doesn't. A literal `true` needs no conversion at all.

---

A code block isn't limited to a single line — every statement inside the curly braces runs, in order, when the condition is `true`.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
and the output is `First line` followed by `Second line`.

---

Statements inside a block run one after another, top to bottom, so two `console.log` calls in the same block print on two separate lines.

---

Indenting the statements inside a block is a readability convention only. JavaScript uses the curly braces, never the indentation, to decide what belongs to the block.

---

Statements such as `if`, `else if`, and `else`, that run or skip code depending on whether a condition is `true` or `false`, are called **conditional statements**.

---

A boolean variable, even one built from a `!` negation like `isAfternoon`, can be used directly as an `if` condition, no comparison needed.

---

The condition of an `if` statement always goes inside parentheses `()`, placed right after the `if` keyword and before the opening curly brace.

---

A block can hold any number of statements, and it can also hold none: `if (true) {}` is valid JavaScript that simply does nothing.

---

The code block of an `if` statement is the set of instructions inside the curly braces `{ }`, the part that actually runs when the condition is `true`.
