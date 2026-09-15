Eine `List` hält nicht einfach nur Werte, sie hält Werte **eines Typs**. Der Typ steht in spitzen Klammern direkt nach dem Namen der Collection:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` und `int` sind hier **Typargumente**, und ein Typ, der eines entgegennimmt, heißt **generisch**. Die List-Klasse wird einmal geschrieben, und `List<String>` und `List<int>` sind zwei verschiedene Typen, die daraus entstehen.

Der Lohn dafür ist, dass der Compiler weiß, was drinsteckt:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // gut: first ist ein String
```

---

`List` ist nicht die einzige generische Collection. Ein `Set` nimmt ein Typargument entgegen, eine `Map` nimmt **zwei**: eines für die Schlüssel und eines für die Werte, in dieser Reihenfolge.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Ein leerer Collection-Literal lässt sich nicht aus seinem Inhalt ablesen, daher schreibst du die Typargumente direkt auf den Literal selbst:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Sind die Typen erst einmal bekannt, hat bereits alles, was du der Collection entnimmst, den richtigen Typ: `ages['Ada']` ist ein `int?`, nie ein Rätselwert.

---

Dart hat außerdem den Typ `dynamic`, der bedeutet: „alles ist erlaubt“. Eine `List<dynamic>` akzeptiert jeden Wert, sieht also bequemer aus als eine `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // akzeptiert
print(things.first.toUpperCase()); // akzeptiert
```

Der Haken: Während du den Code schreibst, wird nichts geprüft. Jeder Aufruf auf einem `dynamic`-Wert wird erst aufgelöst, während das Programm läuft, sodass sich ein Tippfehler wie `things.first.toUpperCse()` gerne kompilieren lässt und vor den Augen eines Benutzers explodiert.

Generics sind die Alternative: ein einziges Stück Code, das mit **jedem** Typ funktioniert, während jede Verwendung davon dennoch auf **einen** Typ geprüft wird. Genau darum geht es in diesem Thema.

---

Du bist nicht auf die generischen Klassen beschränkt, die Dart mitbringt: Du kannst eigene deklarieren. Ein **Typparameter** steht in spitzen Klammern nach dem Klassennamen, und von da an ist er innerhalb des Körpers ein normaler Typ:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` ist nur ein Platzhalter. Er wird ausgefüllt, wenn eine `Box` erstellt wird, entweder explizit oder durch Inferenz:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, aus dem Argument abgeleitet
print(a.value + 1);      // 8, der Compiler weiß, dass value ein int ist
```

Der Buchstabe spielt keine Rolle: `T` ist eine Konvention für „Typ“, nichts weiter.

---

Eine Funktion kann für sich allein generisch sein, ohne in einer generischen Klasse zu leben. Der Typparameter steht zwischen dem Namen und der Parameterliste:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, hier ist T String
print(firstOf([10, 20]));        // 10, hier ist T int
```

Ein Funktionskörper, einmal geprüft, für jeden Typ wiederverwendet. Das Typargument wird normalerweise aus den Argumenten abgeleitet, aber es lässt sich explizit hinschreiben, wenn die Inferenz nichts zum Arbeiten hat:

```dart
final empty = firstOf<String>(<String>[]); // wirft, aber der Typ ist klar
```

Methoden innerhalb einer Klasse folgen genau derselben Regel.

---

Innerhalb einer generischen Klasse ist der Typparameter überall sichtbar: in Feldern, in Konstruktorparametern, in Methodensignaturen und in Methodenkörpern. Er wird einmal deklariert, neben dem Klassennamen, und jedes Mitglied kann ihn verwenden.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

Das Erstellen des Objekts entscheidet über den Typ: `Holder<String>('fig')` macht `item` zu einem `String`, `Holder<int>(3)` macht daraus ein `int`.

---

Eine Klasse kann mehr als einen Typparameter deklarieren, durch Kommas getrennt. `Map<K, V>` ist das eingebaute Beispiel: ein Typ für die Schlüssel, einer für die Werte.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

Die **Reihenfolge** ist Teil des Typs: `Entry<String, int>` und `Entry<int, String>` sind nicht verwandte Typen, und ein Wert des einen kann dem anderen nicht zugewiesen werden. Typparameter lassen sich in einem Rückgabetyp auch umordnen, sodass eine Methode eine gedrehte Version des Objekts zurückgeben kann:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Mit sound null safety kann das Fragezeichen an zwei verschiedenen Stellen landen, und die beiden bedeuten Verschiedenes:

```dart
Box<int?> a = Box(null); // eine Box, die existiert und einen nullable int enthält
Box<int>? b = null;      // gar keine Box, aber falls es eine gibt, enthält sie einen int
```

Bei `Box<int?>` ist das **Typargument** nullable, daher hat `a.value` den Typ `int?` und kann `null` sein, während `a` selbst immer da ist. Bei `Box<int>?` ist die **Variable** nullable, daher kann `b` `null` sein, und du brauchst `b?.value` oder `b!.value`, um in sie hineinzugreifen.

Ein schlichtes `T` bedeutet `T extends Object?`, also ist ein nullable Typargument wie `Box<int?>` völlig legal.

---

Der Unterschied wird wichtig, sobald du den Wert verwendest. Bei einer `Box<int?>` greifst du normal auf das Feld zu und kümmerst dich dann um das `null` darin, während du bei einer `Box<int>?` erst an der fehlenden Box vorbeikommst:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, die Box ist da, ihr Inhalt ist null

Box<int>? b = null;
print(b?.value ?? 0); // 0, die Box selbst fehlt
```

`b.value` auf einer `Box<int>?` zu schreiben kompiliert gar nicht erst: Dart weigert sich, ein Feld von etwas zu lesen, das möglicherweise nicht existiert.

---

Ein unbeschränktes `T` könnte alles sein, daher darfst du innerhalb des Körpers nur verwenden, was jedes Objekt hat. Das kompiliert nicht:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Eine **Bound** behebt das. `T extends num` zu schreiben sagt: „`T` darf nur eine Zahl sein“, und im Austausch darf der Körper alles verwenden, was ein `num` bietet:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

Die Bound wird an der Aufrufstelle geprüft: `half(4)` und `half(2.5)` sind in Ordnung, `half('fig')` ist ein Kompilierfehler. Eine Bound ist ein Versprechen in beide Richtungen: engere Argumente für mehr Möglichkeiten im Inneren.

---

Das Schlüsselwort für eine Bound ist immer `extends`, selbst wenn die Bound ein Interface ist und keine Oberklasse. In einer Typparameterliste gibt es kein `implements`.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Ohne die Bound würde `a > b` nicht kompilieren: Der Vergleichsoperator gehört zu `num`, nicht zu jedem Objekt.

---

Eine Bound kann den Typparameter selbst erwähnen. `Comparable<T>` ist das Interface von allem, was weiß, wie es sich mit seinesgleichen vergleicht, über `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // negativ: fig kommt zuerst
print('kiwi'.compareTo('fig')); // positiv
print('fig'.compareTo('fig'));  // null
```

`T extends Comparable<T>` liest sich also als „jeder Typ, der mit sich selbst verglichen werden kann“, was genau das ist, was eine Sortier- oder Maximumfunktion braucht:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` und `DateTime` erfüllen sie beide direkt. `int` und `double` implementieren `Comparable<num>`, also wird eine Liste von Zahlen einfach als `num` verglichen.

---

Dieselbe Bound funktioniert genauso für das kleinste Element: Nur das Vorzeichen des Vergleichs ändert sich. `compareTo` gibt eine negative Zahl zurück, wenn der Empfänger zuerst kommt, also bedeutet `item.compareTo(best) < 0`: „dieses ist kleiner“.

---

Eine generische Klasse kann benannte und **Factory**-Konstruktoren haben wie jede andere Klasse auch, und der Typparameter ist darin verfügbar. Ein Factory-Konstruktor erstellt das Objekt nicht selbst: Er führt einen Körper aus und gibt eines zurück, sodass er die Instanz beliebig auswählen, wiederverwenden oder bauen kann.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

Das Typargument gehört zur Klasse, nicht zum Namen des Konstruktors: `Box<int>.first(...)`. Innerhalb der Factory ist `<T>[]` eine echte leere `List<T>`, daher ist eine Factory der natürliche Ort, um einen Standardwert für einen Typ zu bauen, den du noch nicht kennst.

---

Ein ohne Bound geschriebener Typparameter ist gar nicht unbeschränkt: `class Box<T>` ist die Kurzform von `class Box<T extends Object?>`. Deshalb wird `Box<int?>` akzeptiert, und deshalb darfst du innerhalb der Klasse nie annehmen, dass `value` nicht-null ist.

Um nullable Typargumente zu verbieten, beschränke den Parameter mit `Object`:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` ist der Typ von allem außer `null`, also liest sich `T extends Object` als „alles, solange es wirklich da ist“.

---

Ein `typedef` gibt einem Typ einen Namen, und es kann eigene Typparameter entgegennehmen. Der übliche Grund: eine Familie von Funktionstypen einmal zu benennen, statt sie bei jeder Verwendung auszuschreiben:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` ist nur eine andere Schreibweise für `int Function(String)`, die beiden sind also austauschbar. Der Gewinn ist Lesbarkeit: Ein als `Transform<I, O> transform` deklarierter Parameter sagt, wofür die Funktion da ist, während `O Function(I)` nur sagt, wie sie aussieht.

Ein generisches typedef und eine generische Funktion lassen sich natürlich kombinieren, wobei die eigenen Typparameter der Funktion die des typedef füllen.
