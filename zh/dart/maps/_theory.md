**Map**（映射）是一种由**键值对**组成的集合：每个值都存储在一个唯一的键下，你可以用键再次找到对应的值。创建 map 使用 `{}` 字面量语法，每一对写作 `key: value`：

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

类型注解 `Map<String, int>` 告诉 Dart 每个键都是 `String` 类型，每个值都是 `int` 类型。和列表一样，`var` 会根据字面量推断类型：

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

读取值时，你在方括号中使用键，就像列表中的索引一样：

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

如果键不在 map 中，查找**不会**抛出错误：它会返回 `null`。因此 `ages['Ann']` 的类型是 `int?`（可为空的 `int`），而不是 `int`：

```dart
print(ages['Zed']); // null
```

---

使用 `map[key] = value` 赋值：如果键还不在 map 中，就**添加**一个新的键值对；如果键已存在，就**更新**该键对应的值：

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // 添加 Bob
ages['Ann'] = 31; // 更新 Ann
print(ages); // {Ann: 31, Bob: 25}
```

新的键会添加在已有键之后，所以 map 会记住插入顺序。

---

`.remove(key)` 方法从 map 中删除一个键及其值。它返回被删除的值，如果键不存在则返回 `null`：

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

`.length` 属性返回键值对的数量：

```dart
print(ages.length); // 1
```

---

要检查 map 是否包含某个键，使用 `.containsKey(key)`。要检查是否有键值对存储了某个值，使用 `.containsValue(value)`。两者都返回 `bool`：

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

读取不存在的键永远不会抛出异常，所以要始终考虑查找可能得到 `null`。一种安全的做法是用 `??` 运算符提供一个回退值：

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

`.keys` 属性返回 map 的所有键，`.values` 返回所有值，均按插入顺序排列。它们都是惰性的 `Iterable`，所以需要真正的 `List` 时要调用 `.toList()`：

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```

---

空的 map 字面量 `{}` 没有可供推断类型的键值对，所以要用 `<K, V>{}` 或类型注解显式指定类型：

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

当 map 没有任何键值对时，`.isEmpty` 属性为 `true`；当它至少有一对时，`.isNotEmpty` 为 `true`：

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

`.forEach()` 方法会对每一对键值对执行一次函数。该函数接收两个参数：键和值：

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

map 不是 `Iterable`，所以不能直接用 `for-in` 遍历它。你需要遍历 `.entries`：每个元素都是一个 `MapEntry`，拥有 `.key` 和 `.value`：

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

`.putIfAbsent(key, ifAbsent)` 方法**仅当**键还不在 map 中时才添加一对键值对。第二个参数是一个生成值的函数。如果键已经存在，map 保持不变。两种情况下都会返回该键当前存储的值：

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Ann 已经存在，没有变化
ages.putIfAbsent('Bob', () => 25); // Bob 被添加
print(ages); // {Ann: 30, Bob: 25}
```

---

`.update(key, update)` 方法会替换已有键的值。第二个参数是一个函数，它接收当前值并返回新值。如果键不存在，`.update()` 会抛出错误，除非你传入一个生成初始值的 `ifAbsent` 函数：

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // apple 变为 4
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwi 以 1 被添加
print(stock); // {apple: 4, kiwi: 1}
```
