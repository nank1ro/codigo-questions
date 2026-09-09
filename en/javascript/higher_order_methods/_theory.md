In JavaScript a function is a **value**: you can store it in a variable, put it in an array, and pass it to another function as an argument. A function that receives a function as an argument, or returns one, is called a **higher-order function**. The function passed in is called a **callback**, because the receiver *calls it back* when it needs to:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Note that `shout` is passed **without parentheses**: `twice(shout, "hi")` hands over the function itself, while `twice(shout("hi"), "hi")` would first call `shout` and pass its result, the string `"HI!"`, which cannot be called.

---

Higher-order functions let you separate *what to do with each element* from *how to walk through the elements*. The walking part is written once, and the callback decides the rest:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
The callback receives one element at a time. It can be an arrow function written inline, like above, or any function stored in a variable. This is exactly how the built-in array methods you will meet next work internally.

---

The built-in `map` does what `transform` does: it calls the callback for every element and collects the results into a **new array**. `forEach` also calls the callback for every element, but it collects nothing and always returns `undefined`; use it only for side effects, such as printing:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
A common mistake is to store the result of `forEach` or to chain another method after it: there is nothing to chain, because it returns `undefined`. Rule of thumb: use `map` when you need the new values, `forEach` when you only need to *do* something.

---

Two more higher-order methods cover most everyday needs.
`filter(callback)` returns a new array with only the elements for which the callback returns `true`; a callback that answers yes or no like this is called a **predicate**.
`reduce(callback, initialValue)` combines all the elements into a single value: the callback receives the **accumulator** (the result so far) and the current element, and returns the new accumulator. The second argument of `reduce` is the starting accumulator:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Because `filter` and `map` return arrays, you can chain them and finish with `reduce`: `numbers.filter(...).map(...).reduce(...)`.

---

Three methods answer questions about an array with a predicate:
- `find(predicate)` returns the **first** element for which the predicate is `true`, or `undefined` if there is none
- `some(predicate)` returns `true` if **at least one** element satisfies the predicate
- `every(predicate)` returns `true` if **all** elements do (and `true` for an empty array)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
All three stop as soon as the answer is known, so they never look at more elements than needed.

---

`sort(compare)` orders an array **in place** using a callback that receives two elements and returns a negative number when the first should come first, a positive number when the second should come first, or `0` when they are equal. For numbers, `(a, b) => a - b` sorts in ascending order and `(a, b) => b - a` in descending order.
Without a comparator, `sort()` converts every element to a **string** and compares them character by character, so `10` comes before `9` because `"1"` is less than `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Since `sort` modifies the array, sort a copy when you also need the original order: `[...numbers].sort(...)`. For strings use `(a, b) => a.localeCompare(b)` as the comparator, which orders text alphabetically.

---

The comparator can look at any part of the elements, so an array of objects is sorted by one of their properties just by comparing that property:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Sorting the copy leaves `items` in its original order.

---

A higher-order function can also **return** a function. The returned function remembers the variables of the place where it was created, even after the outer function has finished: this is called a **closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Each call to `makeMultiplier` creates a new function with its own `factor`. This is how you build a family of similar functions from one template. The same can be written with arrows: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

A closure keeps a **live** link to the variable, not a copy of its value. When several functions are created in the same call, they share the same variable, and every change made through one is visible to the others:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Nobody can read or reset `count` from outside except through those two functions: the variable is **private**. A second call to `makeCounter()` creates a completely separate `count`.

---

Because functions are values, you can write a higher-order function that **combines** two functions into a new one. `compose(f, g)` returns a function that applies `g` first and then `f` to the result, matching the mathematical notation *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
The order matters: `compose(f, g)` runs `g` first, then `f`. Building programs out of small functions glued together this way is called **function composition**.

---

A function that returns a function is also the natural way to **adapt** a callback. Suppose you have a predicate and you need its opposite for `filter`: instead of rewriting it, wrap it:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
A general `not(predicate)` would do this for any predicate: it returns a new function that calls `predicate` with the same argument and flips the result with `!`. Predicates for `filter`, `find`, `some` and `every` receive the element as their first argument, so the wrapper only needs to forward that one value.

---

The accumulator of `reduce` does not have to be a number: it can be a string, an array or an object. Starting from an empty object `{}` you can count or group things in one pass. Remember to **return the accumulator** from the callback, otherwise the next step receives `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` reads the current count, or `0` when that key does not exist yet.

---

Every function has a method `bind` that returns a **new** function with some things fixed in advance. Its first argument becomes the `this` of the new function; the remaining arguments are placed in front of whatever the new function is called with (a **partial application**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Fixing `this` matters for methods. When a method is copied out of its object and called on its own, `this` no longer refers to the object, so `this.name` becomes `undefined`. `bind` locks it to the object:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
The original function is never changed: `bind` always builds a new one, whose `name` is the original name prefixed with `bound `.

---

Real programs combine these methods into a **pipeline**: filter the elements you care about, map them to the values you need, and reduce them to a result. Storing the intermediate arrays in constants keeps each step readable and lets you reuse them:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` turns an array of strings into a single string with the elements separated by a comma and a space.

---

Closures let a returned function keep **private state** between calls. A classic helper built this way is `once(fn)`: it returns a function that runs `fn` only the first time it is called, remembers the result, and returns that same result on every later call without running `fn` again:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
The wrapper needs two private variables: whether `fn` has already run, and the stored result. Both live in the closure, invisible to the outside world. To forward every argument of the wrapper to `fn`, declare the wrapper with a rest parameter `(...args)` and call `fn(...args)`.

---

Everything comes together in `groupBy(items, keyFn)`: a higher-order function that receives a callback deciding the **group key** of each element and returns an object mapping every key to the array of elements with that key. `reduce` with an object accumulator does the whole job:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
For each element, compute the key, create the array for that key if it does not exist yet (`acc[key] ?? []`), push the element and return the accumulator. Because the caller chooses `keyFn`, the same function groups words by initial, people by city or numbers by parity.
