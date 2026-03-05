You might have considered the situation where you would like to reuse a piece of code, just with a few different values.
Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
In Swift we use the `func` keyword followed by the name of the function:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

The parentheses in the __function definition__ don't have to be empty if we want to specify parameters

---

Sometimes we want a function to __return__ a value.
Well, there's the `return` keyword.

---

Functions can have multiple input parameters, which are written within the function's parentheses, separated by commas.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

You can use a tuple type as the return type for a function to return multiple values as part of one compound return value.

---

If you don't want an argument label for a parameter, write an underscore `_` instead of an explicit argument label for that parameter

---

You can define a _default_ value for any parameter in a function by assigning a value to the parameter after that parameter's type.
If a default value is defined, you can omit that parameter when calling the function
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

A _variadic parameter_ accepts zero or more values of a specified type.
You use a variadic parameter to specify that the parameter can be passed a varying number of input values when the function is called.
Write variadic parameters by inserting three period characters `...` after the parameter's type name.
The values passed to a variadic parameter are made available within the function's body as an array of the appropriate type.
For example, a variadic parameter with a name of `numbers` and a type of `Double...` is made available within the function's body as a constant array called numbers of type `[Double]`

---

In functions we can add an _optional comment_ that explains what the function does:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
We can use `///` for a single line comment and `/** */` for a multi line comment
