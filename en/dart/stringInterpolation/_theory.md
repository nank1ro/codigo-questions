A String _interpolation_ is a programmatic way to generate a String.
In Dart we can use the `+` sign (concatenation) to display two or more strings together, like:
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

But using the sign `+` to add a number like '10' to a string like ` "friends"` produces an error as they are a different kind of values

---

String interpolation allow us to display expressions like adding a string to a number, without any error.
Placing an expression inside `${}` evaluates it.
The return value is converted to a String and inserted into the resulting String

---

If you put a `$` before an identifier name, the string interpolation will insert that identifier's contents into the `String`

---

If what follows the `$` sign isn't recognizable as a program identifier, you are going to encounter an error

---

We can also insert variables after the dollar signs to show their value

---

We can use curly brackets to insert values as often as we like using the string interpolation

---

Inside the `${}` we can also put conditions, for example:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

String interpolation is best used in print statements, but we can also store them in variables like normal strings.
