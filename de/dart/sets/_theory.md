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
tags.add('dart');   // false, schon vorhanden
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

---

Sets unterstützen die klassischen Mengenoperationen. Jede gibt ein **neues** Set zurück und lässt die Originale unverändert:

- `a.union(b)` enthält die Elemente, die in `a` **oder** in `b` sind
- `a.intersection(b)` enthält die Elemente, die in **beiden**, `a` und `b`, sind
- `a.difference(b)` enthält die Elemente von `a`, die **nicht** in `b` sind

```dart
var a = {1, 2, 3};
var b = {2, 3, 4};
print(a.union(b));        // {1, 2, 3, 4}
print(a.intersection(b)); // {2, 3}
print(a.difference(b));   // {1}
```

---

Eine Liste in ein Set umzuwandeln ist der einfachste Weg, **Duplikate zu entfernen**: Jede Liste hat eine Methode `.toSet()`, die ein Set mit ihren eindeutigen Elementen in der Reihenfolge ihres ersten Auftretens zurückgibt. Ein Set hat eine Methode `.toList()`, die den umgekehrten Weg geht, sodass die Verkettung beider dir eine Liste ohne Duplikate liefert:

```dart
var votes = ['a', 'b', 'a', 'c', 'b'];
Set<String> unique = votes.toSet();
print(unique); // {a, b, c}
List<String> cleaned = votes.toSet().toList();
print(cleaned); // [a, b, c]
```

---

Sowohl Listen als auch Sets haben eine Methode `.contains()`, aber sie funktionieren sehr unterschiedlich. Eine Liste prüft ihre Elemente eins nach dem anderen von vorne, sodass eine Suche in einer langen Liste mit wachsender Liste langsamer wird. Ein Set speichert seine Elemente anhand ihres Hash, sodass `.contains()` einen Wert in ungefähr konstanter Zeit findet, egal wie viele Elemente vorhanden sind.

Wenn du die Zugehörigkeit oft prüfen musst und Reihenfolge oder Duplikate keine Rolle spielen, ist ein Set das richtige Werkzeug:

```dart
var banned = {'spam', 'scam'};
print(banned.contains('spam')); // schnell, selbst mit Millionen von Elementen
```
