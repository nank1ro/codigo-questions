Every line of Dart you have written so far runs inside an **isolate**: a thread with its own memory and its own event loop. A program starts with one isolate, the *main* isolate, and can start more.

What makes isolates special is that they share **nothing**. Two isolates never see the same object, so there is no locking, no data race and no half-updated value. They talk to each other only by passing **copies** of messages.

The shortest way to use a second isolate is **`Isolate.run`**. It takes a function, runs it on a brand new isolate, and gives you back a `Future` with its result:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` lives in the `dart:isolate` library, so the file must start with `import 'dart:isolate';`. While the new isolate computes, the main isolate stays free: this is real **parallelism**, the work happens on another processor core.

---

The function you hand to `Isolate.run` may **capture** variables from around it. Those values are copied into the new isolate together with the function, so the computation can depend on its caller:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` returns a `Future` of whatever the function returns, so `triple` can simply return it: no `async` and no `await` are needed when you just pass the future on.

The point of moving work to another isolate is that long computations no longer freeze the main one. A loop that runs for a second blocks everything when it runs on the main isolate; inside `Isolate.run` it runs elsewhere and the main isolate keeps handling its own events.

---

Only **data** is copied between isolates; **code** is not. Every isolate of a program can already see all the top-level functions and classes of that program, so the computation given to `Isolate.run` is free to call them:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

What travels is the captured `text` on the way in and the resulting `int` on the way out, each one a copy. The pattern is always the same: keep the heavy function where it is, and wrap the **call** in `Isolate.run`.

---

`await` and `Isolate.run` solve two different problems, and it is worth keeping them apart.

`await` gives you **concurrency** on a single isolate: while one function waits for a timer or a server, the isolate runs other pending code. Nothing runs at the same instant, the isolate just stops idling. This is the right tool for waiting.

`Isolate.run` gives you **parallelism**: a second isolate on a second processor core, running its own code at the same instant as the first. This is the right tool for computing.

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

Awaiting a slow calculation does not help at all: `await bigSum()` still runs `bigSum` on the current isolate and blocks it until the last line. Only a second isolate moves that work away.

---

`Isolate.run` is the shortcut for a single result. When you want an isolate that keeps running and reports back more than once, start it yourself with **`Isolate.spawn`** and give it a way to answer.

That way is a pair of ports. A **`ReceivePort`** is a mailbox: you create it on your side and read the messages that arrive. Its **`sendPort`** is the address of that mailbox, and it is the only thing the other isolate needs in order to reply.

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

`Isolate.spawn` takes the function to run and the single message to pass to it, here the `SendPort`. On the other side, `send` drops a value into the mailbox, and `await receivePort.first` waits for the first message and closes the port.

---

The function given to `Isolate.spawn` is called the **entry point**. It must be a top-level (or static) function that takes exactly one parameter: the message `Isolate.spawn` passes to it.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

The messages arriving in a `ReceivePort` have the static type `dynamic`, because any value could have been sent. When you know what the other isolate sends, cast it:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

A spawned isolate always follows the same four steps: open the mailbox, spawn the worker with its address, wait for the answer, use it.

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

The `await` in front of `Isolate.spawn` waits for the isolate to *start*, not for it to finish its work: the result arrives later, through the port.

---

`Isolate.spawn` passes exactly **one** message to the entry point, and the worker usually needs both a `SendPort` to answer on and some data to work with. The usual trick is to bundle everything into one `List` and unpack it on the other side:

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

The list is copied on the way in, so the worker reads its own values. A `SendPort` is one of the few things that is not copied but shared: it keeps pointing at the mailbox of the isolate that created it, which is exactly why it can be used as a return address.

---

`first` reads one message and closes the mailbox. A `ReceivePort` is also a **`Stream`**, so to read many messages you loop over it with `await for`.

The loop never ends on its own: the port stays open waiting for a message that may never come. The worker therefore sends a last value as a signal, often `null`, and the listener reacts by calling **`close()`**, which ends the stream and the loop:

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

Collecting a whole series of messages follows one recipe: an empty list before the loop, one `add` per real message, and `close()` on the signal that ends the stream. Once the port is closed the `await for` finishes and the function can return:

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

Messages keep the order in which they were sent, so the list you build mirrors the work of the other isolate step by step.

---

An open `ReceivePort` counts as pending work: as long as one exists, the isolate that owns it has a reason to stay alive and its event loop keeps waiting for a message. In a command line program, a main isolate with an open port simply **never exits**, and you have to stop it by hand.

Closing the port is therefore part of the job, not an optimisation:

- `await port.first` closes it for you after one message
- `port.close()` closes it explicitly, which is what you need after an `await for` loop

`Isolate.run` has none of this bookkeeping: it creates the ports, closes them and shuts the isolate down for you. Prefer it whenever one result is all you need.

---

An exception thrown inside an isolate cannot jump across to another one: the two have separate stacks. `Isolate.run` bridges that gap for you by catching the error, copying it back and making the returned future fail with it. On your side it is therefore an ordinary asynchronous error, caught with `try`/`catch` around the `await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

The `await` inside the `try` matters, exactly as with any other future: without it the future would leave the `try` block unfinished and the `catch` would never run.

With `Isolate.spawn` there is no such bridge. An uncaught error kills the spawned isolate silently and the parent keeps waiting for a message that will never arrive, which is one more reason to reach for `Isolate.run` first.

---

The error that comes back from `Isolate.run` is a **copy** of the one thrown on the other side, so the usual checks still work: `catch (e)` gives you the object, and `e is FormatException` tells you which kind of failure it was.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

What you cannot rely on is the stack trace pointing into your own isolate: the error travelled, the stack did not.

---

Put together, an `Isolate.run` program reads like ordinary sequential code: the line before the call runs on the main isolate, the computation runs elsewhere, and the line after the `await` runs back on the main isolate with the result in hand.

```dart
import 'dart:isolate';

int double(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => double(4));
  print(result);
}
// start
// 8
```

---

Because isolates share no memory, every message is **copied** when it crosses. Numbers, booleans, strings, `null`, lists, maps and most plain objects can make the trip; a few things cannot be copied at all, such as an open socket, and trying to send one throws an `ArgumentError`.

The consequence is the rule that makes isolates safe: after sending, the two sides hold **two independent objects**. Whatever one isolate does to its copy is invisible to the other.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort` is the exception that proves the rule: it is shared rather than copied, precisely so that it can still point at the original mailbox.

---

Each `Isolate.run` starts its own isolate, so several of them really do run at the same instant, on as many cores as the machine has. The pattern is the one you already know from futures: start every computation first, then wait for all of them with `Future.wait`, which keeps the results in the order of the input.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Starting an isolate is not free: it costs memory and a few milliseconds. Splitting one long computation across a handful of isolates pays off, sending a thousand trivial additions to a thousand isolates does not.
