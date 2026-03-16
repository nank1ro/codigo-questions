Der **Gleichheitsoperator** `==` vergleicht zwei Werte und gibt `true` zurück, wenn sie gleich sind, oder `false`, wenn sie nicht gleich sind.

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

Das Ergebnis eines Vergleichs ist immer ein `bool`-Wert.

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

Der **Größer-oder-gleich-Operator** `>=` gibt `true` zurück, wenn der linke Wert größer als **oder gleich** dem rechten Wert ist.

```dart
int score = 50;
bool passed = score >= 50; // true
```

Im Gegensatz zu `>` gibt dieser Operator auch `true` zurück, wenn beide Werte gleich sind.
