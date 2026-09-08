Ein **Set** ist eine Sammlung von **eindeutigen** Werten: Derselbe Wert kann höchstens einmal vorkommen. Wie eine Map wird ein Set mit der `{}`-Literalsyntax erstellt, enthält aber einfache Werte statt `key: value`-Paare:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

Die Typannotation `Set<int>` teilt Dart mit, dass jedes Element ein `int` ist. Wie bei Listen und Maps leitet `var` den Typ aus dem Literal ab:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Ein Set speichert nie denselben Wert zweimal. Wenn ein Literal Duplikate enthält, wird nur das erste Vorkommen behalten und die anderen werden zur Laufzeit ohne Fehler verworfen (der Analyzer warnt dich vor einem Literal, das einen Wert wiederholt):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

Die Eigenschaft `.length` gibt zurück, wie viele **eindeutige** Elemente das Set enthält:

```dart
print(letters.length); // 3
```

---

Die Methode `.add(value)` fügt einen einzelnen Wert ein. Sie gibt `true` zurück, wenn der Wert hinzugefügt wurde, und `false`, wenn er bereits im Set war; in diesem Fall ändert sich nichts. Die Methode `.addAll(iterable)` fügt jedes Element einer Liste oder eines anderen Sets ein und überspringt dabei ebenfalls die bereits vorhandenen:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Ein leeres `{}`-Literal ist eine **Map**, kein Set. Um ein leeres Set zu erstellen, gib ihm einen Typ:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

Die Methode `.remove(value)` löscht einen Wert aus dem Set. Sie gibt `true` zurück, wenn der Wert vorhanden war, und sonst `false`:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Um alle Elemente auf einmal zu löschen, verwende `.clear()`.

---

Um zu prüfen, ob ein Wert in einem Set enthalten ist, verwende `.contains(value)`, das einen `bool` zurückgibt. Die Eigenschaft `.isEmpty` ist `true`, wenn das Set keine Elemente hat, und `.isNotEmpty`, wenn es mindestens eins hat:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Das Standard-Set in Dart merkt sich die **Einfügereihenfolge**: Wenn du es ausgibst oder darüber iterierst, erscheinen die Elemente in der Reihenfolge, in der sie zuerst hinzugefügt wurden. Das Hinzufügen eines bereits vorhandenen Werts verschiebt ihn nicht:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Ein Set ist ein `Iterable`, sodass du direkt mit `for-in` über seine Elemente iterieren kannst, genau wie bei einer Liste. Es gibt keine Indizes: Die Elemente werden in Einfügereihenfolge besucht:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
