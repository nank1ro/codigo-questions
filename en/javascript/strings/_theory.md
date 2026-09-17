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

---

The `split(separator)` method breaks a string into an **array** of pieces, cutting at every `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// prints [ 'I', 'like', 'JavaScript' ]
```
The opposite is the array method `join(separator)`, which glues the pieces back into a string:
```javascript
console.log(words.join("-"));
// prints I-like-JavaScript
```

---

User input often has extra spaces around it. The `trim()` method returns a copy of the string with whitespace removed from **both** ends:
```javascript
let input = "   hello   ";
console.log(input.trim());
// prints hello
```
`trimStart()` removes only leading whitespace and `trimEnd()` only trailing whitespace.
Spaces in the middle of the string are never touched.

---

The `replace(search, replacement)` method returns a new string where the **first** occurrence of `search` is swapped for `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// prints blue red
```
To replace **every** occurrence, use `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// prints blue blue
```

---

The `repeat(count)` method returns the string repeated `count` times:
```javascript
console.log("ab".repeat(3));
// prints ababab
console.log("ab".repeat(0));
// prints an empty string
```

---

The `padStart(targetLength, padString)` method adds `padString` to the **start** of the string until it reaches `targetLength` characters. `padEnd()` does the same at the end:
```javascript
console.log("7".padStart(3, "0"));
// prints 007
console.log("Tea".padEnd(6, "."));
// prints Tea...
```
If the string is already long enough, it is returned unchanged.
Numbers do not have string methods, so convert them first with `String(number)`.

---

Two strings are equal with `===` only if they have exactly the same characters, in the same case:
```javascript
console.log("hello" === "hello");
// prints true
console.log("hello" === "Hello");
// prints false
```
The `<` and `>` operators compare strings alphabetically, character by character.
Uppercase letters come before lowercase ones, so `"Zoo" < "apple"` is `true`.

---

Strings are **immutable**: once created, a string can never be changed.
Assigning to an index does nothing, and every string method returns a **new** string instead of modifying the original:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// prints hello
word.toUpperCase();
console.log(word);
// prints hello
```
To keep a result, assign it back to the variable:
```javascript
word = word.toUpperCase();
```

---

Calling `split("")` with an empty separator turns a string into an array of its single characters.
Arrays have a `reverse()` method, so you can reverse a string by splitting, reversing and joining:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// prints cba
```
