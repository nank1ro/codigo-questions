只要条件为 `true`，`while` 循环就会重复执行代码块。

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

循环在每次迭代**前**检查条件。当 `i < 3` 变为 `false` 时，循环停止。

---

计数器变量控制 `while` 循环的执行次数。

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

计数器从 `0` 开始，循环在每次迭代时递增，直到 `count < 5` 变为 `false`。

---

`do-while` 循环与 `while` 循环类似，但它**至少执行一次循环体** — 条件在每次迭代*之后*检查。

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

即使条件从一开始就是 `false`，循环体也会执行一次。

---

`while` 循环的条件可以包含任何布尔表达式。一旦条件求值为 `false`，循环就结束。

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

这里使用整除运算符（`~/`）在每次迭代时将 `n` 减半。

---

`break` 关键字立即退出循环，而不管循环条件如何。

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

没有 `break`，`while (true)` 循环将永远运行。这里当 `i` 到达 `3` 时循环停止。
