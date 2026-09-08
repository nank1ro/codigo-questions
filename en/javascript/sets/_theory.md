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
