**等号演算子** `==` は2つの値を比較し、等しい場合は `true`、そうでない場合は `false` を返します。

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

比較の結果は常に `bool` 値です。

---

**不等号演算子** `!=` は、2つの値が**異なる**場合は `true`、同じ場合は `false` を返します。

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

`==` の反対です。

---

**より大きい演算子** `>` は、左の値が右の値より厳密に大きい場合に `true` を返します。

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

左の値が右の値以下の場合は `false` を返します。

---

**より小さい演算子** `<` は、左の値が右の値より厳密に小さい場合に `true` を返します。

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

左の値が右の値以上の場合は `false` を返します。

---

**以上演算子** `>=` は、左の値が右の値より大きい**または等しい**場合に `true` を返します。

```dart
int score = 50;
bool passed = score >= 50; // true
```

`>` と異なり、この演算子は両方の値が等しい場合にも `true` を返します。
