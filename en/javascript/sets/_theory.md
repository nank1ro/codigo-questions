A **Set** is a collection of **unique** values: every value can appear at most once, and there is no index to reach a value by position.
Sets are perfect when you only care about *which* values are present, not how many times or in what order.
You create an empty set with `new Set()`, add a value with `add(value)` and check whether a value is present with `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

Adding a value that is already in the set does **nothing**: duplicates are simply ignored.
Two more essentials:
- `delete(value)` removes the value from the set
- `size` is the number of values stored (a property, so no parentheses)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` returns the set itself, so several calls can be chained:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Whether you chain or not, a value that is already present is never added a second time, so `size` counts each distinct value only once.

---

You can build a set in one go by passing an array to `new Set()`. Duplicates in the array are dropped, so this is the quickest way to find the distinct values of an array:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
The **spread** operator `...` works the other way around and turns a set back into an array:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` does the same thing.

---

A set remembers the order in which values were added, and you can loop over it with `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Sets also have a `forEach()` method that calls a function for every value:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```

---

`delete(value)` returns `true` when the value was removed and `false` when it was not in the set.
To remove **every** value at once, call `clear()`:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// prints true
console.log(cart.delete("pen"));
// prints false
cart.clear();
console.log(cart.size);
// prints 0
```

---

A set decides whether two values are "the same" with almost the same rule as `===` (except that `NaN` counts as equal to itself). For strings and numbers this compares the content, but **objects are compared by reference**: two object literals with identical fields are two different values.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// prints 1
people.add({ name: "Alice" });
console.log(people.size);
// prints 2
```
Only adding the very same object again is ignored.

---

Combining spread and `filter()` gives you the classic operations of set theory. Each one builds a **new** collection and leaves the originals unchanged:
- **union**, every value that is in `a`, in `b` or in both: `new Set([...a, ...b])`
- **intersection**, only the values that are in **both**: `[...a].filter((x) => b.has(x))`
- **difference**, the values of `a` that are **not** in `b`: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// prints [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// prints [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// prints [ 1, 2 ]
```
Recent JavaScript engines also provide `a.union(b)`, `a.intersection(b)` and `a.difference(b)` directly on sets, but the spread and filter versions work everywhere.

---

To keep the same interface as `Map`, a set offers the iterator methods `values()`, `keys()` and `entries()`.
Since a set has no keys, `keys()` is just another name for `values()`, and `entries()` yields every value **twice**, as a `[value, value]` pair:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// prints [ 'a', 'b' ]
console.log([...letters.entries()]);
// prints [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
In practice you rarely need them: `for...of` and spread already loop over the values directly.

---

`new Set()` accepts any **iterable**, not just arrays. A string is iterable character by character, so it gives you the distinct characters of a text:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// prints [ 'h', 'e', 'l', 'o' ]
```
