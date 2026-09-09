Every value in JavaScript has a **type**. There are seven **primitive** types:
- `number` for any number, like `42` or `3.14`
- `string` for text, like `"Ana"`
- `boolean` for `true` and `false`
- `undefined` for a value that was never provided
- `null` for an intentionally empty value
- `bigint` for whole numbers of any size, like `9007199254740993n`
- `symbol` for unique identifiers created with `Symbol()`

Everything else (arrays, functions, objects created with `{}`, dates...) is an `object`.
The `typeof` operator tells you the type of a value, as a string:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript is **dynamically typed**: a variable has no type of its own, only the value it currently holds has one. The same variable can hold a number now and a string later, and `typeof` follows the value:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
This is convenient, but it also means that a function can receive a value of an unexpected type, so checking with `typeof` is a common first step. Since `typeof` returns a string, you compare its result with a string:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` has a few answers that surprise people.
Functions get their own answer, `"function"`, even though they are objects:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Arrays do **not** get their own answer: they are plain `"object"`, just like `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
And `typeof null` is `"object"`, a historical bug that was never fixed. So `typeof` distinguishes primitives and functions well, but it cannot tell an array, an object and `null` apart.

---

You can convert a value to another type **explicitly** by calling the type as a function:
- `Number(value)` converts to a number: `Number("42")` is `42`
- `String(value)` converts to a string: `String(42)` is `"42"`
- `Boolean(value)` converts to a boolean: `Boolean("")` is `false`

The result is a brand new value; the original is not changed:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Converting explicitly makes your intent visible: whoever reads `Number(input)` knows that `input` was text.

---

`Number()` is strict: the whole string must be a number, otherwise the result is `NaN` ("Not a Number"):
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` and `parseFloat()` are more forgiving: they read digits from the start of the string, skip leading spaces, and stop at the first character that is not part of a number. `parseInt` keeps only the whole part:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
When the string does not start with something that can begin a number (an optional sign, then a digit), they return `NaN` too:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` is the only value that is not equal to itself, so `x === NaN` is always `false`; to detect it use `Number.isNaN(x)`.

---

There are two ways to ask "is this `NaN`?", and they answer different questions.
The old global `isNaN(value)` first **converts** `value` to a number, then checks. So it says `true` for anything that cannot become a number, even if it is not `NaN` at all:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` does **not** convert: it is `true` only when `value` is really the number `NaN`:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Prefer `Number.isNaN`, and convert first if you want to know whether a conversion failed.

---

JavaScript also converts **implicitly**, and the `+` operator is where this bites most often. If either side is a string, `+` **concatenates** and the other side is converted to a string:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Every other arithmetic operator converts both sides to **numbers**:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
So adding values that come from text (user input, files, URLs) can silently build a string instead of a sum. Convert with `Number()` before adding to be safe.

---

A short way to convert a string to a number is the **unary plus**: a `+` placed in front of a single value converts it exactly like `Number()` does:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
It is compact, but easy to confuse with addition, so many teams prefer the explicit `Number("5")`.

---

The **loose** equality `==` converts the two sides to a common type before comparing, following rules that are hard to remember:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
The **strict** equality `===` never converts: values of different types are simply not equal:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Use `===` (and `!==`) by default. The only common exception is `value == null`, which checks `null` and `undefined` together.

---

When JavaScript needs a boolean, for example in an `if` condition or in `Boolean(value)`, it converts the value. Only eight values become `false`; they are called **falsy**:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` and `NaN`.
**Everything else is truthy**, including some values that look empty:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` is a non-empty string, so it is truthy; an empty array is an object, so it is truthy too.

---

A common shortcut to convert any value to a boolean is the **double negation** `!!`: the first `!` converts to a boolean and flips it, the second flips it back:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` and `Boolean(value)` give exactly the same result; the explicit form is easier to read.

---

JavaScript has a single `number` type for whole numbers and decimals: every number is a 64-bit floating point value (a *double*). So `5` and `5.0` are the same value, and there is no separate integer type:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
To ask whether a number has no fractional part, use `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Template literals convert the interpolated value to a string with the same rules as `String()`, so `${5.0}` becomes `"5"`, not `"5.0"`.

---

Because numbers are doubles, some decimals cannot be stored exactly and small errors appear:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
The `toFixed(digits)` method rounds a number to `digits` decimals, but it returns a **string**, which is fine for display and wrong for further math:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
To get a rounded **number**, convert the result back with `Number()`:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

A `number` can represent whole numbers exactly only up to `Number.MAX_SAFE_INTEGER`, which is `9007199254740991`. Beyond that, digits get lost:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
For bigger whole numbers use `bigint`: write the literal with an `n` suffix, or convert with `BigInt()`:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` shows the `n` suffix; `String(big)` gives the plain digits.
A `bigint` and a `number` cannot be mixed in arithmetic: `big + 1` throws a `TypeError`. Convert one side explicitly, with `BigInt(count)` or `Number(big)`.

---

Since `typeof` answers `"object"` for arrays, objects and `null`, telling them apart needs two extra checks.
`Array.isArray(value)` is `true` only for arrays:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
For `null` compare directly, `value === null`. Combining them gives a complete picture of any value:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Check for `null` and arrays first, because the plain `typeof` cannot distinguish them.

---

Text coming from forms, files or URLs is always a string, even when it represents a number or a boolean. Turning it back into the right type combines what you have seen: compare with `"true"` and `"false"` for booleans, and try `Number()` for numbers, remembering that `Number("")` is `0` and that `Number.isNaN` tells you when the conversion failed:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
When nothing matches, keep the string as it is.
