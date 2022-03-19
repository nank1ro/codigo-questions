In Swift we can use the `+` sign to display two or more strings together, like:
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

But using the sign `+` to add a number like '10' to a string like ` "friends"` produces an error as they are a different kind of values

---

String interpolation allow us to display expressions like adding a string to a number, without any error.

---

Every string interpolation statement consists of two parts, the `\()` where we insert the number or variable, and the normal string

---

Next, we add the different kind of value in curly braces so it'll display as one print statement. Like here, with `\(5)`

---

Inserting variables like `friends` between the round brackets displays their value too

---

We can use round brackets to insert values as often as we like inside the string interpolation

---

String interpolations are best used in print statements, but we can also store them in variables like normal strings.
