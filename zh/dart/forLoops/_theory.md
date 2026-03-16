`for` 循环将一段代码重复执行指定次数。基本语法为：

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**：在循环开始前执行一次（例如 `int i = 0`）

**condition**：在每次迭代前检查；当条件为假时循环停止

**update**：在每次迭代后执行（例如 `i++`）

---

可以在循环体内使用循环变量来追踪当前计数。例如，累加求和：

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

循环结束后，`total` 等于 15。

---

`for` 循环可以通过使用递减（`i--`）和 `>=` 条件来**倒序**计数：

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

这在倒计时或反向迭代时非常有用。

---

`for-in` 循环无需索引即可遍历集合中的每个元素：

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

每次迭代将下一个元素赋值给循环变量（此处为 `fruit`）。

---

`break` 语句在满足条件时立即退出循环：

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

当搜索某个值并希望找到后立即停止时，这非常有用。
