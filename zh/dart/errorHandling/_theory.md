有些语句无法执行：读取不是数字的文本、访问超出列表末尾的元素、请求空列表的第一个元素。发生这种情况时，Dart 会**抛出（throw）**一个描述失败的对象。

你可以用 `throw` 关键字自己抛出一个。`Exception('message')` 会构建一个携带简短说明的现成对象：

```dart
throw Exception('no fuel');
```

抛出不是 `return`。它会放弃当前语句、当前函数以及上层的所有调用者，去寻找能处理它的东西。当没有任何东西处理它时，程序就会停止并打印失败信息：

```
Unhandled exception:
Exception: no fuel
```

抛出之后的所有代码都会被跳过，原本会执行的行再也不会运行。这就是本主题要讲的内容：决定在哪里处理失败，而不是让它结束程序。

---

要让程序继续存活，可以把有风险的语句包进 `try` 块，并在 `catch` 块中描述恢复动作：

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

当文本不能表示一个整数时，`int.parse` 会抛出异常。Dart 在第一条抛出异常的语句处离开 `try` 块，跳过其余部分，运行 `catch` 块，然后继续执行后面的代码。括号里的变量，这里是 `e`，就是被抛出的对象本身。

`try` 块里已经完成的事情不会被撤销，所以 `try` 块要保持与预期失败的范围一样小。

---

不带限定的 `catch` 会捕获一切，这也会把你没有预料到的失败隐藏起来。要只处理某一种类型，可以在 `on` 子句中写出它的类型：

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

当文本不是一个整数时，`int.parse` 抛出的是 **`FormatException`**，所以读取输入时应该指定这个类型。`on` 子句只匹配该类型及其子类型，其他任何失败都会继续向外传播并且仍然会显现出来，而不会被一个本不为它准备的恢复动作吞掉。

---

一个 `try` 块后面可以跟**多个**子句，每个子句从不同的失败中恢复。Dart 会把抛出的对象从上到下依次与它们比较，并运行**第一个**匹配的子句：

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

用一个不存在的下标读取列表会抛出 **`RangeError`**，所以这一行代码的两种失败会得到不同的答案。

因为第一个匹配的子句获胜，所以顺序很重要：一个宽泛类型的子句如果放在更具体的子句上面，就总是会获胜，使具体的子句永远无法到达。先写具体的子句，如果想要一个安全网，就把不带限定的 `catch` 放在最后。

上面的 `on RangeError` 子句在这里只是为了演示多个子句如何排序。`RangeError` 表示的是代码本身的错误，而不是程序无法控制的状况，后面的一个练习会解释为什么这种失败应该被预防而不是被捕获。

---

通常恢复动作根本不需要被抛出的对象：类型本身已经说明了一切。这时可以去掉 `catch` 部分，只保留 `on` 子句：

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

两种形式的区别只在于是否得到一个变量：

- `on FormatException catch (e)` — 匹配该类型，并把对象作为 `e` 交给你
- `on FormatException` — 匹配该类型，没有变量
- `catch (e)` — 匹配一切，并把对象交给你

省略用不到的变量，能让处理程序诚实地反映它实际使用的东西。

---

处理程序后面还可以跟第三个块。`finally` 在**任何情况下**都会运行：`try` 块正常结束之后、某个处理程序恢复之后，以及没有任何子句匹配、失败仍在向外传播时。

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

它甚至会在 `return` 把值交回给调用者之前运行，这就是为什么上面的消息会在调用者看到结果之前被打印。这使 `finally` 成为放置无论哪种结果都必须执行的工作的地方，比如关闭你打开的东西。

---

你自己的代码用和库一样的方式抛出异常。`Exception('message')` 构建一个携带简短说明的普通异常，`throw` 把它发送出去：

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

消息不会丢失：`toString()` 把单词 `Exception`、一个冒号和消息拼在一起，这正是未处理异常报告所打印的内容。

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

抛出异常胜过返回一个编造的值（比如 `-1`）：调用者不可能忘记查看它，而且原因会随之一起传递。

---

有时处理程序并不是恢复的合适位置：你只想*留意*这次失败，然后让它继续传给真正能处理它的调用者。`rethrow` 关键字做的就是这件事，用在 `catch` 或 `on ... catch` 块中：

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` 把**同一个**对象继续向外发送，所以调用者看到的是最初的失败。改成写 `throw e` 也能工作，但它会重新开始这段旅程，丢失失败最初发生的位置。

同一条语句中的 `finally` 块仍然会运行，即使是在失败向外传播的路径上。

---

`catch` 子句可以接受**第二个**参数：

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

第一个是抛出的对象，第二个是 `StackTrace`：抛出那一刻正在运行的调用链。它回答的是失败*来自哪里*，而这仅凭消息通常无法得知。

堆栈跟踪会列出文件名、行号和调用帧，并且它随着构建方式和调用路径而变化。打印它、把它附到报告里、把它传递下去——但绝不要把它和固定的文本做比较，也绝不要把程序行为建立在它的内容之上。只有当你打算把它记录到日志时才去请求它。

---

`Exception` 是一个接口，所以你自己的类也可以实现它。自定义异常给失败起了一个 `on` 子句可以选择的名字，还带有处理程序可以读取的字段：

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

有三个部分值得保留：`implements Exception` 让这个类归入其他失败之列，一个携带详细信息的 `final` 字段，以及一个覆盖的 `toString()` 让未处理异常报告可读。没有这个覆盖，Dart 只会打印光秃秃的类名，详细信息就丢失了。

---

Dart 抛出的对象分为两族，它们的含义截然相反。

**`Exception`** 描述的是程序无法控制的状况：不是数字的文本、不存在的文件、毫无回应的网络。`FormatException` 就是其中之一。这些是预期之中的失败，捕获它们才是正常的应对。

**`Error`** 描述的是代码本身的错误：

- `ArgumentError` — 函数被调用时传入了它声明为无效的值
- `StateError` — 对象在无法完成所请求操作的时刻被使用了
- `RangeError` — 下标或值超出了允许的范围

捕获一个 `Error` 会把 bug 藏起来而不是修好它。正确的做法是修改代码，让它不再被抛出：在调用之前检查参数，或者改用不会抛出的 API。这就是为什么 `on FormatException` 子句是好实践，而 `on ArgumentError` 子句几乎从来都不是。

---

有些库会提供一个完全不抛出异常的版本。在 `int.parse` 旁边，Dart 还有 **`int.tryParse`**：同样的转换，但当文本不是数字时，它返回 `null` 而不是抛出异常。

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

结果是 `int?`，所以 `??` 运算符可以把它直接变成一个默认值：

```dart
final port = int.tryParse(text) ?? 8080;
```

当失败是寻常的事、而你只想要一个后备值时，这比 `try` 块更短也更清晰。把 `int.parse` 留给那些错误文本确实是失败、必须让上层某个人听到的情况。

---

`firstWhere` 返回第一个通过测试的元素。当没有元素通过时，它没有元素可返回，于是抛出一个 `StateError`：

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

就像 `int.tryParse` 一样，库也提供了一条出路。命名参数 `orElse` 接受一个函数，在没有匹配时由它产生要使用的值：

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

选择和之前是同一个：当"没有匹配"是寻常结果时用 `orElse`，当它意味着数据已损坏、必须让某个人听到时用不带 `orElse` 的调用。

---

`throw` 和 `try` 不必待在同一个函数里。无法完成自己工作的函数抛出异常，而知道如何处理的调用者捕获它：

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

对于一个坏的年龄应该结束程序、显示消息还是被跳过，`ageFromText` 没有自己的看法——那是调用者的决定，`try` 块就该属于调用者。这种分工正是抛出比返回 `-1` 更有价值的原因：失败会到达唯一能应对它的地方。

记住 `try` 块会在第一个失败处停下，所以失败调用之后的语句也会被跳过。

---

`try` 块放在哪里，决定了一次失败会毁掉多少工作。放在循环外面，第一个坏元素会结束整批处理；放在循环**里面**，只有那个元素被丢弃，其余的仍然会被处理：

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

这是导入文件、读取一组设置或处理一批消息时最常见的形状：一行坏数据不应该把好数据也一起扔掉。规则和之前一样——把 `try` 块保持在可能失败的语句周围，不要再大。

---

最后一块拼图是故意抛出一个 `Error`。一个声明了自己接受什么的函数，应该大声拒绝其他任何东西，而 `ArgumentError` 就是为此准备的对象：

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

消息可以通过 `e.message` 访问到，`toString()` 会打印 `Invalid argument(s): ` 加上它。

这与之前的规则并不矛盾。抛出一个 `ArgumentError` 是对的，捕获一个则不是：它是在告诉*调用者*的作者这次调用本身就是错的，正确的修复是在调用之前做检查，而不是在调用外面套一个处理程序。
