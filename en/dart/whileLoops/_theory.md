A `while` loop repeats a block of code as long as a condition is `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

The loop checks the condition **before** each iteration. When `i < 3` becomes `false`, the loop stops.

---

A counter variable controls how many times a `while` loop runs.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

The counter starts at `0`, and the loop increments it each iteration until `count < 5` is `false`.

---

A `do-while` loop is similar to a `while` loop, but it **always executes the body at least once** — the condition is checked *after* each iteration.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Even if the condition is `false` from the start, the body runs once.

---

A `while` loop condition can involve any boolean expression. As soon as the condition evaluates to `false`, the loop ends.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Here, `n` is halved each iteration using integer division (`~/`).

---

The `break` keyword exits a loop immediately, regardless of the loop condition.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Without `break`, the `while (true)` loop would run forever. Here it stops when `i` reaches `3`.
