In Dart ist eine **Liste** eine geordnete Sammlung von Elementen. Die einfachste Möglichkeit, eine Liste zu erstellen, ist die `[]`-Literalsyntax:

```dart
List<int> numbers = [1, 2, 3];
```

Du kannst auch Typinferenz mit `var` verwenden:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

Die Typannotation `List<String>` teilt Dart mit, dass jedes Element in der Liste ein `String` sein muss.

---

Listen in Dart sind **nullbasiert indiziert**, d. h. das erste Element befindet sich an Index `0`, das zweite an Index `1` usw.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

Der Zugriff auf ein Element per Index erfolgt mit der Syntax `list[index]`.

---

Die Methode `.add()` fügt ein einzelnes Element am **Ende** einer Liste hinzu:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Beachte, dass `.add()` die Liste **direkt** verändert und `void` zurückgibt.

---

Die Eigenschaft `.length` gibt die Anzahl der Elemente in einer Liste zurück:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Eine leere Liste hat die Länge `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

Die Methode `.contains()` prüft, ob eine Liste einen bestimmten Wert enthält. Sie gibt `true` zurück, wenn er gefunden wird, andernfalls `false`:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Dies ist nützlich für Zugehörigkeitsprüfungen ohne Schleife.
