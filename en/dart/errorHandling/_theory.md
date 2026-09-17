Some statements cannot be carried out: reading text that is not a number, taking an element past the end of a list, asking for the first item of an empty one. When that happens Dart **throws** an object that describes the failure.

You can throw one yourself with the `throw` keyword. `Exception('message')` builds a ready-made object carrying a short explanation:

```dart
throw Exception('no fuel');
```

A throw is not a `return`. It abandons the statement, the function, and every caller above it, looking for something that handles it. When nothing does, the program stops and prints the failure:

```
Unhandled exception:
Exception: no fuel
```

Everything after the throw is skipped, so the lines that would have run never do. That is what this topic is about: deciding where a failure is handled instead of letting it end the program.

---

To keep the program alive, wrap the risky statement in a `try` block and describe the recovery in a `catch` block:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` throws when the text does not describe a whole number. Dart leaves the `try` block at the first statement that throws, skips the rest of it, runs the `catch` block, and then carries on with the code that follows. The variable in the parentheses, `e` here, is the thrown object itself.

Nothing inside the `try` block is undone, so keep it as short as the failure you expect.

---

A bare `catch` takes everything, which also hides the failures you did not plan for. To handle exactly one kind, name its type in an `on` clause:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` throws a **`FormatException`** when the text is not a whole number, so that is the type to name when reading input. An `on` clause matches that type and its subtypes, and nothing else: any other failure keeps travelling outwards and still shows up, instead of being swallowed by a recovery that was never meant for it.

---

One `try` block can be followed by **several** clauses, each recovering from a different failure. Dart compares the thrown object against them from top to bottom and runs the **first** one that matches:

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

Reading a list with an index that does not exist throws a **`RangeError`**, so the two failures of that one line get different answers.

Because the first match wins, order matters: a clause for a general type placed above a more specific one would always win, leaving the specific clause unreachable. Write the specific clauses first, and a bare `catch` last if you want a safety net.

The `on RangeError` clause above is here only to show how several clauses are ordered. `RangeError` signals a mistake in the code rather than a condition the program could not control, and a later exercise explains why such a failure should be prevented instead of caught.

---

Often the recovery does not need the thrown object at all: the type already says everything. In that case drop the `catch` part and keep only the `on` clause:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

The two forms differ only in whether you get a variable:

- `on FormatException catch (e)` — matches that type and gives you the object as `e`
- `on FormatException` — matches that type, no variable
- `catch (e)` — matches everything and gives you the object

Leaving out an unused variable keeps the handler honest about what it actually uses.

---

A third block can follow the handlers. `finally` runs **in every case**: after the `try` block finished normally, after a handler recovered, and also when nothing matched and the failure is still travelling outwards.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

It even runs before a `return` hands its value back, which is why the message above is printed before the caller sees the result. That makes `finally` the place for work that must happen either way, such as closing what you opened.

---

Your own code throws the same way the library does. `Exception('message')` builds a plain exception carrying a short explanation, and `throw` sends it on its way:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

The message is not lost: `toString()` puts the word `Exception`, a colon and the message together, which is exactly what the unhandled-exception report prints.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Throwing beats returning a made-up value such as `-1`: the caller cannot forget to look at it, and the reason travels with it.

---

Sometimes a handler is not the right place to recover: you only want to *notice* the failure and let it continue to the caller who can actually deal with it. The `rethrow` keyword does that, inside a `catch` or `on ... catch` block:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` sends the **same** object onwards, so the caller sees the original failure. Writing `throw e` instead would also work, but it restarts the journey and loses where the failure first happened.

A `finally` block in the same statement still runs, even on the way out.

---

A `catch` clause accepts a **second** parameter:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

The first is the thrown object, the second is a `StackTrace`: the chain of calls that were running at the moment of the throw. It answers *where* the failure came from, which the message alone rarely does.

A stack trace lists file names, line numbers and frames, and it changes with the build and the call path. Print it, attach it to a report, pass it on — but never compare it against a fixed text, and never build program behaviour on top of its contents. Ask for it only when you are going to log it.

---

`Exception` is an interface, so your own class can be one. A custom exception gives the failure a name that an `on` clause can select, and fields that a handler can read:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Three parts are worth keeping: `implements Exception` so the class belongs with the other failures, a `final` field carrying the detail, and an overridden `toString()` so the unhandled-exception report is readable. Without that override, Dart prints the bare class name and the detail is lost.

---

Dart throws two families of objects, and they mean opposite things.

An **`Exception`** describes a condition the program could not control: text that was not a number, a file that was not there, a network that answered nothing. `FormatException` is one. These are expected, and catching them is the normal response.

An **`Error`** describes a mistake in the code itself:

- `ArgumentError` — a function was called with a value it documents as invalid
- `StateError` — an object was used at a moment when it cannot do what was asked
- `RangeError` — an index or a value was outside the allowed range

Catching an `Error` hides the bug instead of fixing it. The right answer is to change the code so it stops being thrown: check the argument before calling, or use an API that does not throw. That is why an `on FormatException` clause is good practice, while an `on ArgumentError` clause almost always is not.

---

Some libraries offer a version that does not throw at all. Next to `int.parse`, Dart has **`int.tryParse`**: same conversion, but it returns `null` instead of throwing when the text is not a number.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

The result is an `int?`, so the `??` operator turns it straight into a default:

```dart
final port = int.tryParse(text) ?? 8080;
```

When the failure is ordinary and you only want a fallback, this is shorter and clearer than a `try` block. Keep `int.parse` for the cases where bad text really is a failure that somebody above must hear about.

---

`firstWhere` returns the first element matching a test. When nothing matches there is no element to return, so it throws a `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Like `int.tryParse`, the library offers a way out. The named parameter `orElse` takes a function that produces the value to use when nothing matched:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

The choice is the same one as before: `orElse` when "nothing matched" is an ordinary outcome, the bare call when it would mean the data is broken and somebody must hear about it.

---

The `throw` and the `try` do not have to live in the same function. A function that cannot do its job throws, and the caller that knows what to do about it catches:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` has no opinion about whether a bad age should end the program, show a message or be skipped — that is the caller's decision, and the caller is where the `try` block belongs. This split is why throwing is worth more than returning `-1`: the failure reaches the one place that can answer it.

Remember that the `try` block stops at the first failure, so the statements after the failing call are skipped too.

---

Where the `try` block sits decides how much work a single failure destroys. Around a loop, the first bad element ends the whole batch; **inside** the loop, only that element is lost and the rest is still processed:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

This is the everyday shape for importing a file, reading a list of settings or handling a queue of messages: one damaged row should not throw away the good ones. The rule stays the same as before — keep the `try` block around the statement that can fail, and no larger.

---

The last piece is throwing an `Error` on purpose. A function that documents what it accepts should refuse anything else loudly, and `ArgumentError` is the object for that:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

The message is reachable as `e.message`, and `toString()` prints `Invalid argument(s): ` followed by it.

This does not contradict the rule from before. Throwing an `ArgumentError` is right, catching one is not: it tells the *caller's* author that the call itself is wrong, and the fix is a check before the call, not a handler around it.
