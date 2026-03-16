**加法运算符** `+` 将两个值相加。

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

你可以对 `int` 或 `double` 值使用 `+`。

---

**减法运算符** `-` 从一个值中减去另一个值。

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

如果第二个操作数大于第一个，结果可能为负。

---

**乘法运算符** `*` 将两个值相乘。

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

将 `int` 与另一个 `int` 相乘会产生 `int`。与 `double` 相乘会产生 `double`。

---

**除法运算符** `/` 将一个值除以另一个值。在 Dart 中，`/` **总是返回 `double`**，即使结果是整数。

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (不是 5!)
```

始终使用 `double` 变量来存储 `/` 的结果。

---

**整数除法运算符** `~/` 将两个数相除并**截断**结果为整数（丢弃小数部分）。

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (不是 3.333...)
```

当你需要整数商而不需要余数时，使用 `~/`。
