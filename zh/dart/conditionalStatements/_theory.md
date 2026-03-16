**`if` 语句**仅在条件为 `true` 时执行代码块。

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

只有当条件 `age >= 18` 为 `true` 时，花括号内的代码才会执行。

---

可以在 `if` 块内使用 `print()` 在条件满足时输出消息。

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

如果 `isRaining` 为 `false`，则不输出任何内容。

---

**`if-else` 语句**在条件为 `true` 时执行 `if` 块，在条件为 `false` 时执行 `else` 块。

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

两个分支中始终恰好执行一个。

---

**`else if`** 允许按顺序测试多个条件。第一个条件为 `true` 的分支会被执行，其余分支会被跳过。

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

**三元运算符** `condition ? expr1 : expr2` 是编写简单 `if-else` 表达式的简洁方式。

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

如果条件为 `true`，则使用 `expr1`；否则使用 `expr2`。
