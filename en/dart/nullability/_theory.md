You already know how to declare a variable with a type, such as `String name = 'Ada';`. Sometimes, though, a value is simply **missing**: a user without a nickname, a search that finds nothing, a text that cannot be turned into a number. Dart represents a missing value with `null`.

Since Dart 2.12 the language has **sound null safety**: a normal type like `String` can **never** hold `null`. Trying to assign it is a compile error, so the program does not even run:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

To allow a missing value you add a question mark `?` after the type. A `String?` holds either a `String` or `null`, and printing `null` shows the word `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Types without `?` are called **non-nullable**, types with `?` are **nullable**.

---

A nullable variable declared **without a value** starts as `null`, so `= null` can be left out:

```dart
int? age;
print(age); // null
```

A non-nullable variable has no such default: Dart refuses to compile any code that reads it before a value has been assigned.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Calling a method or reading a property on `null` would crash, so Dart does not let you do it on a nullable value with the usual dot:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

The **null-aware access** operator `?.` solves this: if the value is `null` the whole expression is `null` and nothing else is evaluated, otherwise it works like a normal `.`:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Since the result may be `null`, its type is nullable: `text?.length` is an `int?`, not an `int`.

---

Often a missing value should be replaced by a **default**. The **if-null** operator `??` returns the left operand when it is not `null`, and the right operand otherwise:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` only reacts to `null`: an empty string `''` or the number `0` are real values, so they are kept.

`??` combines nicely with `?.`, because `?.` produces a nullable result:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

The big advantage of null safety is that most `null` mistakes are found by the **compiler**, not by your users. The rules so far:

- a non-nullable type (`String`, `int`, `List<int>`...) can never be `null`
- a nullable type (`String?`, `int?`, `List<int>?`...) can, and starts as `null` when declared without a value
- `.` on a nullable value does not compile: use `?.` or provide a default with `??`

---

The **if-null assignment** operator `??=` assigns a value to a variable **only if** that variable is currently `null`; otherwise it leaves it untouched:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

It also works on map entries, which are nullable because a key might be missing:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

Sometimes **you** know that a nullable value is not `null` at a certain point, even if the compiler cannot tell. The **null assertion** operator `!` turns a `String?` into a `String` by promising that the value is present:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Be careful: `!` moves the check from compile time to run time. If the value **is** `null`, the program throws an error and stops:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Use `!` sparingly, and only when a `null` there would be a bug anyway.

---

Remember the difference between the three operators you have seen on a nullable value:

- `?.` returns `null` when the value is `null`, and never throws
- `??` replaces `null` with a default
- `!` assumes the value is present and **throws at run time** when it is not

None of them is a compile error: the compiler trusts your `!`, and only the running program can find out that the promise was broken.

---

Checking a nullable value with `if` is safer than `!`, and Dart rewards you for it. After a check like `if (x != null)`, the compiler knows that `x` cannot be `null` inside the block, so it treats `x` as non-nullable there. This is called **type promotion**:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

Promotion also works after an early return:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

Promotion applies to **local variables and parameters**, whose value cannot change behind your back between the check and the use.

---

Type promotion does **not** work on a class **field** that can be changed from outside, because between the check and the use another piece of code (a getter overridden in a subclass, another method) could set it back to `null`:

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

The standard fix is to copy the field into a **local variable**, which does promote:

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

A non-nullable field must normally receive a value in the constructor. When the value is only known **later** (after reading a file, opening a connection...), you can mark the field `late`: the compiler accepts the missing initializer and trusts you to assign the field before reading it.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Reading a `late` field that has not been assigned yet throws a `LateInitializationError` at run time. Like `!`, `late` trades a compile-time guarantee for a run-time check, so it is a promise you must keep.

`late` can also be combined with an initializer, which then runs **lazily**, the first time the variable is read:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

Nullability shapes how you declare **named parameters**. A named parameter with a nullable type is optional: when the caller omits it, it is simply `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

A named parameter with a non-nullable type and no default value would have no value when omitted, so Dart requires you to mark it `required`; the caller must then always pass it:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

Nullability also applies to the **elements** of a collection. A `List<int>` never contains `null`, while a `List<int?>` may:

```dart
List<int?> scores = [7, null, 9];
```

Note the difference with `List<int>?`, which is a list that may itself be missing but, when present, holds only real numbers.

To get rid of the `null` elements, `nonNulls` returns an `Iterable` with only the present values, typed without `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` does the same and also works when the list mixes several types.

---

Many library functions use `null` to report that something **could not be done**. Converting a string to a number is the classic example: `int.parse` throws a `FormatException` when the text is not a number, while `int.tryParse` returns `null` instead and lets you decide what to do:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

The return type of `int.tryParse` is `int?`, so everything you learned applies: `??` for a default, `?.` to chain, and an `if` check to promote. `double.tryParse` works the same way.

---

Two more operators have a null-aware variant.

The **null-aware cascade** `?..` runs a chain of cascade operations only when the object is not `null`, and skips them all otherwise:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

The **null-aware spread** `...?` inserts the elements of a nullable collection into a literal, adding nothing when the collection is `null`:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Without the `?`, `...extra` on a `List<int>?` would be a compile error.

---

Real data is full of gaps: a form field left empty, a column missing from a file, a string that is not quite a number. The tools of this chapter combine naturally to handle them: `nonNulls` to drop missing elements, `int.tryParse` to convert safely, `??` or an `if` check to deal with what could not be converted.
