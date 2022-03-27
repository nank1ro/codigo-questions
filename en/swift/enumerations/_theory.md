An `enumeration` defines a common type for a group of related values and enables you to work with those values in a type-safe way within your code.
We declare enumerations using the `enum` keyword:
```swift
enum Colors {
	case blue
	case red
	case green
}
```
The values defined in an enumeration (such as `blue`, `red` and `green`) are its _enumeration cases_.
We use the `case` keyword to introduce new enumeration cases.

---

Multiple cases can appear on a single line, separated by commas:
```swift
enum Colors {
	case blue, red, green
}
```

---

We can match individual enumeration values with a `switch` statement:
```swift
let color = Colors.red
switch color {
	case .blue:
		print("Blue")
	case .red:
		print("Red")
	case .green:
		print("Green")
}
// prints "Red"
```
Keep in mind that if you don't need to provide a `case` for every enumeration case, you can provide a `default` case to cover any cases that aren't addressed explicitly

---

For some enumerations, it's useful to have a collection of all of that enumeration's cases.
You enable this by writing `: CaseIterable` after the enumeration's name.
Swift exposes a collection of all the cases as an `allCases` property of the enumeration type:
```swift
enum Colors: CaseIterable {
	case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
