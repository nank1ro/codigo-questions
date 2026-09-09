Ein `Future` steht für einen **einzelnen** Wert, der später eintrifft. Ein **Stream** steht für eine **Folge** von Werten, die im Laufe der Zeit eintreffen: Tastendrücke, Teile einer Datei, Nachrichten von einem Server. Jeder Wert heißt **Event**, und nach dem letzten Event ist der Stream **beendet**.

Der einfachste Weg, einen Stream zu bauen, ist `Stream.fromIterable`, das jedes Element einer Liste nacheinander aussendet:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Um die Events einzeln zu konsumieren, verwendest du eine **`await for`**-Schleife. Wie `await` ist sie nur innerhalb einer mit `async` markierten Funktion erlaubt, `main` wird also zu `Future<void> main() async`. Der Schleifenrumpf läuft einmal pro Event, und die Schleife endet, wenn der Stream beendet ist:

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

Eine gewöhnliche `for`-Schleife funktioniert hier nicht: Ein `Stream` ist kein `Iterable`, seine Werte stehen nicht alle auf einmal zur Verfügung.

---

`Stream.fromIterable` braucht alle Werte im Voraus. Um Werte einen nach dem anderen zu **erzeugen**, schreibst du einen **asynchronen Generator**: eine Funktion, deren Rumpf mit `async*` markiert ist und deren Rückgabetyp `Stream<T>` ist. Darin sendet `yield` ein einzelnes Event an den Stream:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

Der Rumpf läuft nicht, wenn du `countTo(3)` aufrufst: Er läuft träge, während der Zuhörer nach Werten fragt, und der Stream ist beendet, wenn der Rumpf zu Ende ist.

Um alle Events in einer `List` zu sammeln, rufst du `toList()` auf. Es liefert ein `Future<List<T>>`, du musst es also mit `await` abwarten:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Eine `await for`-Schleife kann mehr als nur ausgeben: Sie kann eine vor der Schleife deklarierte Variable aktualisieren. Eine Funktion, die einen Stream konsumiert und ein Ergebnis berechnet, muss mit `async` markiert sein und liefert ein `Future` dieses Ergebnisses:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

Die Funktion erreicht das `return` erst, nachdem der Stream beendet ist, der Aufrufer bekommt den Endwert also, wenn er das Future abwartet:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Jeder Stream endet irgendwann. Bei einem `async*`-Generator ist der Stream **beendet**, sobald der Funktionsrumpf zu Ende ist, egal ob er das Ende erreicht hat oder auf ein `return` gestoßen ist. Eine `await for`-Schleife über einen beendeten Stream wird verlassen, und jedes Future von `toList()` wird abgeschlossen.

Ein Stream startet nicht neu und wiederholt seine Werte nicht: Einmal beendet, bleibt er beendet.

---

`await for` pausiert die aktuelle Funktion, bis der Stream beendet ist. Wenn du auf Events reagieren willst, **ohne zu warten**, rufst du `listen` auf und übergibst einen Callback: Er wird einmal pro Event aufgerufen, und der Code nach `listen` läuft sofort weiter.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` akzeptiert außerdem einen benannten Parameter `onDone`, eine Funktion ohne Argumente, die aufgerufen wird, wenn der Stream endet:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Ein `async*`-Generator kann **jedes Event eines anderen Streams** mit `yield*` (yield-star) weiterreichen. Das ist wie eine `await for`-Schleife, die jeden Wert ausgibt, nur in einer Zeile:

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

Der äußere Stream macht mit seinen eigenen `yield`s weiter, sobald der innere Stream beendet ist.

---

Wie `Iterable` hat auch ein `Stream` Methoden, die aus einem bestehenden Stream einen **neuen Stream** bauen:

- `map` transformiert jedes Event
- `where` behält nur die Events, die eine Bedingung erfüllen
- `take` hört nach einer bestimmten Anzahl von Events auf

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Diese Methoden sind **träge**: Nichts läuft, bis jemand den entstehenden Stream abhört. Sie lassen sich verketten, und der Quell-Stream wird nie verändert.

---

Da `where`, `map` und `take` jeweils einen Stream liefern, kannst du sie verketten und mit `toList()` abschließen, um das Ergebnis als Liste zu bekommen. Nur das abschließende `toList()` braucht ein `await`, denn es ist der einzige Aufruf, der ein `Future` liefert:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Neben `toList()` bietet ein Stream weitere Methoden, die alle seine Events **konsumieren** und ein einzelnes `Future` liefern:

- `first` und `last` werden mit dem ersten bzw. letzten Event abgeschlossen
- `length` wird mit der Anzahl der Events abgeschlossen
- `join(separator)` wird mit allen zu einem `String` verbundenen Events abgeschlossen
- `reduce(combine)` verbindet die Events jeweils zu zweit zu einem einzigen Wert

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` ruft `combine` mit dem bisherigen Ergebnis und dem nächsten Event auf. Es wirft eine Exception, wenn der Stream leer ist, verwende es also nur, wenn mindestens ein Event garantiert ist.

---

Die Methoden von `Stream` teilen sich in zwei Gruppen:

- **transformierende** Methoden wie `map`, `where`, `take` und `skip` liefern einen **neuen `Stream`** und sind träge: Kein Event wird verarbeitet, bis der neue Stream abgehört wird
- **konsumierende** Methoden wie `toList`, `reduce`, `join`, `first`, `last` und `length` hören den Stream ab und liefern ein **`Future`** mit dem Endergebnis

Eine Kette besteht daher aus null oder mehr transformierenden Aufrufen, gefolgt von höchstens einem konsumierenden Aufruf.

---

Generatoren erzeugen Events innerhalb einer Funktion. Wenn die Events von **woanders** kommen (einem Button, einem Netzwerk-Callback, einem anderen Objekt), brauchst du einen **`StreamController`**. Er lebt in der Bibliothek `dart:async`, die Datei muss also mit `import 'dart:async';` beginnen.

Ein Controller besitzt einen Stream und lässt dich Events hineinschieben:

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` sendet ein Event
- `close()` beendet den Stream; vergisst du es, warten die Zuhörer für immer
- `stream` ist der `Stream`, den die Zuhörer konsumieren

Events, die hinzugefügt werden, bevor jemand zuhört, werden in einem Puffer aufbewahrt, der Code oben ist also sicher: Ein Zuhörer, der später kommt, bekommt trotzdem `4` und `2`.

---

Ein `StreamController` wird oft an derselben Stelle erzeugt und konsumiert: Du abonnierst `controller.stream` mit `listen`, fügst dann mit `add` Events hinzu und schließt den Controller mit `close`. Da `listen` nicht wartet, werden die Events geliefert, nachdem der aktuelle Code fertig ist, aber immer in der Reihenfolge, in der sie hinzugefügt wurden:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

Die bisher gesehenen Streams sind **Single-Subscription-Streams**: Sie erlauben genau einen Zuhörer. Ein zweiter Aufruf von `listen`, `await for` oder einer konsumierenden Methode wirft einen `StateError` ("Stream has already been listened to").

Um einen Stream unter mehreren Zuhörern zu teilen, wandle ihn mit `asBroadcastStream()` in einen **Broadcast**-Stream um:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Ein Broadcast-Stream puffert nicht: Ein Zuhörer bekommt nur die Events, die **nach** seinem Abonnement gesendet werden. Im Beispiel abonnieren beide Zuhörer vor dem ersten `await`, also bekommen beide jedes Event.

---

Ein Controller kann mit dem benannten Konstruktor `StreamController<T>.broadcast()` direkt einen Broadcast-Stream erzeugen. Sein `stream` akzeptiert beliebig viele Zuhörer, und jedes Event wird an alle geliefert, in der Reihenfolge ihres Abonnements:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

Wie jeder Broadcast-Stream puffert er nicht: Events, die hinzugefügt werden, bevor ein Zuhörer abonniert, sind für diesen Zuhörer verloren.

---

Ein Stream kann neben Werten auch **Fehler** transportieren. Innerhalb eines `async*`-Generators sendet ein `throw` ein Fehler-Event und beendet den Stream; ein `StreamController` kann eines mit `addError` senden.

Auf der konsumierenden Seite wirft eine `await for`-Schleife den Fehler dort erneut, wo die Schleife steht, du behandelst ihn also mit einem gewöhnlichen `try`/`catch` um die Schleife herum:

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

Bei `listen` übergibst du stattdessen einen `onError`-Callback: `stream.listen(print, onError: (e) => print('caught: $e'));`
