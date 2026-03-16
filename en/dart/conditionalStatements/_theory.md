An **`if` statement** executes a block of code only when a condition is `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

The code inside the curly braces runs only if the condition `age >= 18` evaluates to `true`.

---

You can use `print()` inside an `if` block to display a message when a condition is met.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

If `isRaining` is `false`, nothing is printed.

---

An **`if-else` statement** runs the `if` block when the condition is `true`, and the `else` block when it is `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Exactly one of the two branches always executes.

---

**`else if`** lets you test multiple conditions in sequence. The first branch whose condition is `true` is executed, and the rest are skipped.

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

The **ternary operator** `condition ? expr1 : expr2` is a compact way to write a simple `if-else` expression.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

If the condition is `true`, `expr1` is used; otherwise `expr2` is used.
