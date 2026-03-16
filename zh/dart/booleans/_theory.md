__布尔值__是一种数据类型，只能保存两个值之一：`true` 或 `false`。
在 Dart 中，布尔类型使用关键字 `bool` 声明。

```dart
bool isRaining = true;
```

变量 `isRaining` 存储值 `true`，表示当前正在下雨。
布尔值始终以小写形式书写：`true` 和 `false`。

---

就像任何其他变量一样，你可以使用 `print()` 打印布尔值。
当你打印布尔值时，Dart 输出文本 `true` 或 `false`。

```dart
bool isSunny = true;
print(isSunny); // true
```

---

布尔变量也可以保存值 `false`。
当某个事情不是事实时，使用 `false`。

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

就像 `true` 一样，`false` 也必须以小写形式书写。

---

__否定运算符__ `!`（也称为"not"或"非"）翻转布尔值。
将 `!` 应用于 `true` 得到 `false`，将 `!` 应用于 `false` 得到 `true`。

```dart
bool isActive = true;
print(!isActive); // false
```

当你想检查条件的相反情况时，这很有用。

---

布尔值在整个编程中用于表示条件和做出决策。
每当你的程序需要在两种可能性之间做出选择时，就涉及布尔值。

例子：
- 用户是否登录？（`isLoggedIn`）
- 门是否打开？（`isDoorOpen`）
- 订单是否已发货？（`isShipped`）
