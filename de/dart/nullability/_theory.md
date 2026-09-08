Du weißt bereits, wie man eine Variable mit einem Typ deklariert, zum Beispiel `String name = 'Ada';`. Manchmal fehlt ein Wert aber einfach: ein Benutzer ohne Spitzname, eine Suche, die nichts findet, ein Text, der sich nicht in eine Zahl umwandeln lässt. Dart stellt einen fehlenden Wert mit `null` dar.

Seit Dart 2.12 hat die Sprache **sound null safety**: Ein normaler Typ wie `String` kann **niemals** `null` enthalten. Der Versuch einer solchen Zuweisung ist ein Kompilierfehler, sodass das Programm gar nicht erst läuft:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Um einen fehlenden Wert zuzulassen, hängst du ein Fragezeichen `?` an den Typ an. Ein `String?` enthält entweder einen `String` oder `null`, und die Ausgabe von `null` zeigt das Wort `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Typen ohne `?` heißen **nicht-nullable**, Typen mit `?` heißen **nullable**.

---

Eine nullable Variable, die **ohne Wert** deklariert wird, beginnt als `null`, sodass `= null` weggelassen werden kann:

```dart
int? age;
print(age); // null
```

Eine nicht-nullable Variable hat keinen solchen Standardwert: Dart weigert sich, Code zu kompilieren, der sie liest, bevor ein Wert zugewiesen wurde.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Der Aufruf einer Methode oder das Lesen einer Eigenschaft von `null` würde abstürzen, deshalb erlaubt Dart dir das bei einem nullable Wert nicht mit dem gewöhnlichen Punkt:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

Der Operator `?.` für **null-aware Zugriff** löst dieses Problem: Ist der Wert `null`, ist der gesamte Ausdruck `null` und nichts weiter wird ausgewertet, andernfalls funktioniert er wie ein normaler `.`:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Da das Ergebnis `null` sein kann, ist sein Typ nullable: `text?.length` ist ein `int?`, kein `int`.

---

Oft soll ein fehlender Wert durch einen **Standardwert** ersetzt werden. Der **If-Null-Operator** `??` gibt den linken Operanden zurück, wenn dieser nicht `null` ist, andernfalls den rechten Operanden:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` reagiert nur auf `null`: Ein leerer String `''` oder die Zahl `0` sind echte Werte und werden beibehalten.

`??` lässt sich gut mit `?.` kombinieren, weil `?.` ein nullable Ergebnis erzeugt:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

Der große Vorteil von null safety ist, dass die meisten `null`-Fehler vom **Compiler** gefunden werden und nicht von deinen Benutzern. Die Regeln bisher:

- ein nicht-nullable Typ (`String`, `int`, `List<int>`...) kann niemals `null` sein
- ein nullable Typ (`String?`, `int?`, `List<int>?`...) kann es, und er beginnt als `null`, wenn er ohne Wert deklariert wird
- `.` auf einem nullable Wert kompiliert nicht: verwende `?.` oder gib einen Standardwert mit `??` an

---

Der **If-Null-Zuweisungsoperator** `??=` weist einer Variablen einen Wert **nur dann** zu, wenn diese Variable aktuell `null` ist; andernfalls lässt er sie unverändert:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

Er funktioniert auch auf Map-Einträgen, die nullable sind, weil ein Schlüssel fehlen kann:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

Manchmal weißt **du**, dass ein nullable Wert an einer bestimmten Stelle nicht `null` ist, auch wenn der Compiler das nicht erkennen kann. Der **Null-Assertion-Operator** `!` macht aus einem `String?` einen `String`, indem er verspricht, dass der Wert vorhanden ist:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Sei vorsichtig: `!` verlagert die Prüfung von der Kompilierzeit zur Laufzeit. Ist der Wert **tatsächlich** `null`, wirft das Programm einen Fehler und stoppt:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Verwende `!` sparsam und nur, wenn ein `null` an dieser Stelle ohnehin ein Bug wäre.

---

Erinnere dich an den Unterschied zwischen den drei Operatoren, die du an einem nullable Wert gesehen hast:

- `?.` gibt `null` zurück, wenn der Wert `null` ist, und wirft nie
- `??` ersetzt `null` durch einen Standardwert
- `!` nimmt an, dass der Wert vorhanden ist, und **wirft zur Laufzeit**, wenn er es nicht ist

Keiner davon ist ein Kompilierfehler: Der Compiler vertraut deinem `!`, und nur das laufende Programm kann herausfinden, dass das Versprechen gebrochen wurde.

---

Einen nullable Wert mit `if` zu prüfen ist sicherer als `!`, und Dart belohnt dich dafür. Nach einer Prüfung wie `if (x != null)` weiß der Compiler, dass `x` innerhalb des Blocks nicht `null` sein kann, und behandelt `x` dort als nicht-nullable. Das nennt man **Type Promotion**:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

Die Promotion funktioniert auch nach einem vorzeitigen `return`:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

Die Promotion gilt für **lokale Variablen und Parameter**, deren Wert sich zwischen Prüfung und Verwendung nicht heimlich ändern kann.

---

Type Promotion funktioniert **nicht** bei einem Klassen**feld**, das von außen geändert werden kann, denn zwischen Prüfung und Verwendung könnte ein anderer Codeabschnitt (ein in einer Unterklasse überschriebener Getter, eine andere Methode) es wieder auf `null` setzen:

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

Die übliche Lösung ist, das Feld in eine **lokale Variable** zu kopieren, für die die Promotion tatsächlich greift:

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

Ein nicht-nullable Feld muss normalerweise im Konstruktor einen Wert erhalten. Ist der Wert erst **später** bekannt (nach dem Lesen einer Datei, dem Öffnen einer Verbindung ...), kannst du das Feld als `late` markieren: Der Compiler akzeptiert den fehlenden Initialisierer und vertraut darauf, dass du das Feld zuweist, bevor du es liest.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Das Lesen eines `late`-Feldes, dem noch kein Wert zugewiesen wurde, wirft zur Laufzeit einen `LateInitializationError`. Wie `!` tauscht `late` eine Garantie zur Kompilierzeit gegen eine Prüfung zur Laufzeit ein, es ist also ein Versprechen, das du einhalten musst.

`late` lässt sich auch mit einem Initialisierer kombinieren, der dann **verzögert** ausgeführt wird, nämlich beim ersten Lesen der Variable:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

Die Nullbarkeit bestimmt, wie du **benannte Parameter** deklarierst. Ein benannter Parameter mit einem nullable Typ ist optional: Lässt der Aufrufer ihn weg, ist er einfach `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Ein benannter Parameter mit einem nicht-nullable Typ und ohne Standardwert hätte beim Weglassen keinen Wert, daher verlangt Dart von dir, ihn als `required` zu markieren; der Aufrufer muss ihn dann immer übergeben:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

Nullbarkeit gilt auch für die **Elemente** einer Collection. Eine `List<int>` enthält niemals `null`, während eine `List<int?>` es kann:

```dart
List<int?> scores = [7, null, 9];
```

Beachte den Unterschied zu `List<int>?`: Das ist eine Liste, die selbst fehlen kann, aber wenn sie vorhanden ist, enthält sie nur echte Zahlen.

Um die `null`-Elemente loszuwerden, gibt `nonNulls` ein `Iterable` zurück, das nur die vorhandenen Werte enthält, typisiert ohne `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` macht dasselbe und funktioniert auch, wenn die Liste mehrere Typen mischt.

---

Viele Bibliotheksfunktionen verwenden `null`, um zu melden, dass etwas **nicht getan werden konnte**. Das Umwandeln eines Strings in eine Zahl ist das klassische Beispiel: `int.parse` wirft eine `FormatException`, wenn der Text keine Zahl ist, während `int.tryParse` stattdessen `null` zurückgibt und dir die Entscheidung überlässt, was zu tun ist:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

Der Rückgabetyp von `int.tryParse` ist `int?`, also gilt alles, was du gelernt hast: `??` für einen Standardwert, `?.` zum Verketten und eine `if`-Prüfung für die Promotion. `double.tryParse` funktioniert genauso.

---

Zwei weitere Operatoren haben eine null-aware Variante.

Die **Null-aware-Kaskade** `?..` führt eine Kette von Kaskadenoperationen nur aus, wenn das Objekt nicht `null` ist, und überspringt sie andernfalls alle:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

Der **Null-aware-Spread** `...?` fügt die Elemente einer nullable Collection in ein Literal ein, ohne etwas hinzuzufügen, wenn die Collection `null` ist:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Ohne das `?` wäre `...extra` auf einer `List<int>?` ein Kompilierfehler.

---

Echte Daten sind voller Lücken: ein leer gelassenes Formularfeld, eine in einer Datei fehlende Spalte, ein String, der nicht ganz eine Zahl ist. Die Werkzeuge dieses Kapitels lassen sich natürlich kombinieren, um damit umzugehen: `nonNulls`, um fehlende Elemente zu verwerfen, `int.tryParse`, um sicher umzuwandeln, und `??` oder eine `if`-Prüfung, um das zu behandeln, was nicht umgewandelt werden konnte.
