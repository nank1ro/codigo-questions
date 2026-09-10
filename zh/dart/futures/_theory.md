有些操作需要时间：读取文件、调用服务器、等待定时器。Dart 不会在它们运行时阻塞程序。相反，这类函数会返回一个 **`Future<T>`**：一个承诺，表示类型为 `T` 的值将在**稍后**可用。

最简单的 future 是已经拥有其值的那种，用 `Future.value` 构建：

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

要从 future 中取出值，你需要 **`await`** 它。`await` 会暂停当前函数，直到 future 完成，然后把普通的值交给你。它只能用在标记了 **`async`** 的函数里，所以 `main` 变成 `Future<void> main() async`：

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

没有 `await` 时，`n` 就是 `Future` 本身，`print(n)` 会显示 `Instance of 'Future<int>'` 而不是那个数字。

---

把函数标记为 `async` 会做两件事：允许在函数体里使用 `await`，并让函数**返回一个 `Future`**。你用 `return` 返回的东西会成为该 future 完成时的值，所以即使函数体返回的是普通的 `T`，声明的返回类型也是 `Future<T>`：

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

这里不需要 `Future.value`：`async` 关键字会替你把返回值包装起来。

---

`Future.value` 会立即完成。要模拟耗时的工作，请使用 **`Future.delayed`**：它接收一个 `Duration` 和一个函数，等待这段时间，然后以该函数的返回值完成：

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` 用 `seconds`、`milliseconds` 或 `minutes` 这样的命名参数构建。在 `async` 函数里，你也可以单独等待一个延迟，不带值，只为暂停：

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

两种写法都很常见；第二种读起来像普通的顺序代码。

---

把 future 的两个方向记清楚：

- `async` 函数**声明** `Future<T>` 而**返回**普通的 `T`：包装是自动的
- 对 `Future<T>` 使用 `await` 的调用方**收到**普通的 `T`：拆包是自动的

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

写成 `int count() async` 是错误的：`async` 函数必须声明 `Future`（或 `void`）返回类型。

---

`await` 并不是使用 future 的唯一方式。你也可以用 **`then`** 注册一个**回调**：future 完成后，你传入的函数会带着这个值被调用。与 `await` 不同，`then` **不会**暂停当前函数，所以它后面的代码会先运行：

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

即使是用 `Future.value` 构建的 future，也要等当前代码执行完才交付它的值，这就是 `waiting` 先被打印的原因。`then` 在任何函数里都能用，无论是不是 `async`。

---

在 `async` 函数里，`await` 让你可以像写普通顺序代码一样写异步步骤。每个 `await` 都会等待它的 future，只有值到位后，下一行才会运行：

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` 也可以直接用在表达式里：`return await width() * await height();` 得到同样的结果。

---

当函数遇到 `await` 时，它会在那一行**暂停**，程序的其余部分继续运行。`await` 之后的行只有在 future 完成后才会运行。因此，从上到下读一个 `async` 函数，就能知道它各个效果的确切顺序：

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

future 也可以以**错误**完成。当 `async` 函数抛出异常时，异常不会立刻逃逸出去：它会成为所返回 future 的错误。对该 future 使用 `await` 的一方会在 `await` 处看到这个错误被抛出，因此可以用普通的 `try`/`catch` 处理：

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

`try` 里面的 `await` 至关重要：`return parseLater(s);` 会把 future **不加等待地**交给调用方，于是错误会在 `try` 块已经结束之后才到达，`catch` 永远不会执行。

---

错误随 future 传递，而不是沿调用栈传递。调用一个会抛出异常的 `async` 函数本身绝不会让调用方崩溃：错误被存放在返回的 future 里，稍后在 await 这个 future 的地方才出现。因此 `try`/`catch` 必须包住 **`await`**，而不是创建 future 的那次调用。

如果始终没有人 await 或处理这个失败的 future，Dart 会报告 *unhandled exception*，在命令行程序中还会以错误退出。

---

使用回调时，错误由 **`catchError`** 处理，它是 `then` 的对应物。两者都返回一个新的 future，所以通常链式调用：future 成功时 `then` 收到值，失败时 `catchError` 收到错误，两个回调只会有一个运行：

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

放在 `then` 之后的 `catchError` 也会捕获 `then` 回调里抛出的错误。和 `then` 一样，链之后的代码会先运行，因为回调只有在当前代码执行完后才被调用。

---

当多个 future 彼此不依赖时，把它们全部交给 **`Future.wait`**：它接收一个 `List<Future<T>>`，让它们同时运行，并返回单个 `Future<List<T>>`，在**全部**完成时结束。结果保持输入列表的顺序，与哪个 future 先完成无关：

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` 需要 `25` 毫秒，因为 `fast()` 只有在 `slow()` 完成后才被调用；`await Future.wait([slow(), fast()])` 大约需要 `20` 毫秒，也就是最长那个的时长。

---

`Future.wait` 是“加载多样东西，然后继续”的工具。典型写法是：构建 future 列表，对它 `await Future.wait`，然后使用得到的列表：

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` 先完成，但列表仍然按照调用顺序排列：`stock()` 在前，`orders()` 在后。

---

让两个 future 同时运行并不一定需要 `Future.wait`。`async` 函数在被**调用**时就开始运行，直到它的第一个 `await`；你拿回的 future 就是已经在进行中的工作。所以诀窍是：**先调用，后 await**：

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

对比 `return await words() / await pages();`，其中 `pages()` 只有在 `words()` 完成后才被调用：结果相同，时间翻倍。只要第二次调用不需要第一次的结果，就优先使用并发写法。

---

错误会**传播**到每一个没有捕获它的 `await`。如果 `load()` 失败，`loadTwice()` 里的 `await load()` 就会抛出；由于 `loadTwice` 没有 `try`/`catch`，它自己的 future 也以同样的错误失败；就这样沿着调用链一路向上，直到某个 `await` 被 `try`/`catch` 包住：

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

这与异常在同步调用中传播的方式一致：你只在知道该怎么办的那一层处理一次。

---

`Future.wait` 遵循同样的规则：如果**任何一个** future 失败，合并后的 future 就以该错误完成，`await Future.wait(...)` 会抛出异常。你永远拿不到只包含成功值的部分列表。要保留其他结果，就在把每个 future 传给 `Future.wait` 之前，在它内部处理错误，例如用 `catchError`。

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

因为 `await` 把 future 的错误变成了普通异常，所有常见的 `try`/`catch` 写法都适用于异步代码，包括重试循环。在 `catch` 块里，**`rethrow`** 会再次抛出同一个错误，这就是在最后一次尝试之后放弃的方式：

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

像 `Future<String> Function() task` 这样的函数类型参数接收的是**函数**本身，而不是一个 future：每次调用 `task()` 都会开始一次新的尝试。
