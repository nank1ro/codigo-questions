The **addition operator** `+` adds two values together.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

You can use `+` with `int` or `double` values.

---

The **subtraction operator** `-` subtracts one value from another.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

The result can be negative if the second operand is larger than the first.

---

The **multiplication operator** `*` multiplies two values together.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Multiplying an `int` by another `int` produces an `int`. Multiplying with a `double` produces a `double`.

---

The **division operator** `/` divides one value by another. In Dart, `/` **always returns a `double`**, even when the result is a whole number.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Always use a `double` variable to store the result of `/`.

---

The **integer division operator** `~/` divides two numbers and **truncates** the result to an integer (discards any decimal part).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Use `~/` when you need a whole-number quotient without a remainder.
