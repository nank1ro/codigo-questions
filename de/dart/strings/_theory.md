Ein **String** ist ein Stück Text: eine Folge von Zeichen, die in Anführungszeichen eingeschlossen ist. In Dart kannst du einfache Anführungszeichen `'...'` oder doppelte Anführungszeichen `"..."` verwenden, sie funktionieren genau gleich:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Wenn du dich für eine Art von Anführungszeichen entscheidest, kannst du die andere Art innerhalb des Textes verwenden, ohne sie zu escapen:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Wenn du dasselbe Anführungszeichen innerhalb brauchst, escape es mit einem Backslash: `'It\'s sunny'`.

---

Zwei Strings können mit dem `+`-Operator zu einem neuen zusammengefügt werden, das nennt man **Verkettung**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart fügt außerdem zwei String-**Literale** zusammen, die direkt nebeneinander geschrieben werden, ganz ohne Operator. Das ist praktisch, um einen langen Text auf mehrere Zeilen aufzuteilen:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Nur Strings können mit `+` verkettet werden: `'Age: ' + 30` ist ein Kompilierfehler, weil `30` ein `int` ist.

---

Anstatt zu verketten, kannst du Werte mit **Interpolation** direkt in einen String einfügen. Schreibe `$name`, um den Wert einer Variablen einzufügen, und `${expression}`, um das Ergebnis eines beliebigen Ausdrucks einzufügen:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

Interpolation funktioniert mit jedem Typ: Zahlen, Booleans und Listen werden automatisch in Text umgewandelt, sodass `'Age: $age'` auch dann funktioniert, wenn `age` ein `int` ist.

---

Jeder String kennt über seine `.length`-Eigenschaft, wie viele Zeichen er enthält. Leerzeichen und Satzzeichen zählen ebenfalls als Zeichen:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Du kannst ein einzelnes Zeichen mit eckigen Klammern und seinem **Index** lesen, beginnend bei `0`. Das Ergebnis ist ein einzelnes Zeichen als `String`:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Das Lesen eines Index außerhalb des Strings (wie `word[5]`) wirft einen Fehler.

---

Strings sind in Dart **unveränderlich**: einmal erstellt, ändert sich ein String nie mehr. Methoden wie `.toUpperCase()` und `.toLowerCase()` verändern den ursprünglichen String nicht, sie **geben einen neuen zurück**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Wenn die Variable den neuen Wert enthalten soll, weise das Ergebnis wieder zu: `word = word.toUpperCase();`.

---

Von Nutzern eingegebener Text hat oft zusätzliche Leerzeichen drumherum. Die Methode `.trim()` gibt eine Kopie des Strings ohne führende und nachgestellte Leerzeichen (Leerzeichen, Tabs und Zeilenumbrüche) zurück. `.trimLeft()` und `.trimRight()` entfernen sie nur auf einer Seite:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

Die Methode `.substring(start, end)` gibt den Teil eines Strings vom Index `start` bis, **aber ohne**, Index `end` zurück. Wenn du `end` weglässt, wird alles bis zum Ende des Strings genommen:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Mehrere Methoden lassen dich innerhalb eines Strings suchen:

- `.contains(other)` gibt `true` zurück, wenn `other` irgendwo im String vorkommt
- `.startsWith(other)` und `.endsWith(other)` prüfen den Anfang und das Ende
- `.indexOf(other)` gibt den Index des ersten Vorkommens zurück, oder `-1`, wenn es nicht gefunden wird

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Alle sind case-sensitive: `'Dart'.contains('dart')` ist `false`.

---

Die Methode `.replaceAll(from, to)` gibt einen neuen String zurück, in dem **jedes** Vorkommen von `from` durch `to` ersetzt wird. `.replaceFirst(from, to)` ersetzt nur das erste:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

Die Methode `.split(separator)` zerlegt einen String bei jedem Vorkommen des Trennzeichens in eine `List<String>`. Das Gegenteil ist `.join(separator)`, eine Methode von Listen, die die Elemente zu einem String zusammenfügt:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Der Aufruf von `.split('')` mit einem leeren Trennzeichen liefert dir eine Liste mit jedem einzelnen Zeichen.
