Eine **Methode höherer Ordnung** ist eine Methode, die eine Funktion als Argument entgegennimmt. Dart-Collections bieten viele davon, und die Funktion, die du übergibst, ist meist eine anonyme Funktion, geschrieben mit der Pfeil-Syntax `(x) => ...`.

`map` ist die häufigste davon: Sie ruft die Funktion für jedes Element auf und erzeugt die Ergebnisse, eines pro Element, und lässt die ursprüngliche Collection unverändert:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Beachte die **runden Klammern** in der Ausgabe. `map` gibt keine `List` zurück: Es gibt ein `Iterable` zurück, eine Sequenz, die du durchlaufen kannst. Um eine echte Liste zurückzubekommen, rufe **`toList()`** darauf auf:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Eckige Klammern in der Ausgabe zeigen dir, dass du eine `List` vor dir hast, runde Klammern, dass du ein einfaches `Iterable` vor dir hast.

---

`where` nimmt eine Funktion, die ein `bool` zurückgibt – ein sogenanntes **Prädikat** – und behält nur die Elemente, für die sie `true` liefert. Die Reihenfolge der übrig bleibenden Elemente ändert sich nie:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Wie `map` gibt auch `where` ein `Iterable` zurück und verändert die ursprüngliche Collection nie, daher ist `toList()` wieder das, was das Ergebnis in eine `List` verwandelt.

In anderen Sprachen heißt diese Methode `filter`; in Dart heißt sie `where`.

---

Die Funktion, die an `map` übergeben wird, muss nicht denselben Typ zurückgeben wie die Elemente, die sie erhält. Das Abbilden einer Liste von Strings auf ihre Längen verwandelt eine `List<String>` in ein `Iterable<int>`, aus dem `toList()` dann eine `List<int>` macht:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

Das Ergebnis hat immer **genau so viele Elemente wie das Original**, in derselben Reihenfolge: `map` transformiert Elemente, es fügt nie welche hinzu oder entfernt welche.

---

Einige Methoden höherer Ordnung beantworten eine Frage über die Collection, statt eine neue zu erstellen. Sie nehmen ein Prädikat entgegen und geben ein `bool` zurück:

- `any` ist `true`, wenn **mindestens ein** Element das Prädikat erfüllt
- `every` ist `true`, wenn **alle** Elemente es erfüllen

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Beide brechen ab, sobald die Antwort feststeht: `any` beim ersten Element, das passt, `every` beim ersten, das nicht passt.

Auf einer leeren Collection ist `any` `false` und `every` ist `true`: Es gibt kein Element, das das erste belegt, und keines, das das zweite widerlegt.

---

`map` und `where` sind **lazy**: Beim Aufrufen passiert nichts. Sie geben ein `Iterable` zurück, das sich die Quelle und die Funktion merkt, und die Funktion wird erst aufgerufen, wenn jemand das Ergebnis durchläuft, ein Element nach dem anderen.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // noch nichts berechnet
print(doubled.first);                      // berechnet nur 2
```

`toList()` ist das, was die Sequenz **materialisiert**: Es durchläuft sie von Anfang bis Ende und speichert jedes Ergebnis in einer echten `List`.

Laziness hat zwei Konsequenzen, die man sich merken sollte. Ein lazy `Iterable` wird jedes Mal neu berechnet, wenn du es iterierst, daher ist es günstiger, einmal mit `toList()` zu materialisieren, wenn du die Werte mehr als einmal brauchst. Und es schaut weiterhin auf die ursprüngliche Collection, sodass eine Änderung dieser Collection ändert, was das `Iterable` erzeugt:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` kombiniert eine ganze Collection zu einem **einzelnen Wert**. Es nimmt zwei Argumente: den Startwert des **Akkumulators** und eine Funktion, die den bisherigen Akkumulator und das nächste Element erhält und den neuen Akkumulator zurückgibt:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Hier startet `acc` bei `0`, wird dann `1`, `3`, `6` und schließlich `10`.

Der Akkumulator muss keine Zahl sein und nicht denselben Typ wie die Elemente haben: Wenn du bei `''` startest und Text hinzufügst, baust du aus einer Liste beliebiger Elemente einen `String`.

Ein Detail, das du beachten solltest: Dart leitet den Akkumulator-Typ aus dem Startwert **und** daraus ab, wo das Ergebnis verwendet wird. Innerhalb von `print(...)` ist der erwartete Typ unbekannt, speichere das Ergebnis also zuerst in einer Variable (oder schreibe `fold<int>(...)`), sonst beklagt sich der Compiler, dass er `+` nicht auf den Akkumulator anwenden kann.

---

`reduce` ist der kürzere Verwandte von `fold`. Es nimmt keinen Startwert: Das **erste Element** ist der Start-Akkumulator, und die Funktion läuft für jedes übrige Element:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Da es keinen Startwert gibt, hat das Ergebnis immer **denselben Typ wie die Elemente**, und der Aufruf von `reduce` auf einer leeren Collection wirft einen `StateError`: Es gibt kein erstes Element als Startpunkt. `fold` hat dieses Problem nicht, weshalb es die sicherere Standardwahl ist.

`reduce` ist am besten, wenn du ein Element unter vielen suchst, zum Beispiel das größte:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` gibt das **erste** Element zurück, das ein Prädikat erfüllt, anstatt alle:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Wenn nichts passt, gibt es kein Element zurückzugeben, also wirft `firstWhere` einen `StateError`. Um eine Antwort statt eines Fehlers zu bekommen, übergib das benannte Argument **`orElse`**: eine Funktion ohne Parameter, die den Ersatzwert erzeugt.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` ist eine Funktion, kein einfacher Wert, daher wird sie nur aufgerufen, wenn die Suche fehlschlägt. `orElse: 'none'` zu schreiben kompiliert nicht.

---

Wenn die Funktion, die du an `map` gibst, für jedes Element eine Collection zurückgibt, erhältst du am Ende eine Sequenz von Collections. **`expand`** macht dieselbe Arbeit, fügt aber danach alle zu einer flachen Sequenz zusammen:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

Die Reihenfolge bleibt erhalten: Alles, was das erste Element erzeugt, kommt zuerst, dann alles, was das zweite erzeugt, und so weiter.

Da die zurückgegebene Collection beliebig groß sein kann, ist `expand` auch der Weg, um **mehr oder weniger** Elemente zu erzeugen, als du am Anfang hattest: Für ein Element eine leere Liste zurückzugeben, lässt es einfach weg.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` behält die **ersten** `n` Elemente und `skip(n)` wirft sie weg. Keins von beiden nimmt eine Funktion entgegen, aber beide geben ein lazy `Iterable` zurück, sodass sie natürlich zwischen die anderen Methoden höherer Ordnung passen:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Mehr Elemente anzufordern, als vorhanden sind, ist kein Fehler: Du bekommst einfach das, was existiert, oder ein leeres Ergebnis.

`takeWhile` und `skipWhile` sind die Versionen mit einem Prädikat. Sie nehmen oder verwerfen Elemente vom Anfang **solange** das Prädikat erfüllt ist, und stoppen beim ersten Element, das es nicht erfüllt, selbst wenn spätere wieder passen würden:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart hat keine `sorted`-Methode. `sort` gehört zu `List`, es ordnet die Liste **in place** um und gibt nichts zurück:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Weil es `void` zurückgibt, kannst du das Ergebnis gar nicht verwenden: `final sorted = numbers.sort();` liefert einen Wert, den der Compiler dich nicht lesen lässt. Das Idiom für eine geordnete **Kopie** ist `toList()` gefolgt vom Cascade `..sort()`: `toList()` erzeugt die Kopie, und `..` führt `sort` darauf aus, während es trotzdem die Kopie selbst zurückgibt.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], unverändert
```

`sort` akzeptiert auch einen **Comparator**: eine Funktion mit zwei Elementen, die eine negative Zahl zurückgibt, wenn das erste vor dem zweiten kommt, `0`, wenn sie gleich sind, und sonst eine positive Zahl. `compareTo` erzeugt genau das, daher ist das Ordnen nach einem beliebigen Schlüssel ein Einzeiler:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` und `reduce` sehen ähnlich aus, und die Wahl zwischen ihnen läuft auf zwei Fragen hinaus: Kann die Collection leer sein, und hat das Ergebnis denselben Typ wie die Elemente?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String aus Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int aus Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` kann immer nur einen Element-Typ zurückgeben, weil es bei einem Element startet. `fold` startet bei einem Wert deiner Wahl, daher kann der Akkumulator ein `int` sein, der zählt, ein `String`, der wächst, oder sogar eine `List`, die aufgebaut wird. Und da dieser Startwert bereits existiert, ist eine leere Collection einfach die Antwort, die `fold` unverändert zurückgibt, während `reduce` nichts zurückzugeben hat und wirft.

---

Jede dieser Methoden gibt ein `Iterable` zurück, und jedes `Iterable` hat dieselben Methoden wieder. Genau das ermöglicht **Verkettung**: Eine ganze Berechnung liest sich als Pipeline von links nach rechts, wobei jeder Schritt mit dem arbeitet, was der vorherige erzeugt hat.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Nur der letzte Schritt braucht `toList()`: Ruft man es in der Mitte auf, baut man eine Liste, die niemand behält.

Der Typ ändert sich entlang der Kette, und damit auch das, was die nächste Funktion erhält: Nach `where` auf einer `List<String>` hast du immer noch Strings, aber nach `map((w) => w.length)` sieht der nächste Schritt Zahlen.

Da jeder Schritt lazy ist, kommt es bei der erledigten Arbeit auf die Reihenfolge an, nicht nur beim Ergebnis: Erst mit `where` zu filtern bedeutet, dass `map` auf weniger Elementen aufgerufen wird.

---

Nichts an diesen Methoden ist besonders: Sie haben einfach eine **Funktion als Parameter**, und deine eigenen Funktionen können dasselbe tun. Der Typ eines Funktionsparameters wird als Rückgabetyp geschrieben, dann `Function`, dann die Parametertypen in Klammern:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

Der Aufrufer entscheidet, **was** passiert, die Funktion entscheidet, **worauf**. Beachte, wie `operation` direkt an `map` übergeben wird: Ein Funktionswert kann wie jeder andere Wert weitergegeben werden.

Das Argument kann eine anonyme Funktion sein oder der **Name** einer bestehenden, geschrieben ohne Klammern. Mit Klammern würde man sie aufrufen, statt sie zu übergeben:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Eine Funktion kann auch eine Funktion **zurückgeben**. Der Rückgabetyp wird genau wie ein Funktionsparameter-Typ geschrieben, und der zurückgegebene Wert ist meist eine anonyme Funktion:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` multipliziert nichts: Sie baut eine neue Funktion, die mit `3` multipliziert, und gibt diese zurück. Diese Funktion wird dann gespeichert, aufgerufen oder wie jede andere an `map` übergeben:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

Die zurückgegebene Funktion merkt sich `factor` auch dann noch, wenn `multiplier` längst fertig ist. Eine Funktion, die die Variablen des Scopes behält, in dem sie erstellt wurde, heißt **Closure**, und sie ist es, die Funktionsfabriken wie diese erst möglich macht.

---

Zusammengenommen ersetzen diese Methoden die meisten handgeschriebenen Schleifen. Eine Pipeline liest sich meist in drei Stufen: **Wähle** die Elemente mit `where` aus, **transformiere** sie mit `map`, dann **kombiniere** sie mit `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Weil `fold` seinen eigenen Startwert wählt, kann es eine Kette auch mit einem Typ abschließen, der nichts mit den Elementen zu tun hat, etwa einem `String`, der Stück für Stück gewachsen ist:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Jede Stufe bleibt kurz und sagt, was sie tut – das ist der eigentliche Grund, sie einer Schleife vorzuziehen, die alle drei auf einmal erledigt.
