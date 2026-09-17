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

---

有些字符不能直接输入到引号内。**转义序列**以反斜杠开头：`\n` 表示换行，`\t` 表示制表符，`\\` 表示反斜杠，`\$` 表示字面的美元符号（否则 `$` 会触发插值）：

```dart
print('one\ntwo');   // 在两行中分别打印 one 和 two
print('Cost: \$5');  // Cost: $5
```

**原始字符串（raw string）**以 `r` 为前缀：在它内部，反斜杠和 `$` 都是普通字符，不会被转义或插值：

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

对于跨多行的文本，可以使用由三重引号 `'''` 或 `"""` 界定的**多行字符串**：其中的换行会被保留。

```dart
var poem = '''
roses are red
violets are blue''';
```

---

在底层，字符串的每个字符都以数字形式存储，即它的**代码单元（code unit）**（一个 UTF-16 编码）。`.codeUnitAt(index)` 返回某个字符的编码，`.codeUnits` 返回整个编码列表。`String.fromCharCode(code)` 则相反，根据编码构建字符串：

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

连续的字母有连续的编码：`'A'` 是 65，`'B'` 是 66，以此类推。

---

当两个字符串包含完全相同、顺序也相同的字符时，用 `==` 比较它们会相等。这种比较是**区分大小写**的，并且会计入每一个空格：

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

如果要忽略大小写进行比较，先转换两边：`a.toLowerCase() == b.toLowerCase()`。对于排序，`.compareTo(other)` 会根据该字符串在另一个字符串之前、相等还是之后，返回一个负数、`0` 或一个正数。

---

由于字符串是不可变的，在循环中用 `+=` 拼接长文本会在每一步都创建一个新字符串。**StringBuffer** 可以高效地收集文本片段，只有在你需要时才生成最终的字符串：

- `.write(value)` 追加一个值（任何类型都会被转换为文本）
- `.writeln(value)` 追加该值，并在其后加上换行符
- `.toString()` 返回目前为止构建出的字符串

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

字符串方法会返回字符串，因此可以一个接一个地**链式调用**。结合 `.split('')`、列表的 `.reversed` 属性和 `.join()`，可以在一个表达式中反转字符串：

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

**回文（palindrome）**是指正着读和倒着读都一样的文本，例如 `level`。
