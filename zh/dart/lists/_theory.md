在 Dart 中，**列表**是一种有序的元素集合。创建列表最简单的方式是使用 `[]` 字面量语法：

```dart
List<int> numbers = [1, 2, 3];
```

也可以使用 `var` 进行类型推断：

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

类型注解 `List<String>` 告诉 Dart 列表中的每个元素都必须是 `String` 类型。

---

Dart 中的列表是**从零开始索引**的，即第一个元素在索引 `0` 处，第二个在索引 `1` 处，依此类推。

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

通过索引访问元素使用 `list[index]` 语法。

---

`.add()` 方法将单个元素追加到列表的**末尾**：

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

注意，`.add()` **就地**修改列表，返回值为 `void`。

---

`.length` 属性返回列表中的元素个数：

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

空列表的长度为 `0`：

```dart
var empty = [];
print(empty.length); // 0
```

---

`.contains()` 方法检查列表是否包含给定的值。如果找到则返回 `true`，否则返回 `false`：

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

这对于不使用循环进行成员检查非常有用。
