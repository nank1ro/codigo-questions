A **comment** is text inside your source code that is meant for people, not for the compiler. The compiler throws comments away before it builds the program, so you can use them to explain what the code is for, leave reminders or note a decision.

The most common kind is the **single-line comment**: everything from `//` to the end of that line is ignored.
```c
// Greet the user
printf("Hello\n");
```
The first line does nothing when the program runs; only the `printf` produces output.

---

Because the compiler removes comments completely, adding or deleting a comment never changes what a program does. Only the code that is **not** commented runs.

This makes `//` a quick way to switch a line of code off without deleting it. This is called **commenting out**:
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
The second line is now a comment, so `total` stays `10`. Removing the `//` brings the line back to life.

Commenting out is handy while you experiment, but remember to clean up: code that stays commented out for a long time only confuses whoever reads it next.

---

When a comment needs more than one line, C offers the **multi-line comment** (also called a block comment): it starts with `/*` and ends with `*/`, and everything in between is ignored, including line breaks.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
A block comment can also be short and stay on one line: `/* like this */`.

Unlike `//`, which stops at the end of the line, a `/*` comment only stops at the `*/`. If you forget to close it, the compiler will treat all the following code as part of the comment.

---

Block comments **do not nest**. The compiler ends a `/*` comment at the very first `*/` it finds, no matter how many `/*` came before it:
```c
/* outer /* inner */ still code */
```
Here the comment ends right after `inner`, so `still code */` is compiled as code and produces an error.

This matters when you want to comment out a block that already contains a `/* */` comment: the inner `*/` would close your outer comment too early. In that case, put `//` in front of each line instead.

---

A comment does not need its own line: it can follow the code on the same line. This is a **trailing comment**, and it is a good place for a short note about that specific statement:
```c
int retries = 3; // give up after three attempts
```
Both `//` and `/* */` work as trailing comments, but be careful with `/*`: since it only stops at `*/`, an unclosed `/*` at the end of a line swallows the lines that follow, and the program no longer compiles.

---

A common use of block comments is the **header comment**: a short block placed directly above a function that says what it does, what its parameters mean and what it returns.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Whoever calls `to_seconds` can now read the header instead of the body. Keep the header next to the function so they are updated together.

---

The compiler replaces every comment with a single space. This means a `/* */` comment can appear anywhere a space can, even in the middle of a statement or an expression:
```c
int area = width /* cm */ * height /* cm */;
```
This is occasionally useful to label the operands or the arguments of a call. A `//` comment cannot do this, because it would comment out the rest of the line, including the code after it.

---

Programmers use a few conventional keywords at the start of a comment to flag work that is not finished:

- `TODO` marks something that still needs to be written
- `FIXME` marks code that is known to be wrong and must be corrected

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Editors and tools can list these markers, so the pending work is easy to find. Once the work is done, delete the marker: a stale `TODO` is misleading.

---

A good comment explains **why** the code does something, not **what** it does. The code already shows what happens; repeating it in words adds noise and goes stale as soon as the code changes:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
The reason behind the numbers is what a reader cannot guess:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
If a comment only restates the line below it, delete it or replace it with the reason.

---

Putting it together: use `//` for short notes and trailing comments, `/* */` for longer blocks and header comments, mark unfinished work with `TODO` or `FIXME`, and remove commented-out code and stale markers once they are no longer needed.
