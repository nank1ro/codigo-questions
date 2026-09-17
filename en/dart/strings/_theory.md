A **String** is a piece of text: a sequence of characters wrapped in quotes. In Dart you can use single quotes `'...'` or double quotes `"..."`, they work exactly the same way:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Picking one kind of quote lets you use the other kind inside the text without any escaping:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

If you need the same quote inside, escape it with a backslash: `'It\'s sunny'`.

---

Two strings can be joined into a new one with the `+` operator, called **concatenation**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart also joins two string **literals** that are written next to each other, without any operator. This is handy for splitting a long text over several lines:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Only strings can be concatenated with `+`: `'Age: ' + 30` is a compile error, because `30` is an `int`.

---

Instead of concatenating, you can insert values directly into a string with **interpolation**. Write `$name` to insert the value of a variable, and `${expression}` to insert the result of any expression:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

Interpolation works with any type: numbers, booleans and lists are converted to text automatically, so `'Age: $age'` is fine even though `age` is an `int`.

---

Every string knows how many characters it holds through its `.length` property. Spaces and punctuation count as characters too:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

You can read a single character with square brackets and its **index**, starting from `0`. The result is a one-character `String`:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Reading an index outside the string (like `word[5]`) throws an error.

---

Strings in Dart are **immutable**: once created, a string never changes. Methods like `.toUpperCase()` and `.toLowerCase()` do not modify the original string, they **return a new one**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

If you want the variable to hold the new value, assign the result back: `word = word.toUpperCase();`.

---

Text typed by a user often has extra spaces around it. The `.trim()` method returns a copy of the string without leading and trailing whitespace (spaces, tabs and newlines). `.trimLeft()` and `.trimRight()` remove it only on one side:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

The `.substring(start, end)` method returns the part of a string from index `start` up to, **but not including**, index `end`. If you omit `end`, it takes everything until the end of the string:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Several methods let you search inside a string:

- `.contains(other)` returns `true` if `other` appears anywhere in the string
- `.startsWith(other)` and `.endsWith(other)` check the beginning and the end
- `.indexOf(other)` returns the index of the first occurrence, or `-1` if it is not found

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

All of them are case-sensitive: `'Dart'.contains('dart')` is `false`.

---

The `.replaceAll(from, to)` method returns a new string where **every** occurrence of `from` is replaced by `to`. `.replaceFirst(from, to)` replaces only the first one:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

The `.split(separator)` method cuts a string into a `List<String>` at every occurrence of the separator. The opposite is `.join(separator)`, a method of lists that glues the elements into one string:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Calling `.split('')` with an empty separator gives you a list with every single character.

---

Some characters cannot be typed directly inside quotes. **Escape sequences** start with a backslash: `\n` is a newline, `\t` a tab, `\\` a backslash and `\$` a literal dollar sign (otherwise `$` starts an interpolation):

```dart
print('one\ntwo');   // prints one and two on separate lines
print('Cost: \$5');  // Cost: $5
```

A **raw string** is prefixed with `r`: inside it, backslashes and `$` are plain characters, nothing is escaped or interpolated:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

For text that spans several lines, use a **multi-line string** delimited by triple quotes `'''` or `"""`: line breaks inside it are kept.

```dart
var poem = '''
roses are red
violets are blue''';
```

---

Under the hood, every character of a string is stored as a number, its **code unit** (a UTF-16 code). `.codeUnitAt(index)` gives the code of one character and `.codeUnits` gives the whole list. `String.fromCharCode(code)` does the opposite, building a string from a code:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

Consecutive letters have consecutive codes: `'A'` is 65, `'B'` is 66, and so on.

---

Two strings are equal with `==` when they contain exactly the same characters, in the same order. The comparison is **case-sensitive** and counts every space:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

To compare while ignoring case, convert both sides first: `a.toLowerCase() == b.toLowerCase()`. For ordering, `.compareTo(other)` returns a negative number, `0` or a positive number depending on whether the string comes before, is equal to, or comes after the other.

---

Because strings are immutable, building a long text with `+=` in a loop creates a new string at every step. A **StringBuffer** collects pieces of text efficiently and produces the final string only when you ask for it:

- `.write(value)` appends a value (any type is converted to text)
- `.writeln(value)` appends the value followed by a newline
- `.toString()` returns the string built so far

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

String methods return strings, so they can be **chained** one after the other. Combined with `.split('')`, the list property `.reversed` and `.join()`, this lets you reverse a string in a single expression:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

A **palindrome** is a text that reads the same forwards and backwards, like `level`.
