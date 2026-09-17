> Before I begin, I wanted to tell you that I am very happy to teach you Dart.
With this message I take the opportunity to let you know that the app you are using was written right in Dart, using the Flutter framework. So it is an honor for me to be able to share my expertise in the language.

Dart, like many other programming languages, allows you to document your code.
This allows you to write any text next to the code.
Comments are ignored by the compiler.

Dart supports _single-line_ comments, _multi-line_ comments, and _documentation_ comments.

Here is how to write a _single-line_ comment:
```dart
// This is a comment. It is not executed.
```

---

You can stack up _single-line_ comments in order to write _multi-line_ comments.
```dart
// This is a
// multi-line comment
```

---

You can also create comment blocks, or _multi-line_ comments.
_Multi-line_ comments begin with `/*` and end with `*/`.
```dart
/*
This is a multi-line
comment
*/
```

---

In addition to these two ways of writing comments, Dart includes _documentation comments_.

_Documentation comments_ are multi-line or single-line comments that begin with `///` or `/**.` The use of `///` on consecutive lines has the same effect as a multi-line documentation comment.

_Documentation comments_ are very useful because they allow documentation to be generated. 
You will want to add _documentation comments_ to your code to make it clear what a particular block of code does.

Within a _documentation comment_, the analyser resolves any name enclosed in square brackets as a reference to another API element.
Using square brackets one can refer to _classes_, _methods_, _fields_, _variables_, _functions_ and _parameters_.

Here is an example:
```dart
/// A domesticated South American camelid (Lama glama).
///
/// Just like any other animal, llamas need to eat,
/// so don't forget to [feed] them some [Food].
class Llama {
  String? name;

  /// Feeds your llama [food].
  ///
  /// The typical llama eats one bale of hay per week.
  void feed(Food food) {
    // ...
  }

  /// Exercises your llama with an [activity] for
  /// [timeLimit] minutes.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

In the generated documentation, `[feed]` becomes a link to the documentation for the `feed` method, and `[Food]` becomes a link to the documentation for the `Food` class.
While `[activity]` and `[timeLimit]` become a link to the documentation for `activity` and `timeLimit` respectively.
