**集合**（`Set`）是由**唯一**值组成的集合：同一个值最多只能出现一次。和 map 一样，集合使用 `{}` 字面量语法创建，但它包含的是普通值而不是 `key: value` 对：

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

类型注解 `Set<int>` 告诉 Dart 每个元素都是 `int` 类型。和列表、map 一样，`var` 会根据字面量推断类型：

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

集合永远不会存储同一个值两次。如果字面量中有重复项，只会保留第一次出现的值，其余的会在运行时被丢弃，且不会报错（分析器会对重复值的字面量发出警告）：

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

`.length` 属性返回集合中**唯一**元素的数量：

```dart
print(letters.length); // 3
```

---

`.add(value)` 方法插入单个值。如果该值被添加则返回 `true`，如果它已经在集合中则返回 `false`，此时不会发生任何变化。`.addAll(iterable)` 方法插入列表或另一个集合中的所有元素，同样会跳过已存在的元素：

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

空的 `{}` 字面量是一个 **map**，而不是集合。要创建一个空集合，需要为它指定类型：

```dart
var empty = <String>{};
Set<int> other = {};
```

---

`.remove(value)` 方法从集合中删除一个值。如果该值存在则返回 `true`，否则返回 `false`：

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

要一次删除所有元素，使用 `.clear()`。

---

要检查某个值是否在集合中，使用返回 `bool` 的 `.contains(value)`。当集合没有元素时 `.isEmpty` 为 `true`，当集合至少有一个元素时 `.isNotEmpty` 为 `true`：

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Dart 中默认的集合会记住**插入顺序**：当你打印或遍历它时，元素会按照它们首次被添加的顺序出现。添加一个已经存在的值不会改变它的位置：

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

集合是一个 `Iterable`，所以你可以像列表一样直接用 `for-in` 遍历它的元素。它没有索引：元素会按插入顺序被访问：

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
