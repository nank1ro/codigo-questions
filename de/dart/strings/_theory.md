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

---

Manche Zeichen lassen sich nicht direkt innerhalb von Anführungszeichen eingeben. **Escape-Sequenzen** beginnen mit einem Backslash: `\n` ist ein Zeilenumbruch, `\t` ein Tab, `\\` ein Backslash und `\$` ein literales Dollarzeichen (andernfalls beginnt `$` eine Interpolation):

```dart
print('one\ntwo');   // gibt one und two in separaten Zeilen aus
print('Cost: \$5');  // Cost: $5
```

Ein **Raw-String** wird mit `r` vorangestellt: darin sind Backslashes und `$` einfache Zeichen, nichts wird escaped oder interpoliert:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

Für Text, der sich über mehrere Zeilen erstreckt, verwende einen **mehrzeiligen String**, begrenzt durch dreifache Anführungszeichen `'''` oder `"""`: Zeilenumbrüche darin bleiben erhalten.

```dart
var poem = '''
roses are red
violets are blue''';
```

---

Im Hintergrund wird jedes Zeichen eines Strings als Zahl gespeichert, seine **Code-Unit** (ein UTF-16-Code). `.codeUnitAt(index)` gibt den Code eines Zeichens zurück und `.codeUnits` die ganze Liste. `String.fromCharCode(code)` macht das Gegenteil und baut aus einem Code einen String:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

Aufeinanderfolgende Buchstaben haben aufeinanderfolgende Codes: `'A'` ist 65, `'B'` ist 66, und so weiter.

---

Zwei Strings sind mit `==` gleich, wenn sie exakt dieselben Zeichen in derselben Reihenfolge enthalten. Der Vergleich ist **case-sensitive** und zählt jedes Leerzeichen:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

Um ohne Berücksichtigung der Groß-/Kleinschreibung zu vergleichen, wandle zuerst beide Seiten um: `a.toLowerCase() == b.toLowerCase()`. Für eine Reihenfolge gibt `.compareTo(other)` eine negative Zahl, `0` oder eine positive Zahl zurück, je nachdem, ob der String vor, gleich mit oder nach dem anderen kommt.

---

Da Strings unveränderlich sind, erzeugt das Aufbauen eines langen Textes mit `+=` in einer Schleife bei jedem Schritt einen neuen String. Ein **StringBuffer** sammelt Textstücke effizient und erzeugt den endgültigen String erst, wenn du danach fragst:

- `.write(value)` hängt einen Wert an (jeder Typ wird in Text umgewandelt)
- `.writeln(value)` hängt den Wert gefolgt von einem Zeilenumbruch an
- `.toString()` gibt den bisher aufgebauten String zurück

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

String-Methoden geben Strings zurück, daher können sie nacheinander **verkettet** werden. Kombiniert mit `.split('')`, der Listen-Eigenschaft `.reversed` und `.join()` kannst du damit einen String in einem einzigen Ausdruck umkehren:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

Ein **Palindrom** ist ein Text, der vorwärts und rückwärts gelesen gleich ist, wie `level`.
