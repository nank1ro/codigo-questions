JavaScript has two different ways to say "there is no value here".
`undefined` means that a value was **never provided**. A variable declared without a value holds `undefined`, and so does a property that does not exist in an object:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` is a value that **you** assign on purpose to say "empty, and I know it":
```javascript
let owner = null;
console.log(owner);
// prints null
```
So `undefined` is usually the language telling you that something is missing, while `null` is the programmer stating that something is intentionally empty.

---

Functions produce `undefined` in two more situations.
When you call a function with **fewer arguments** than it declares, the missing parameters hold `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
When a function finishes **without a `return`** (or with a bare `return;`), calling it gives `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Notice that passing `null` explicitly is not the same as omitting the argument: `greet(null)` prints `null`, because `null` is a real value that was handed to the function.

---

The `typeof` operator returns the type of a value as a string. For `undefined` it answers `"undefined"`, as you would expect:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
For `null`, however, it answers `"object"`. This is a bug from the very first version of JavaScript that was never fixed, because too much code depends on it:
```javascript
console.log(typeof null);
// prints object
```
So `typeof` is a reliable way to detect `undefined`, but not `null`. To check for `null`, compare with it directly: `value === null`.

---

How do `null` and `undefined` compare with each other? It depends on the operator.
The **loose** equality `==` treats them as the same thing, and considers them different from any other value, including `0`, `""` and `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
The **strict** equality `===` also compares the type, and `null` and `undefined` have different types:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

Most of the time you do not care *which* of the two "no value" markers you got: you just want to know whether a value is there.
Because `null == undefined` is `true` and nothing else is loosely equal to `null`, the comparison `value == null` is the standard idiom to catch **both** at once:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
This is the one case where `==` is preferred over `===`: writing `value === null || value === undefined` does exactly the same job, only longer.
Values such as `0`, `""` and `false` are *not* `null`: they are real values that happen to be falsy.

---

Reading a property of `null` or `undefined` is an error that stops the program:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` is `undefined`, and `undefined` has no properties. The **optional chaining** operator `?.` solves this: if the value on its left is `null` or `undefined`, the whole expression stops and evaluates to `undefined` instead of throwing:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
When the left side does have a value, `?.` behaves exactly like a normal `.`. You can chain several: `user.address?.street?.name` returns `undefined` as soon as any link is missing.

---

Optional chaining is not limited to dot properties. There are two more forms.
`?.[]` reads an element or a computed key only when the left side has a value:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` calls a function only when it exists, which is handy for optional callbacks:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
In every form, the check applies to the value **right before** the `?.`: `post?.tags?.[0]` is safe even when `post` itself is `null` or `undefined`.

---

Once you know a value may be missing, you usually want a **default** in its place. Two operators do that, and they differ in what they consider "missing".
`a || b` returns `b` whenever `a` is **falsy**: not only `null` and `undefined`, but also `0`, `""`, `false` and `NaN`.
The **nullish coalescing** operator `a ?? b` returns `b` only when `a` is `null` or `undefined`, and keeps every other value:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Use `??` when `0`, `""` or `false` are legitimate values that must be kept, and `||` when you really want to replace every falsy value.

---

A very common pattern is "fill in this property only if it is not set yet". Written with `??` it repeats the name:
```javascript
options.timeout = options.timeout ?? 1000;
```
The **nullish assignment** operator `??=` does the same in one step: it assigns the right side only when the left side is currently `null` or `undefined`, and leaves any other value untouched:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` stays `0` because `0` is not nullish; `timeout` did not exist, so it receives `1000`. The same idea exists for `||` as `||=`, which overwrites every falsy value.

---

A **default parameter** gives a parameter a value when the caller does not provide one. The rule is precise: the default is used only when the argument is `undefined`, which includes omitting it. Passing `null` does **not** trigger the default, because `null` is a value:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Default parameters follow the `undefined` rule, while `??` covers both `null` and `undefined`: choose the one that matches how your function will be called.

---

Optional chaining and the `== null` guard work well together: the chain reads the nested value without throwing, and the guard decides what to do when the result is missing:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Inside the last `return` a plain `.` is safe, because the guard has already proven that every link exists.

---

Many built-in methods report "nothing found" by returning `undefined`. The array method `find(callback)` is the typical example: it returns the first element for which the callback is `true`, or `undefined` when no element matches:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Reading `found.price` here would throw, so `?.` and `??` are the natural companions of `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` and `undefined` behave differently when an object is converted to JSON with `JSON.stringify()`.
JSON has a `null` value but no `undefined`, so a property whose value is `undefined` is simply **left out**, while a `null` property is kept:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Inside arrays the positions cannot disappear, so `undefined` becomes `null` there:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Checking `obj.key === undefined` cannot tell two situations apart: the property does not exist, or it exists and holds the value `undefined`.
`Object.hasOwn(obj, key)` answers the first question only: it returns `true` when the object has its **own** property named `key`, whatever its value:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"Own" means declared on the object itself: inherited members such as `toString` are available on every object but `Object.hasOwn(config, "toString")` is `false`.
