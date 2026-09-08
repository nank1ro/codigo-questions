A **string** is a sequence of characters wrapped in quotes, like `"hello"` or `'hello'`.
Every string has a `length` property that tells you how many characters it contains:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
Spaces and punctuation count as characters too.

---

Each character in a string has an **index**, starting from `0`.
You can read a single character with square brackets or with the `charAt()` method:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
The last character is at index `length - 1`:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

Strings come with many built-in **methods**. Two of the simplest change the case of every letter:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
```
Both methods take no arguments, so remember the parentheses.

---

To check whether a string contains another string, use these methods, which all return a boolean:
- `includes(text)` is `true` if `text` appears anywhere
- `startsWith(text)` is `true` if the string begins with `text`
- `endsWith(text)` is `true` if the string ends with `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
The comparison is case-sensitive: `"Hello".includes("h")` is `false`.

---

The `indexOf()` method returns the index where a piece of text **first** appears in the string.
If the text is not found, it returns `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

The `slice(start, end)` method extracts a piece of a string, from index `start` up to (but not including) index `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
```
If you omit `end`, the slice goes to the end of the string.
A negative index counts from the end: `word.slice(-3)` is `"ipt"`.
The `substring(start, end)` method works the same way but does not accept negative indexes.

---

`indexOf()` and `slice()` work well together: find where something is, then cut the string there.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// prints 45
```
