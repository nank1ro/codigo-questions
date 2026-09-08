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
