A `Future` represents a **single** value that arrives later. A **Stream** represents a **sequence** of values that arrive over time: key presses, chunks of a file, messages from a server. Each value is called an **event**, and after the last event the stream is **done**.

The simplest way to build a stream is `Stream.fromIterable`, which emits every element of a list, one after the other:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

To consume the events one by one you use an **`await for`** loop. Like `await`, it is only allowed inside a function marked `async`, so `main` becomes `Future<void> main() async`. The loop body runs once per event and the loop ends when the stream is done:

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

A plain `for` loop does not work here: a `Stream` is not an `Iterable`, its values are not available all at once.

---

`Stream.fromIterable` needs all the values up front. To **produce** values one at a time, write an **asynchronous generator**: a function whose body is marked `async*` and whose return type is `Stream<T>`. Inside it, `yield` sends one event to the stream:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

The body does not run when you call `countTo(3)`: it runs lazily, as the listener asks for values, and the stream is done when the body finishes.

To collect every event into a `List`, call `toList()`. It returns a `Future<List<T>>`, so you `await` it:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

An `await for` loop can do more than print: it can update a variable declared before the loop. A function that consumes a stream and computes a result must be marked `async`, and it returns a `Future` of that result:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

The function only reaches `return` after the stream is done, so the caller gets the final value when it awaits the future:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Every stream eventually ends. For an `async*` generator, the stream is **done** as soon as the function body finishes, whether it reached the end or hit a `return`. An `await for` loop over a done stream exits, and any `toList()` future completes.

A stream does not restart or repeat its values: once it is done, it stays done.

---

`await for` pauses the current function until the stream is done. When you want to react to events **without waiting**, call `listen` and pass a callback: it is invoked once per event, and the code after `listen` runs right away.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` also accepts an `onDone` named parameter, a function with no arguments called when the stream ends:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

An `async*` generator can forward **every event of another stream** with `yield*` (yield-star). It is like an `await for` loop that yields each value, in one line:

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

The outer stream continues with its own `yield`s once the inner stream is done.

---

Like `Iterable`, a `Stream` has methods that build a **new stream** from an existing one:

- `map` transforms each event
- `where` keeps only the events that satisfy a condition
- `take` stops after a given number of events

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

These methods are **lazy**: nothing runs until someone listens to the resulting stream. They can be chained, and the source stream is never modified.

---

Because `where`, `map` and `take` each return a stream, you can chain them and finish with `toList()` to get the result as a list. Only the final `toList()` needs an `await`, since it is the only call that returns a `Future`:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Besides `toList()`, a stream offers other methods that **consume** all its events and return a single `Future`:

- `first` and `last` complete with the first or last event
- `length` completes with the number of events
- `join(separator)` completes with all events joined into one `String`
- `reduce(combine)` combines the events two at a time into one value

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` calls `combine` with the result so far and the next event. It throws if the stream is empty, so only use it when at least one event is guaranteed.

---

Stream methods fall into two groups:

- **transforming** methods like `map`, `where`, `take` and `skip` return a **new `Stream`** and are lazy: no event is processed until the new stream is listened to
- **consuming** methods like `toList`, `reduce`, `join`, `first`, `last` and `length` listen to the stream and return a **`Future`** with the final result

A chain therefore looks like zero or more transforming calls followed by at most one consuming call.

---

Generators produce events from inside one function. When events come from **elsewhere** (a button, a network callback, another object) you need a **`StreamController`**. It lives in the `dart:async` library, so the file must start with `import 'dart:async';`.

A controller owns a stream and lets you push events into it:

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

- `add(value)` sends one event
- `close()` ends the stream; forgetting it means listeners wait forever
- `stream` is the `Stream` that listeners consume

Events added before anyone listens are kept in a buffer, so the code above is safe: a listener that arrives later still receives `4` and `2`.

---

A `StreamController` is often created and consumed in the same place: subscribe to `controller.stream` with `listen`, then `add` events and `close` the controller. Because `listen` does not wait, the events are delivered after the current code finishes, but always in the order they were added:

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

The streams seen so far are **single-subscription**: they allow exactly one listener. Calling `listen`, `await for` or any consuming method a second time throws a `StateError` ("Stream has already been listened to").

To share a stream between several listeners, convert it to a **broadcast** stream with `asBroadcastStream()`:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

A broadcast stream does not buffer: a listener only receives the events emitted **after** it subscribed. In the example both listeners subscribe before the first `await`, so both receive every event.

---

A controller can create a broadcast stream directly with the named constructor `StreamController<T>.broadcast()`. Its `stream` accepts any number of listeners, and each event is delivered to all of them, in the order they subscribed:

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

Like every broadcast stream, it does not buffer: events added before a listener subscribes are lost for that listener.

---

A stream can carry **errors** as well as values. Inside an `async*` generator, a `throw` sends an error event and ends the stream; a `StreamController` can send one with `addError`.

On the consuming side, an `await for` loop rethrows the error where the loop is, so you handle it with an ordinary `try`/`catch` around the loop:

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

With `listen`, pass an `onError` callback instead: `stream.listen(print, onError: (e) => print('caught: $e'));`
