**等于运算符** `==` 比较两个值，如果它们相等则返回 `true`，如果它们不相等则返回 `false`。

```dart
int a = 5;
int b = 5;
bool result = a == b; // true
```

比较的结果总是一个 `bool` 值。

---

**不等于运算符** `!=` 在两个值**不同**时返回 `true`，在它们相同时返回 `false`。

```dart
int x = 3;
int y = 7;
bool result = x != y; // true
```

它是 `==` 的相反操作。

---

**大于运算符** `>` 在左值严格大于右值时返回 `true`。

```dart
int a = 8;
int b = 3;
bool result = a > b; // true
```

如果左值等于或小于右值，则返回 `false`。

---

**小于运算符** `<` 在左值严格小于右值时返回 `true`。

```dart
int a = 2;
int b = 9;
bool result = a < b; // true
```

如果左值等于或大于右值，则返回 `false`。

---

**大于或等于运算符** `>=` 在左值大于**或等于**右值时返回 `true`。

```dart
int score = 50;
bool passed = score >= 50; // true
```

与 `>` 不同，当两个值相等时，此运算符也返回 `true`。
