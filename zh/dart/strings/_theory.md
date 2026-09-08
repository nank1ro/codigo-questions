**字符串（String）**是一段文本：一串用引号包裹的字符。在 Dart 中，你可以使用单引号 `'...'` 或双引号 `"..."`，它们的作用完全相同：

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

选择一种引号后，可以在文本内部不加转义地使用另一种引号：

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

如果需要在文本内部使用相同的引号，用反斜杠对其进行转义：`'It\'s sunny'`。

---

两个字符串可以用 `+` 运算符连接成一个新的字符串，这称为**拼接（concatenation）**：

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart 还会将写在一起、不带任何运算符的两个字符串**字面量**自动连接起来。这在把一段长文本拆成多行书写时很方便：

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

只有字符串才能用 `+` 拼接：`'Age: ' + 30` 会编译报错，因为 `30` 是 `int` 类型。

---

除了拼接，你还可以用**插值（interpolation）**直接把值插入字符串。写 `$name` 可以插入变量的值，写 `${expression}` 可以插入任意表达式的结果：

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

插值适用于任何类型：数字、布尔值和列表都会自动转换为文本，所以即使 `age` 是 `int` 类型，`'Age: $age'` 也是有效的。

---

每个字符串都能通过它的 `.length` 属性知道自己包含多少个字符。空格和标点符号也算作字符：

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

你可以用方括号加上**索引**来读取单个字符，索引从 `0` 开始。结果是一个单字符的 `String`：

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

读取超出字符串范围的索引（比如 `word[5]`）会抛出错误。

---

Dart 中的字符串是**不可变的**：字符串一旦创建就永远不会改变。像 `.toUpperCase()` 和 `.toLowerCase()` 这样的方法不会修改原字符串，而是**返回一个新的字符串**：

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

如果你希望变量保存新的值，需要把结果重新赋值给它：`word = word.toUpperCase();`。

---

用户输入的文本周围经常带有多余的空格。`.trim()` 方法返回一个去掉首尾空白字符（空格、制表符和换行符）的字符串副本。`.trimLeft()` 和 `.trimRight()` 只去除某一侧的空白：

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

`.substring(start, end)` 方法返回字符串从索引 `start` 开始到索引 `end`（**不包含**）为止的部分。如果省略 `end`，则返回从 `start` 到字符串末尾的全部内容：

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

有几个方法可以在字符串内部进行查找：

- `.contains(other)` 如果 `other` 出现在字符串中的任意位置，返回 `true`
- `.startsWith(other)` 和 `.endsWith(other)` 分别检查开头和结尾
- `.indexOf(other)` 返回第一次出现的索引，如果找不到则返回 `-1`

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

它们都区分大小写：`'Dart'.contains('dart')` 的结果是 `false`。

---

`.replaceAll(from, to)` 方法返回一个新字符串，其中**每一处** `from` 都被替换为 `to`。`.replaceFirst(from, to)` 只替换第一处：

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

`.split(separator)` 方法在每次出现分隔符的地方把字符串切分成 `List<String>`。与之相反的是 `.join(separator)`，这是列表的一个方法，把元素粘合成一个字符串：

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

用空字符串调用 `.split('')` 会得到一个包含每个单独字符的列表。
