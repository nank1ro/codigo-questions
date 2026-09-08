Du weißt bereits, wie man eine Funktion mit einem Namen deklariert, z. B. `void sayHello() { ... }`. Dart erlaubt es dir auch, eine Funktion **ohne Namen** zu schreiben: eine **anonyme Funktion**. Sie hat dieselben Bestandteile wie eine benannte Funktion (Parameter in runden Klammern und einen Rumpf in geschweiften Klammern), aber keinen Rückgabetyp und keinen Namen:

```dart
(String name) {
  print('Hello, $name!');
}
```

Da sie keinen Namen hat, ist die übliche Art, sie zu verwenden, sie in einer Variable zu speichern und die Variable dann wie eine Funktion aufzurufen:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Beachte das `;` nach der schließenden geschweiften Klammer: Die Zuweisung ist eine normale Anweisung.

---

Eine anonyme Funktion kann Parameter haben und mit `return` einen Wert zurückgeben, genau wie eine benannte Funktion. Der Rückgabetyp wird nicht hingeschrieben: Dart **leitet** ihn aus den `return`-Anweisungen im Rumpf ab.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Wenn der Rumpf ein einzelner Ausdruck ist, kann eine anonyme Funktion die **Pfeilsyntax** `=>` verwenden, genau wie eine benannte Funktion. Der Pfeil ersetzt die geschweiften Klammern und das Schlüsselwort `return`:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Diese Kurzform ist mit Abstand die häufigste Art, anonyme Funktionen in Dart zu schreiben.

---

Funktionen sind Werte, also haben sie einen Typ. Der Typ einer Funktion wird als **Rückgabetyp**, dann das Schlüsselwort `Function` und dann die **Parametertypen** in runden Klammern geschrieben:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Wenn die Variable auf diese Weise typisiert ist, können die Parametertypen in der anonymen Funktion weggelassen werden, weil Dart sie aus dem deklarierten Typ ableitet:

```dart
int Function(int, int) add = (a, b) => a + b;
```

Der bloße Typ `Function` akzeptiert jede Funktion, egal welche Parameter und welcher Rückgabetyp sie hat, aber er sagt Dart nichts darüber, wie man sie aufruft.

---

Da ein Funktionstyp ein normaler Typ ist, kann eine Funktion **eine andere Funktion als Parameter** nehmen. Im Rumpf wird der Parameter wie jede andere Funktion aufgerufen:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Hier entscheidet der Aufrufer, was `apply` tut, indem er eine anonyme Funktion als zweites Argument übergibt.

---

Viele Methoden von Dart-Sammlungen nehmen eine Funktion als Argument, und anonyme Funktionen sind der natürliche Weg, eine zu übergeben. Die einfachste ist `forEach`, die die übergebene Funktion einmal für jedes Element einer Liste aufruft:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

Der Parametertyp wird aus der Liste abgeleitet, daher ist `fruit` ein `String`, ohne dass man ihn hinschreiben muss.

---

Zwei weitere sehr häufig verwendete Methoden, die eine anonyme Funktion nehmen, sind `map` und `where`:

- `map` transformiert jedes Element mit der Funktion und gibt die neuen Werte zurück
- `where` behält nur die Elemente, für die die Funktion `true` zurückgibt

Beide geben ein lazy `Iterable` zurück; rufe `toList()` auf, um das Ergebnis in eine `List` umzuwandeln:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Da `map` und `where` beide ein `Iterable` zurückgeben, können ihre Aufrufe hintereinander **verkettet** werden. Jeder Schritt erhält das Ergebnis des vorherigen, und `toList()` wird einmal am Ende aufgerufen:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` ordnet eine Liste an Ort und Stelle neu. Standardmäßig verwendet es die natürliche Ordnung der Elemente, aber du kannst eine anonyme Funktion übergeben, die **zwei Elemente vergleicht** und eine negative Zahl, null oder eine positive Zahl zurückgibt. `compareTo` liefert genau eine solche Zahl, daher ist es der übliche Baustein:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Das Vertauschen von `a` und `b` im Vergleich kehrt die Reihenfolge um.

---

`reduce` fasst alle Elemente einer Liste zu einem einzigen Wert zusammen. Seine anonyme Funktion nimmt zwei Parameter: den **bisher akkumulierten Wert** und das **nächste Element**, und gibt den neuen akkumulierten Wert zurück. Das erste Element dient als Startpunkt:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` wirft bei einer leeren Liste einen Fehler, da es kein erstes Element als Startpunkt gibt.

---

Eine Funktion kann auch **eine Funktion zurückgeben**. Der Rückgabetyp ist dann ein Funktionstyp, und der Rumpf gibt eine anonyme Funktion zurück:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Beachte, dass die zurückgegebene Funktion weiterhin `amount` verwendet, einen Parameter von `makeAdder`, sogar noch nachdem `makeAdder` fertig ist. Eine Funktion, die sich die Variablen um sie herum so merkt, heißt **Closure**.

---

Eine Closure liest die Variablen, die sie erfasst, nicht nur: Sie kann sie auch **ändern**, und die Änderungen bleiben zwischen den Aufrufen erhalten. So kann man einen privaten Zustand ohne eine Klasse halten:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Jeder Aufruf von `makeTimer()` erzeugt eine brandneue `seconds`-Variable, daher teilen sich zwei Timer nie ihren Zählerstand.
