A `for` loop repeats a block of code a set number of times. The basic syntax is:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: runs once before the loop starts (e.g., `int i = 0`)

**condition**: checked before each iteration; loop stops when false

**update**: runs after each iteration (e.g., `i++`)

---

You can use the loop variable inside the body to track the current count. For example, accumulating a sum:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

After the loop, `total` equals 15.

---

A `for` loop can count **downward** by using a decrement (`i--`) and a `>=` condition:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

This is useful for countdowns or reverse iteration.

---

The `for-in` loop iterates over every element in a collection without needing an index:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

Each iteration assigns the next element to the loop variable (`fruit` here).

---

The `break` statement exits a loop immediately when a condition is met:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

This is useful when searching for a value and you want to stop once it is found.
