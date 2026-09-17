Eine **Map** ist eine Sammlung von **Schlüssel-Wert-Paaren**: Jeder Wert wird unter einem eindeutigen Schlüssel gespeichert, und du verwendest den Schlüssel, um den Wert wiederzufinden. Eine Map wird mit der `{}`-Literalsyntax erstellt, wobei jedes Paar als `key: value` geschrieben wird:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

Die Typannotation `Map<String, int>` teilt Dart mit, dass jeder Schlüssel ein `String` und jeder Wert ein `int` ist. Wie bei Listen leitet `var` den Typ aus dem Literal ab:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Um einen Wert zu lesen, verwendest du den Schlüssel in eckigen Klammern, genau wie einen Index in einer Liste:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Wenn der Schlüssel nicht in der Map ist, wirft der Zugriff **keinen** Fehler: Er gibt `null` zurück. Aus diesem Grund ist der Typ von `ages['Ann']` `int?` (ein nullable `int`), nicht `int`:

```dart
print(ages['Zed']); // null
```

---

Eine Zuweisung mit `map[key] = value` **fügt** entweder ein neues Paar **hinzu**, wenn der Schlüssel noch nicht in der Map ist, oder **aktualisiert** den Wert, der unter einem vorhandenen Schlüssel gespeichert ist:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // fügt Bob hinzu
ages['Ann'] = 31; // aktualisiert Ann
print(ages); // {Ann: 31, Bob: 25}
```

Neue Schlüssel werden nach den vorhandenen angehängt, sodass sich eine Map die Einfügereihenfolge merkt.

---

Die Methode `.remove(key)` löscht einen Schlüssel und seinen Wert aus der Map. Sie gibt den entfernten Wert zurück, oder `null`, wenn der Schlüssel nicht vorhanden war:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

Die Eigenschaft `.length` gibt die Anzahl der Schlüssel-Wert-Paare zurück:

```dart
print(ages.length); // 1
```

---

Um zu prüfen, ob eine Map einen bestimmten Schlüssel enthält, verwendest du `.containsKey(key)`. Um zu prüfen, ob irgendein Paar einen bestimmten Wert speichert, verwendest du `.containsValue(value)`. Beide geben einen `bool` zurück:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Das Lesen eines fehlenden Schlüssels wirft nie einen Fehler, also solltest du immer daran denken, dass ein Zugriff dir `null` liefern kann. Ein sicheres Muster ist, mit dem `??`-Operator einen Fallback bereitzustellen:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

Die Eigenschaft `.keys` liefert alle Schlüssel einer Map und `.values` liefert alle Werte, in Einfügereihenfolge. Es sind träge `Iterable`s, also rufe `.toList()` auf, wenn du eine echte `List` brauchst:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```

---

Eine leere Map-Literal `{}` hat keine Paare, aus denen die Typen abgeleitet werden könnten, also gib ihr explizite Typen mit `<K, V>{}` oder mit einer Typannotation:

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

Die Eigenschaft `.isEmpty` ist `true`, wenn eine Map keine Paare hat, und `.isNotEmpty` ist `true`, wenn sie mindestens eines hat:

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

Die Methode `.forEach()` führt eine Funktion einmal für jedes Paar aus. Die Funktion erhält zwei Parameter: den Schlüssel und den Wert:

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

Eine Map ist kein `Iterable`, daher kannst du nicht direkt mit `for-in` darüber iterieren. Iteriere stattdessen über `.entries`: Jedes Element ist ein `MapEntry` mit einem `.key` und einem `.value`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

Die Methode `.putIfAbsent(key, ifAbsent)` fügt ein Paar **nur dann** hinzu, wenn der Schlüssel noch nicht in der Map ist. Das zweite Argument ist eine Funktion, die den Wert erzeugt. Wenn der Schlüssel bereits existiert, bleibt die Map unverändert. In beiden Fällen wird der jetzt unter dem Schlüssel gespeicherte Wert zurückgegeben:

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Ann ist bereits vorhanden, nichts ändert sich
ages.putIfAbsent('Bob', () => 25); // Bob wird hinzugefügt
print(ages); // {Ann: 30, Bob: 25}
```

---

Die Methode `.update(key, update)` ersetzt den Wert eines vorhandenen Schlüssels. Das zweite Argument ist eine Funktion, die den aktuellen Wert erhält und den neuen zurückgibt. Wenn der Schlüssel fehlt, wirft `.update()` einen Fehler, es sei denn, du übergibst eine `ifAbsent`-Funktion, die den Anfangswert erzeugt:

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // apple wird 4
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwi wird mit 1 hinzugefügt
print(stock); // {apple: 4, kiwi: 1}
```
