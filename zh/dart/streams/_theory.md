`Future` 表示稍后到达的**单个**值。**Stream** 表示随时间陆续到达的值的**序列**：按键、文件的分块、来自服务器的消息。每个值称为一个**事件**，在最后一个事件之后，流就**结束**了。

构建流最简单的方式是 `Stream.fromIterable`，它会把列表中的每个元素一个接一个地发出：

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

要逐个消费这些事件，你需要使用 **`await for`** 循环。和 `await` 一样，它只能出现在标记了 `async` 的函数里，所以 `main` 变成了 `Future<void> main() async`。循环体每个事件执行一次，流结束时循环也随之结束：

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

这里普通的 `for` 循环行不通：`Stream` 不是 `Iterable`，它的值不是一次性全部就绪的。

---

`Stream.fromIterable` 需要事先拿到所有的值。要一个一个地**生产**值，就写一个**异步生成器**：函数体标记为 `async*`、返回类型为 `Stream<T>` 的函数。在它内部，`yield` 向流发送一个事件：

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

调用 `countTo(3)` 时函数体并不会运行：它是惰性执行的，随着监听者索取值而逐步运行，函数体结束时流也就结束了。

要把所有事件收集到一个 `List` 中，调用 `toList()`。它返回 `Future<List<T>>`，所以你要用 `await` 等待它：

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

`await for` 循环不只能打印：它还可以更新在循环之前声明的变量。消费一个流并计算结果的函数必须标记为 `async`，并返回该结果的 `Future`：

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

函数只有在流结束之后才会到达 `return`，所以调用方在等待这个 future 时才拿到最终的值：

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

每个流最终都会结束。对 `async*` 生成器来说，只要函数体执行完毕，流就**结束**了，无论它是跑到了末尾还是遇到了 `return`。对已结束的流的 `await for` 循环会退出，任何 `toList()` 的 future 都会完成。

流不会重新开始，也不会重复它的值：一旦结束，就一直是结束状态。

---

`await for` 会暂停当前函数，直到流结束。当你想**不等待**就对事件作出反应时，调用 `listen` 并传入一个回调：它每个事件被调用一次，而 `listen` 之后的代码会立即执行。

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` 还接受一个命名参数 `onDone`，那是一个无参函数，在流结束时被调用：

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

`async*` 生成器可以用 `yield*`（yield-star）转发**另一个流的每个事件**。它就像一个把每个值都 yield 出来的 `await for` 循环，只用一行：

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

内层流结束后，外层流继续执行它自己的 `yield`。

---

和 `Iterable` 一样，`Stream` 也有从已有流构建**新流**的方法：

- `map` 转换每个事件
- `where` 只保留满足条件的事件
- `take` 在给定数量的事件之后停止

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

这些方法是**惰性的**：在有人监听结果流之前，什么都不会执行。它们可以链式调用，而且源流永远不会被修改。

---

因为 `where`、`map` 和 `take` 各自都返回一个流，你可以把它们链起来，最后用 `toList()` 把结果拿成一个列表。只有最后的 `toList()` 需要 `await`，因为它是唯一返回 `Future` 的调用：

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

除了 `toList()`，流还提供其他**消费**它全部事件并返回单个 `Future` 的方法：

- `first` 和 `last` 以第一个或最后一个事件完成
- `length` 以事件的数量完成
- `join(separator)` 以所有事件连接成的一个 `String` 完成
- `reduce(combine)` 两两合并事件，最终得到一个值

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` 会把目前的结果和下一个事件传给 `combine`。如果流是空的，它会抛出异常，所以只在保证至少有一个事件时才使用它。

---

`Stream` 的方法分为两组：

- **转换**方法，比如 `map`、`where`、`take` 和 `skip`，返回一个**新的 `Stream`**，并且是惰性的：在新流被监听之前不会处理任何事件
- **消费**方法，比如 `toList`、`reduce`、`join`、`first`、`last` 和 `length`，会监听这个流并返回带有最终结果的 **`Future`**

因此一条链看起来就是零个或多个转换调用，后面最多跟一个消费调用。

---

生成器在一个函数内部产生事件。当事件来自**别处**（一个按钮、一个网络回调、另一个对象）时，你需要一个 **`StreamController`**。它位于 `dart:async` 库中，所以文件必须以 `import 'dart:async';` 开头。

控制器拥有一个流，并让你把事件推入其中：

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` 发送一个事件
- `close()` 结束这个流；忘记它就意味着监听者会一直等下去
- `stream` 就是监听者所消费的那个 `Stream`

在任何人监听之前添加的事件会被保存在缓冲区里，所以上面的代码是安全的：稍后到来的监听者仍然会收到 `4` 和 `2`。

---

`StreamController` 常常在同一处被创建和消费：用 `listen` 订阅 `controller.stream`，然后用 `add` 添加事件，再用 `close` 关闭控制器。因为 `listen` 不会等待，事件会在当前代码结束之后才送达，但始终按照它们被添加的顺序：

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

到目前为止见到的流都是**单订阅**流：它们只允许恰好一个监听者。第二次调用 `listen`、`await for` 或任何消费方法都会抛出 `StateError`（"Stream has already been listened to"）。

要在多个监听者之间共享一个流，用 `asBroadcastStream()` 把它转换成**广播**流：

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

广播流不做缓冲：监听者只会收到它订阅**之后**发出的事件。在这个例子里，两个监听者都在第一个 `await` 之前订阅，所以两者都收到了每个事件。

---

控制器可以用命名构造函数 `StreamController<T>.broadcast()` 直接创建一个广播流。它的 `stream` 接受任意数量的监听者，每个事件都会按照它们订阅的顺序送达所有监听者：

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

和每个广播流一样，它不做缓冲：在某个监听者订阅之前添加的事件，对这个监听者来说就丢失了。

---

流除了值之外还能携带**错误**。在 `async*` 生成器内部，`throw` 会发送一个错误事件并结束这个流；`StreamController` 可以用 `addError` 发送一个错误。

在消费一侧，`await for` 循环会在循环所在的位置重新抛出这个错误，所以你用围绕循环的普通 `try`/`catch` 来处理它：

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

使用 `listen` 时，改为传入一个 `onError` 回调：`stream.listen(print, onError: (e) => print('caught: $e'));`
