A String _template_ is a programmatic way to generate a String.
In Kotlin we can use the `+` sign (concatenation) to display two or more strings together, like:
```kotlin
println("Hello " + "Kotlin!")
// prints "Hello Kotlin!"
```

---

But using the sign `+` to add a number like '10' to a string like ` "friends"` produces an error as they are a different kind of values

---

String templates allow us to display expressions like adding a string to a number, without any error.
Placing an expression inside `${}` evaluates it.
The return value is converted to a String and inserted into the resulting String

---

If you put a $ before an identifier name, the String template will insert that identifier's contents into the String

---

If what follows the `$` sign isn't recognizable as a program identifier, nothing special happens

---

We can also insert variables after the dollar signs to show their value

---

We can use curly brackets to insert values as often as we like inside the string templates

---

Inside the `${}` we can also put conditions, for example:
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// prints Correct
```

---

String templates are best used in print statements, but we can also store them in variables like normal strings.
