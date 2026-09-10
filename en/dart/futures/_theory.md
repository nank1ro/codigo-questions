Some operations take time: reading a file, calling a server, waiting for a timer. Dart does not block the program while they run. Instead, such a function returns a **`Future<T>`**: a promise that a value of type `T` will be available **later**.

The simplest future is one that already has its value, built with `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

To get the value out of a future you **`await`** it. `await` pauses the current function until the future completes, then gives you the plain value. It is only allowed inside a function marked **`async`**, so `main` becomes `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Without `await`, `n` would be the `Future` itself, and `print(n)` would show `Instance of 'Future<int>'` instead of the number.

---

Marking a function `async` does two things: it allows `await` inside the body, and it makes the function **return a `Future`**. Whatever you `return` becomes the value the future completes with, so the declared return type is `Future<T>` even though the body returns a plain `T`:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

You do not need `Future.value` here: the `async` keyword wraps the returned value for you.

---

`Future.value` completes right away. To simulate work that takes time, use **`Future.delayed`**: it takes a `Duration` and a function, waits for the duration, then completes with what the function returns:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` is built with named parameters such as `seconds`, `milliseconds` or `minutes`. Inside an `async` function you can also await a delay on its own, with no value, just to pause:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Both styles are common; the second reads like ordinary sequential code.

---

Keep the two sides of a future clear in your head:

- an `async` function **declares** `Future<T>` and **returns** a plain `T`: the wrapping is automatic
- a caller that `await`s a `Future<T>` **receives** a plain `T`: the unwrapping is automatic

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Writing `int count() async` is an error: an `async` function must declare a `Future` (or `void`) return type.

---

`await` is not the only way to use a future. You can also register a **callback** with **`then`**: the function you pass is called with the value once the future completes. Unlike `await`, `then` does **not** pause the current function, so the code after it runs first:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Even a future built with `Future.value` delivers its value only after the current code has finished, which is why `waiting` is printed first. `then` works in any function, `async` or not.

---

Inside an `async` function, `await` lets you write asynchronous steps as if they were ordinary sequential code. Each `await` waits for its future, and the next line only runs once the value is there:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` can also be used directly inside an expression: `return await width() * await height();` gives the same result.

---

When a function hits an `await`, it **pauses** at that line and the rest of the program continues. The lines after the `await` run only once the future completes. Reading an `async` function top to bottom therefore tells you the exact order of its effects:

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

A future can also complete with an **error**. When an `async` function throws, the exception does not escape immediately: it becomes the error of the returned future. Whoever `await`s that future sees the error thrown at the `await`, so it can be handled with an ordinary `try`/`catch`:

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

The `await` inside the `try` is essential: `return parseLater(s);` would hand the future to the caller **without waiting**, so the error would arrive after the `try` block is already over and the `catch` would never run.

---

Errors travel with the future, not through the call stack. Calling an `async` function that throws never crashes the caller by itself: the error is stored in the returned future and shows up later, at the point where the future is awaited. A `try`/`catch` therefore has to wrap the **`await`**, not the call that created the future.

If nobody ever awaits or handles the failed future, Dart reports an *unhandled exception* and, in a command-line program, exits with an error.

---

With callbacks, errors are handled by **`catchError`**, the counterpart of `then`. Both return a new future, so they are usually chained: `then` receives the value if the future succeeds, `catchError` receives the error if it fails, and only one of the two callbacks runs:

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

`catchError` placed after `then` also catches errors thrown inside the `then` callback. As with `then`, the code after the chain runs first, because callbacks are only invoked once the current code has finished.

---

When several futures do not depend on each other, hand them all to **`Future.wait`**: it takes a `List<Future<T>>`, lets them run at the same time, and returns a single `Future<List<T>>` that completes when **all** of them are done. The results keep the order of the input list, regardless of which future finished first:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` takes `25` milliseconds, because `fast()` is only called once `slow()` has completed; `await Future.wait([slow(), fast()])` takes about `20`, the duration of the longest one.

---

`Future.wait` is the tool for "load several things, then continue". The typical shape is: build the list of futures, `await Future.wait` on it, then use the resulting list:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` completes first, but the list still follows the order of the calls: `stock()` first, `orders()` second.

---

You do not need `Future.wait` to run two futures at the same time. An `async` function starts running as soon as it is **called**, up to its first `await`; the future you get back is the work already in progress. So the trick is to **call first, await later**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Compare with `return await words() / await pages();`, where `pages()` is only called after `words()` has completed: same result, twice the time. Prefer the concurrent form whenever the second call does not need the result of the first.

---

An error **propagates** through every `await` that does not catch it. If `load()` fails, `await load()` inside `loadTwice()` throws; since `loadTwice` has no `try`/`catch`, its own future fails with the same error; and so on up the chain, until some `await` is wrapped in a `try`/`catch`:

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

This mirrors how exceptions propagate through synchronous calls: you handle them once, at the level that knows what to do.

---

`Future.wait` follows the same rule: if **any** of the futures fails, the combined future completes with that error and `await Future.wait(...)` throws. You never get a partial list of the successful values. To keep the others, handle the error inside each individual future, for example with `catchError`, before passing it to `Future.wait`.

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

Because `await` turns future errors into ordinary exceptions, all the usual `try`/`catch` patterns apply to asynchronous code, including loops that retry. Inside a `catch` block, **`rethrow`** throws the same error again, which is how you give up after the last attempt:

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

A function-typed parameter such as `Future<String> Function() task` receives the **function** itself, not a future: each `task()` call starts a fresh attempt.
