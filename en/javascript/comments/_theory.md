A **comment** is a note written inside the source code for the people who read it. JavaScript ignores comments completely, so they never change what the program does.

The simplest comment is the **single-line comment**: it starts with `//` and runs until the end of the line.
```javascript
// Greets the user
console.log("Hello");
```
Use comments to explain what a piece of code is for, or why it was written that way. Note that, unlike some other languages, `#` does **not** start a comment in JavaScript.

---

A comment does not need its own line: it can follow the code on the same line. This is an **inline comment** (or trailing comment), and it is a good place for a short note about that specific statement:
```javascript
const retries = 3; // give up after three attempts
```
Everything from `//` to the end of the line is ignored, while the code before it runs as usual.

---

Because comments are ignored, adding or deleting a comment never changes what a program does. Only the code that is **not** commented runs.

This makes `//` a quick way to switch a line of code off without deleting it. This is called **commenting out**:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
The second line is now a comment, so `total` stays `10`. Removing the `//` brings the line back to life.

Commenting out is handy while you experiment, but remember to clean up: code that stays commented out for a long time only confuses whoever reads it next.

---

When a comment needs more than one line, JavaScript offers the **multi-line comment** (also called a block comment): it starts with `/*` and ends with `*/`, and everything in between is ignored, including line breaks.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
A block comment can also be short and stay on one line: `/* like this */`.

---

Whatever kind of comment you use, the rule is the same: the text inside it is **not code**. A `console.log` inside a comment never prints anything, and code written after `//` on the same line never runs, even when the line starts with real code:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
When you are not sure what a program prints, mentally delete every comment first and read what is left.

---

Unlike `//`, which stops at the end of the line, a `/*` comment only stops at the `*/`. If you forget to close it, JavaScript treats all the following code as part of the comment and reports a syntax error:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Both `//` and `/* */` work as inline comments, but with `/*` always make sure the `*/` is there.

---

Block comments in JavaScript **cannot be nested**: the comment ends at the **first** `*/` it meets, no matter how many `/*` came before it.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Here the comment ends right after `inner`, so `still a comment */` is read as code and causes a syntax error. Keep this in mind when you comment out a block that already contains a `/* */` comment: use `//` on each line instead, or remove the inner comment first.

---

To comment out several lines at once, wrap them in a single block comment instead of adding `//` to every line:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Since the lines inside the block are ignored, `total` never changes. Remember that this only works when none of those lines contains a `*/`.

---

JavaScript has a third kind of comment, the **documentation comment**, written in the **JSDoc** format: a block comment that starts with `/**` (two asterisks) placed directly above a function. Inside it, lines usually start with ` * ` and special **tags** beginning with `@` describe the function:
- `@param {type} name description` for each parameter
- `@returns {type} description` for the return value

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
To JavaScript it is just a comment, but editors read it and show it as the help text for `greet`, together with the type written in braces (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

The first line of a JSDoc comment is the **summary**: a short sentence that says what the function does. Write it in the third person, as if describing the function: "Returns...", "Adds...", "Checks...". Then list the tags, one per line:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
The comment must sit right above the declaration, with no blank line in between, otherwise editors do not attach it to the function.

---

A JSDoc comment is also a **contract**: it tells whoever calls the function what to pass and what to expect back, before the body is even written. Reading the comment is often enough to implement the function:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Each `@param` matches one parameter, in the same order, and `@returns` describes every possible result.

---

The order inside a JSDoc comment is always the same: the summary first, then one `@param` per parameter in the order they are declared, then `@returns` last. The opening `/**` and the closing ` */` wrap everything, and the comment sits directly above the function it describes:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

A JavaScript file can start with a special line called the **shebang** (or hashbang): `#!` followed by the path of the program that should run the file. On Unix-like systems it lets you run a script directly from the terminal, like `./hello.js`, without typing `node` first:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignores this line exactly like a comment, but only when it is the **very first line** of the file: anywhere else, `#!` is a syntax error. `/usr/bin/env node` means "find `node` on this system and use it".

---

A good comment explains **why** the code does something, not **what** it does. The code already shows what happens; repeating it in words adds noise and goes stale as soon as the code changes:
```javascript
// set timeout to 30
const timeout = 30;
```
The reason behind the number is what a reader cannot guess:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
If a comment only restates the line below it, delete it or replace it with the reason.

---

Some comments follow a convention that editors understand. The most common **markers** are:
- `// TODO: ...` flags something that still needs to be written
- `// FIXME: ...` flags code that is known to be wrong and must be corrected

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
To JavaScript they are ordinary comments; editors list them so pending work is easy to find. A `TODO` usually sits next to a placeholder that keeps the code running until the real implementation is written. When you complete the work, replace the placeholder and remove the marker in the same change: a stale `TODO` is misleading.

---

A `FIXME` is different from a `TODO`: the code already exists, but it is known to be wrong. A good `FIXME` says what the bug is and, when possible, gives an example that shows it, so the next person can fix it quickly. As with `TODO`, delete the marker once the bug is fixed, but keep the JSDoc comment, which is still true.
