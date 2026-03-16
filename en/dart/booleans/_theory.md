A __boolean__ is a data type that can hold one of only two values: `true` or `false`.
In Dart, the boolean type is declared with the keyword `bool`.

```dart
bool isRaining = true;
```

The variable `isRaining` stores the value `true`, meaning it is currently raining.
Boolean values are always written in lowercase: `true` and `false`.

---

Just like any other variable, you can print a boolean value with `print()`.
When you print a boolean, Dart outputs the text `true` or `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

A boolean variable can also hold the value `false`.
Use `false` when something is not the case.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Just like `true`, `false` must be written in lowercase.

---

The __negation operator__ `!` (also called "not") flips a boolean value.
Applying `!` to `true` gives `false`, and applying `!` to `false` gives `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

This is useful when you want to check the opposite of a condition.

---

Booleans are used throughout programming to represent conditions and drive decisions.
Whenever your program needs to decide between two possibilities, a boolean is involved.

Examples:
- Is the user logged in? (`isLoggedIn`)
- Is the door open? (`isDoorOpen`)
- Has the order been shipped? (`isShipped`)
