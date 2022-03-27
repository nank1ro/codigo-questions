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
