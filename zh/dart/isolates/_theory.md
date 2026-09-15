你到目前为止写下的每一行 Dart 都运行在一个 **isolate** 内：一个拥有自己的内存和自己的事件循环的线程。程序从一个 isolate 开始，即 *main* isolate（主 isolate），并且可以启动更多 isolate。

isolate 的特别之处在于它们**不共享任何东西**。两个 isolate 永远不会看到同一个对象，因此没有锁、没有数据竞争，也不会有更新到一半的值。它们只通过传递消息的**副本**来互相通信。

使用第二个 isolate 的最简方式是 **`Isolate.run`**。它接收一个函数，在一个全新的 isolate 上运行它，并返回一个带有其结果的 `Future`：

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` 位于 `dart:isolate` 库中，所以文件必须以 `import 'dart:isolate';` 开头。当新 isolate 计算时，主 isolate 保持空闲：这是真正的**并行**，工作发生在另一个处理器核心上。

---

你交给 `Isolate.run` 的函数可以**捕获**它周围的变量。这些值会随函数一起被复制进新 isolate，因此计算可以依赖其调用者：

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` 返回一个 `Future`，其值就是函数的返回值，所以 `triple` 可以直接把它返回：当你只是把这个 future 传递出去时，不需要 `async` 也不需要 `await`。

把工作移到另一个 isolate 的意义在于，长时间的计算不会再冻结主 isolate。一个运行一秒钟的循环如果跑在主 isolate 上会阻塞一切；而在 `Isolate.run` 内部它跑在别处，主 isolate 得以继续处理自己的事件。

---

在 isolate 之间只有**数据**会被复制；**代码**不会。程序的每个 isolate 本来就能看到该程序所有的顶层函数和类，因此交给 `Isolate.run` 的计算可以随意调用它们：

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

传递的是进去时被捕获的 `text` 和出来时的结果 `int`，两者都是副本。这个模式始终一样：把繁重的函数留在原地，把**调用**包进 `Isolate.run`。

---

`await` 和 `Isolate.run` 解决的是两个不同的问题，值得把它们区分开。

`await` 给你的是单个 isolate 上的**并发**：当一个函数在等待定时器或服务器时，isolate 会去运行其他待执行的代码。没有任何东西在同一瞬间运行，isolate 只是不再空转。这是用于等待的正确工具。

`Isolate.run` 给你的是**并行**：第二个 isolate 在第二个处理器核心上，与第一个在同一瞬间运行自己的代码。这是用于计算的正确工具。

```dart
await Future.delayed(const Duration(seconds: 1)); // 等待：没有核心繁忙
await Isolate.run(() => hugeCalculation());       // 计算：另一个核心正忙
```

等待一个缓慢的计算毫无帮助：`await bigSum()` 仍然在当前 isolate 上运行 `bigSum`，并阻塞它直到最后一行。只有第二个 isolate 才能把那份工作移走。

---

`Isolate.run` 是获取单个结果的捷径。当你想要一个持续运行并多次汇报结果的 isolate 时，就用 **`Isolate.spawn`** 自己启动它，并给它一条应答的途径。

这条途径就是一对端口。**`ReceivePort`** 是一个邮箱：你在自己这一侧创建它，并读取到达的消息。它的 **`sendPort`** 是这个邮箱的地址，也是另一个 isolate 回复时唯一需要的东西。

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` 接收要运行的函数和传给它的单条消息，这里就是 `SendPort`。在另一侧，`send` 把一个值投进邮箱，而 `await receivePort.first` 等待第一条消息并关闭端口。

---

交给 `Isolate.spawn` 的函数被称为**入口点**。它必须是一个顶层（或静态）函数，并且恰好接收一个参数：`Isolate.spawn` 传给它的消息。

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

到达 `ReceivePort` 的消息静态类型是 `dynamic`，因为任何值都可能被发送过来。当你知道另一个 isolate 发送的是什么时，就对它进行类型转换：

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

被 spawn 的 isolate 总是遵循同样的四个步骤：打开邮箱，带着邮箱的地址 spawn 工作单元，等待答案，使用它。

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

`Isolate.spawn` 前面的 `await` 等待的是 isolate *启动*，而不是它完成工作：结果稍后通过端口到达。

---

`Isolate.spawn` 只向入口点传递**一条**消息，而工作单元通常既需要一个用来应答的 `SendPort`，又需要一些要处理的数据。常见的技巧是把所有东西打包进一个 `List`，在另一侧再把它解开：

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

列表在进入时被复制，所以工作单元读取的是它自己的那些值。`SendPort` 是少数不被复制而是被共享的东西之一：它始终指向创建它的那个 isolate 的邮箱，这正是它能被用作回信地址的原因。

---

`first` 读取一条消息并关闭邮箱。`ReceivePort` 同时也是一个 **`Stream`**，所以要读取多条消息，可以用 `await for` 对它进行循环。

循环自己永远不会结束：端口保持打开，等待一条可能永远不来的消息。因此工作单元会发送最后一个值作为信号，通常是 `null`，而监听方的反应是调用 **`close()`**，它会结束流和循环：

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

收集一整串消息遵循同一个配方：循环前准备一个空列表，每条真正的消息做一次 `add`，在结束流的信号到来时调用 `close()`。端口一旦关闭，`await for` 就会结束，函数也就可以返回了：

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

消息保持它们被发送时的顺序，所以你构建的列表一步一步地映出另一个 isolate 的工作。

---

一个打开的 `ReceivePort` 被算作未完成的工作：只要它还存在，拥有它的 isolate 就有理由继续存活，它的事件循环会一直等待消息。在命令行程序中，一个带着打开端口的主 isolate 简直**永远不会退出**，你必须手动把它停掉。

因此，关闭端口是任务的一部分，而不是一种优化：

- `await port.first` 在一条消息之后替你关闭它
- `port.close()` 显式地关闭它，这正是 `await for` 循环之后你所需要的

`Isolate.run` 完全没有这些簿记工作：它创建端口、关闭端口并替你把 isolate 关停。只要你只需要一个结果，就优先使用它。

---

在一个 isolate 内部抛出的异常无法跳到另一个 isolate：两者的调用栈是分开的。`Isolate.run` 替你弥合了这个鸿沟：它捕获错误，把错误复制回来，并让返回的 future 以该错误失败。因此在你这一侧，它就是一个普通的异步错误，在 `await` 周围用 `try`/`catch` 捕获：

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

`try` 里的 `await` 很重要，与任何其他 future 完全一样：没有它，future 会在 `try` 块尚未结束时离开，`catch` 就永远不会运行。

`Isolate.spawn` 没有这样的桥梁。一个未捕获的错误会悄悄杀死被 spawn 的 isolate，而父 isolate 会继续等待一条永远不会到来的消息，这是优先选用 `Isolate.run` 的又一个理由。

---

从 `Isolate.run` 返回的错误是在另一侧抛出的那个错误的**副本**，所以常用的检查仍然有效：`catch (e)` 给你错误对象，`e is FormatException` 告诉你它是哪一种失败。

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

你不能指望的是指向你自己 isolate 的堆栈跟踪：错误旅行了，堆栈没有。

---

组合起来，一个 `Isolate.run` 程序读起来就像普通的顺序代码：调用之前的那一行在主 isolate 上运行，计算在别处运行，而 `await` 之后的那一行带着结果回到主 isolate 上运行。

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

因为 isolate 之间不共享内存，每条消息在跨越时都会被**复制**。数字、布尔值、字符串、`null`、列表、映射和大多数普通对象都能完成这趟旅行；少数东西完全无法被复制，比如一个打开的 socket，尝试发送它会抛出 `ArgumentError`。

由此得出的就是让 isolate 安全的那条规则：发送之后，两侧持有的是**两个独立的对象**。一个 isolate 对它的副本做的任何事情，对另一个 isolate 都是不可见的。

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // 副本会增长
print(numbers);                           // [1, 2, 3]
```

`SendPort` 是这条规则的例外：它是被共享的而不是被复制的，恰恰是为了让它仍然能够指向原来的邮箱。

---

每个 `Isolate.run` 都会启动自己的 isolate，所以多个 `Isolate.run` 确实会在同一瞬间运行，占用机器拥有的多个核心。这个模式你在 futures 里已经见过：先启动每一个计算，然后用 `Future.wait` 等待它们全部完成，它按输入的顺序保存结果。

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

启动一个 isolate 并不是免费的：它要花费内存和几毫秒。把一个漫长的计算拆分到少数几个 isolate 上是值得的；把一千个微不足道的加法发送给一千个 isolate 则不值得。
