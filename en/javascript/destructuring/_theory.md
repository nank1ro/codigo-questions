Reading values out of an array one index at a time is noisy:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**Destructuring** does the same job in one line. On the left of `=` you write a pattern that looks like the array itself, and every name inside it receives the element at the same position:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
The pattern does not have to cover the whole array: extra elements are simply ignored, and a name with no matching element becomes `undefined`.

---

Destructuring is most useful right where an array arrives: a function argument, or the result of a call. Instead of keeping the array around and indexing it everywhere, you unpack it once and give the parts real names:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
Nothing is copied or changed in the original array, the pattern only reads from it.

---

Sometimes only one element deep inside the array matters. You can leave a position empty in the pattern, keeping the comma that separates it: such an empty position is called a **hole**, and it skips the element without naming it:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
Count the commas, not the names: every comma moves the pattern one position forward, whether or not a name sits before it.

---

An array is not always as long as the pattern expects. Writing `= value` after a name gives it a **default**, used whenever the array has nothing at that position:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
The default is evaluated only when it is needed, so it may even be a function call, and a default can be given to any position, not just the last one.

---

A pattern can also stand on the left of a plain assignment, with no `const` or `let` in front, and then it writes into variables that already exist. That turns swapping two values into a single line, with no temporary variable:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
The right side is built first, so both old values are already safe inside the temporary array when the assignment happens. Mind the semicolon on the previous line: a line that starts with `[` would otherwise be read as an index of whatever came before.

---

Objects can be destructured too, with curly braces instead of square ones. Here position means nothing: each name is matched against the **key** that spells the same:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
Swapping `age` and `name` in the pattern changes nothing, and keys that the pattern does not mention are simply left behind. A name with no matching key becomes `undefined`.

---

Object patterns and defaults combine exactly like array ones, which makes them a tidy way to read a configuration object whose keys may or may not be there:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
Because the whole pattern is one statement, a function can unpack everything it needs from its argument on its very first line.

---

An object pattern names its variables after the keys, which is awkward when the keys are cryptic or already taken. Writing `key: newName` **renames** the variable:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
Read it as "take `n`, call it `name`". The colon does not declare a type, and `n` itself is never created as a variable, only `name` is. A renamed name can still get a default, written after it: `{ n: name = "unknown" }`.

---

Defaults have one rule that surprises everybody: they apply **only** to `undefined`. A key that exists and holds `null`, `0`, `""` or `false` is a real value, so the pattern takes it and the default is never used:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` behaves the same way as `0` here, even though it often means "no value" in an API response. When `null` must be replaced too, destructure first and fall back afterwards with `??`.

---

Where a key holds another object or an array, the pattern can simply keep going and describe that shape too:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
Careful with what that line creates: `address: { city }` means "go into `address`", not "give me `address`", so only `city` becomes a variable. To get both, mention the key twice: `const { address, address: { city } } = user;`. Array and object patterns nest into each other freely, as in `{ tags: [first] }`.

---

Taking the head of an array and keeping the tail is such a common need that patterns have their own syntax for it. Three dots in front of the last name make it a **rest element**, and it collects every remaining element into a brand new array:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
A rest element must come last in the pattern and cannot have a default: when nothing is left it is simply an empty array.

---

Object patterns have a rest too, and there it collects every key the pattern did not mention into a new object:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
This is the shortest way to build a copy of an object without one of its keys: the original is never touched, and the rest object is a fresh one holding the remaining values.

---

A pattern can replace a parameter name in a function declaration, so the unpacking happens as the call is made:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
Inside the body there is no object variable at all, only `width` and `height`. The caller passes one object, but the signature documents exactly which keys the function reads, and the keys can arrive in any order.

---

A destructured parameter with defaults makes a neat options object, but it still breaks when the caller passes nothing: reading a key from `undefined` throws a `TypeError`. Giving the whole pattern a default of `{}` fixes it:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
Read the line from the outside in: `= {}` supplies an empty object when the argument is missing, and each inner default then fills in its own key.

---

`Object.entries(obj)` turns an object into an array of `[key, value]` pairs. Put an array pattern in the head of a `for...of` loop and every pair is unpacked as the loop runs:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
This is the readable way to walk an object: no index, no lookup, just the two names you care about. `Object.keys` and `Object.values` give only one side each, `Object.entries` gives both.

---

Everything seen so far belongs to one syntax, so the pieces combine freely: an object pattern can nest another object pattern, which can hold a renamed key with a default, next to an array pattern ending in a rest element. One line then describes the whole shape a function expects:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
Keep it readable: a pattern that no longer fits on a couple of lines is usually a sign that the function is asking for too much.
