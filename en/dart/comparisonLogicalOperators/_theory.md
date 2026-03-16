The **equal operator** `==` compares two values and returns `true` if they are equal, or `false` if they are not.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

The result of a comparison is always a `bool` value.

---

The **not equal operator** `!=` returns `true` when two values are **different**, and `false` when they are the same.

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

It is the opposite of `==`.

---

The **greater than operator** `>` returns `true` when the left value is strictly larger than the right value.

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

If the left value is equal to or smaller than the right, it returns `false`.

---

The **less than operator** `<` returns `true` when the left value is strictly smaller than the right value.

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

If the left value is equal to or larger than the right, it returns `false`.

---

The **greater than or equal operator** `>=` returns `true` when the left value is larger than **or equal to** the right value.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Unlike `>`, this operator also returns `true` when both values are equal.
