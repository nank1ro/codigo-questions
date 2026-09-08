A function does not need a name. A **function expression** creates a function as a value, which you can store in a variable and call through it:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
An **arrow function** is a shorter way to write the same thing: drop the `function` keyword and put a "fat arrow" `=>` between the parameter list and the body:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Arrow functions are usually stored in a `const`, so the name cannot be reassigned by mistake, and are called exactly like any other function.

---

Arrow functions get shorter in two common cases.
When the body is a **single expression**, you can drop the curly braces and the `return` keyword: the value of the expression is returned automatically (an **implicit return**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
When there is **exactly one parameter**, you can also drop the parentheses around it:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
With zero parameters or with two or more, the parentheses are required: `() => 42` and `(a, b) => a + b`.

---

There is one trap with the implicit return. An arrow function whose body starts with `{` is read as a **block body**, never as an object literal:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Here `{ name: name }` is a block containing the label `name:` followed by the expression `name`. Nothing is returned, so the call gives `undefined`.
To return an object literal in one line, wrap it in **parentheses** so that JavaScript treats it as an expression:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Wrapping the object literal in parentheses is the standard way to build objects with a one-line arrow function, for example when you turn a couple of values into a record:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
An arrow function with no parameters starts with an empty pair of parentheses `()`:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Arrow functions really shine as **callbacks**: functions passed as arguments to other functions. Array methods are the most common example.
`map(callback)` returns a new array with the result of the callback for every element, and `filter(callback)` returns a new array with only the elements for which the callback returns `true`:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Both return a new array and leave the original untouched, so you can chain them: `numbers.filter(...).map(...)`.

---

Two more array methods take a callback.
`forEach(callback)` calls the callback once per element and returns nothing; use it for side effects such as printing.
`reduce(callback, initialValue)` folds the array into a single value: the callback receives the accumulated value so far and the current element, and returns the new accumulated value:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` orders an array in place using a callback that receives two elements and returns a negative number when the first should come first, a positive number when the second should come first, or `0` when they are equal. For numbers, `(a, b) => a - b` sorts in ascending order and `(a, b) => b - a` in descending order.
`find(callback)` returns the first element for which the callback returns `true`, or `undefined` if there is none:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

Arrow function parameters support the same features as regular function parameters.
A **default value** is used when the argument is omitted or is `undefined`:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Note that a parameter with a default value always needs the parentheses, even when it is the only one: `name = "World" => ...` is a syntax error.

---

A **rest parameter** `...name` collects any number of arguments into an array, and it works in arrow functions too:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Regular functions also have a hidden array-like `arguments` object holding every argument they received. Arrow functions **do not**: inside an arrow, `arguments` refers to the surrounding function's `arguments` or does not exist at all. Whenever you need "all the arguments" in an arrow function, use a rest parameter.

---

A function remembers the variables of the scope where it was **created**, even after that scope has finished running. This is called a **closure**.
The classic example is a counter maker: every call to `makeCounter` creates a fresh `count` and returns an arrow function that keeps using that same `count`:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Nobody else can read or reset `count`: it lives only inside the returned function. A second call to `makeCounter()` creates an independent counter with its own `count`.

---

Because a function is a value, an arrow function can **return another arrow function**. Chaining two arrows is a compact way to write a function that builds functions:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Read it from left to right: `makeAdder` takes `amount` and returns `(n) => n + amount`, an arrow function that captures `amount` through a closure. `makeAdder(1)(5)` calls the returned function immediately.
