Variables are containers for storing data values.
Every variable in Swift is an object.
To create a variable, we need to give it a **name** keeping in mind that it must not contain spaces.
A variable is created the moment you first assign a value to it.
In Swift you declare constants with the `let` keyword and variables with the `var` keyword.
The value of a constant can't be changed once it's set, whereas a variable can be set to a different value in the future.
An example of a variable creation named `x` is:
```swift
var x = 1
```
In this way we have assigned the value `1` to the variable named `x`.
If we print the variable `x` we get back the number `1`:
```swift
print(x) // prints 1
```

---

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

We can also give variables the values of other variables. Here, we can give to the `y` variable the value of `x`
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

When we update a variable, it forgets its previous value. Here we can display the `x` variable twice and see how its value updates.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

In Swift string variables can be declared only by using double quotes:
```swift
let x = "May"
```

---

If we want a variable name with multiple words, we use **camelCase**.
It is the practice of writing phrases such that each word in the middle of the phrase begins with a capital letter
