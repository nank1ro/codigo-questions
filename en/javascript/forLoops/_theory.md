We know how to repeat code using a `while` loop.
Like this program repeating statements to display `hello`
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
But we can do the same with `for` loops:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

In a `for` loop we can specify how many times we'd like our loop to run

---

We can use `<` to loop until the next number excluded, or `<=` to loop until the next number included

---

The variable called `i` is the counter variable.
We can give it the name we want.
It counts what repetition of the loop we're currently on

---

In JavaScript we have also the `forEach` loop.
In fact, `forEach` calls the given closure on each element in the sequence in the same order as a `for` loop:
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
Using the `forEach` method is distinct from a `for` loop in two important ways:
1. The `break` or `continue` statements cannot be used to exit the current call of the body closure or to skip subsequent calls.
2. Using the `return` statement in the body closure will only exit the closure and not the outer scope, and it won't skip subsequent calls.
NOTE: `=>` this is called _arrow function_ and it's an ES6 shorter function syntax that replaces curly brackets {} and returns the value (if needed)
