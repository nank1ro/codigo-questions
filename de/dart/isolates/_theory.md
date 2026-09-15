Jede Zeile Dart, die du bisher geschrieben hast, läuft in einem **Isolate**: einem Thread mit eigenem Speicher und eigener Event-Loop. Ein Programm startet mit einem Isolate, dem *Main*-Isolate, und kann weitere starten.

Was Isolates besonders macht, ist, dass sie **nichts** teilen. Zwei Isolates sehen nie dasselbe Objekt, daher gibt es keine Sperren, keine Data Races und keinen halb aktualisierten Wert. Sie kommunizieren nur, indem sie **Kopien** von Nachrichten übergeben.

Der kürzeste Weg, ein zweites Isolate zu verwenden, ist **`Isolate.run`**: Es nimmt eine Funktion entgegen, führt sie in einem brandneuen Isolate aus und liefert dir ein `Future` mit ihrem Ergebnis:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` lebt in der `dart:isolate`-Bibliothek, daher muss die Datei mit `import 'dart:isolate';` beginnen. Während das neue Isolate rechnet, bleibt das Main-Isolate frei: Das ist echte **Parallelität**, die Arbeit passiert auf einem anderen Prozessorkern.

---

Die Funktion, die du an `Isolate.run` übergibst, darf Variablen aus ihrer Umgebung **einfangen**. Diese Werte werden zusammen mit der Funktion in das neue Isolate kopiert, sodass die Berechnung von ihrem Aufrufer abhängen kann:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` liefert ein `Future` mit dem, was die Funktion zurückgibt, daher kann `triple` es einfach weiterreichen: `async` und `await` sind nicht nötig, wenn du das Future nur weitergibst.

Der Sinn davon, Arbeit in ein anderes Isolate zu verlagern, ist, dass lange Berechnungen das Main-Isolate nicht mehr einfrieren. Eine Schleife, die eine Sekunde läuft, blockiert alles, wenn sie im Main-Isolate läuft; innerhalb von `Isolate.run` läuft sie woanders, und das Main-Isolate behandelt weiter seine eigenen Events.

---

Zwischen Isolates werden nur **Daten** kopiert, nicht **Code**. Jedes Isolate eines Programms kann bereits alle Top-Level-Funktionen und -Klassen dieses Programms sehen, daher darf die Berechnung, die an `Isolate.run` übergeben wird, sie frei aufrufen:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

Unterwegs ist der eingefangene `text` auf dem Hinweg und das resultierende `int` auf dem Rückweg, jeweils eine Kopie. Das Muster ist immer dasselbe: Lass die schwere Funktion, wo sie ist, und verpacke den **Aufruf** in `Isolate.run`.

---

`await` und `Isolate.run` lösen zwei verschiedene Probleme, und es lohnt sich, sie auseinanderzuhalten.

`await` liefert dir **Nebenläufigkeit** auf einem einzelnen Isolate: Während eine Funktion auf einen Timer oder einen Server wartet, führt das Isolate anderen anstehenden Code aus. Nichts läuft zum selben Zeitpunkt, das Isolate hört nur auf, untätig zu sein. Das ist das richtige Werkzeug zum Warten.

`Isolate.run` liefert dir **Parallelität**: ein zweites Isolate auf einem zweiten Prozessorkern, das seinen eigenen Code zum selben Zeitpunkt wie das erste ausführt. Das ist das richtige Werkzeug zum Rechnen.

```dart
await Future.delayed(const Duration(seconds: 1)); // wartet: kein Kern ist beschäftigt
await Isolate.run(() => hugeCalculation());       // wird berechnet: ein anderer Kern ist beschäftigt
```

Eine langsame Berechnung zu awaiten hilft überhaupt nicht: `await bigSum()` führt `bigSum` weiterhin im aktuellen Isolate aus und blockiert es bis zur letzten Zeile. Nur ein zweites Isolate verlagert diese Arbeit weg.

---

`Isolate.run` ist die Abkürzung für ein einzelnes Ergebnis. Wenn du ein Isolate willst, das weiterläuft und sich mehr als einmal zurückmeldet, startest du es selbst mit **`Isolate.spawn`** und gibst ihm eine Möglichkeit zu antworten.

Diese Möglichkeit ist ein Paar von Ports. Ein **`ReceivePort`** ist ein Briefkasten: Du erstellst ihn auf deiner Seite und liest die Nachrichten, die ankommen. Sein **`sendPort`** ist die Adresse dieses Briefkastens, und er ist das Einzige, was das andere Isolate braucht, um zu antworten.

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` nimmt die auszuführende Funktion und die einzelne Nachricht, die ihr übergeben wird, hier den `SendPort`. Auf der anderen Seite wirft `send` einen Wert in den Briefkasten, und `await receivePort.first` wartet auf die erste Nachricht und schließt den Port.

---

Die Funktion, die an `Isolate.spawn` übergeben wird, heißt **Einstiegspunkt**. Sie muss eine Top-Level-Funktion (oder statische Funktion) sein, die genau einen Parameter entgegennimmt: die Nachricht, die `Isolate.spawn` ihr übergibt.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

Die Nachrichten, die in einem `ReceivePort` ankommen, haben den statischen Typ `dynamic`, weil jeder Wert gesendet worden sein könnte. Wenn du weißt, was das andere Isolate sendet, castest du sie:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Ein gestartetes Isolate folgt immer denselben vier Schritten: den Briefkasten öffnen, den Worker mit seiner Adresse starten, auf die Antwort warten, sie verwenden.

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

Das `await` vor `Isolate.spawn` wartet darauf, dass das Isolate *startet*, nicht darauf, dass es seine Arbeit beendet: Das Ergebnis kommt später über den Port.

---

`Isolate.spawn` übergibt genau **eine** Nachricht an den Einstiegspunkt, und der Worker braucht normalerweise sowohl einen `SendPort` zum Antworten als auch einige Daten zum Arbeiten. Der übliche Trick ist, alles in eine `List` zu packen und sie auf der anderen Seite auszupacken:

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

Die Liste wird auf dem Hinweg kopiert, daher liest der Worker seine eigenen Werte. Ein `SendPort` ist eines der wenigen Dinge, die nicht kopiert, sondern geteilt werden: Er zeigt weiterhin auf den Briefkasten des Isolates, das ihn erstellt hat, und genau deshalb kann er als Rücksendeadresse verwendet werden.

---

`first` liest eine Nachricht und schließt den Briefkasten. Ein `ReceivePort` ist auch ein **`Stream`**, daher iterierst du zum Lesen vieler Nachrichten mit `await for` darüber.

Die Schleife endet nie von selbst: Der Port bleibt offen und wartet auf eine Nachricht, die vielleicht nie kommt. Der Worker sendet daher einen letzten Wert als Signal, oft `null`, und der Listener reagiert, indem er **`close()`** aufruft, was den Stream und die Schleife beendet:

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

Das Einsammeln einer ganzen Reihe von Nachrichten folgt einem Rezept: eine leere Liste vor der Schleife, ein `add` pro echter Nachricht und `close()` bei dem Signal, das den Stream beendet. Sobald der Port geschlossen ist, endet das `await for`, und die Funktion kann zurückkehren:

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

Nachrichten behalten die Reihenfolge, in der sie gesendet wurden, daher spiegelt die Liste, die du baust, die Arbeit des anderen Isolates Schritt für Schritt wider.

---

Ein offener `ReceivePort` zählt als anstehende Arbeit: Solange einer existiert, hat das Isolate, das ihn besitzt, einen Grund, am Leben zu bleiben, und seine Event-Loop wartet weiter auf eine Nachricht. In einem Kommandozeilenprogramm beendet sich ein Main-Isolate mit offenem Port einfach **nie**, und du musst es von Hand stoppen.

Den Port zu schließen ist daher Teil der Aufgabe, keine Optimierung:

- `await port.first` schließt ihn für dich nach einer Nachricht
- `port.close()` schließt ihn explizit, was du nach einer `await for`-Schleife brauchst

Bei `Isolate.run` entfällt all diese Buchhaltung: Es erstellt die Ports, schließt sie und fährt das Isolate für dich herunter. Bevorzuge es, wann immer ein Ergebnis alles ist, was du brauchst.

---

Eine Ausnahme, die innerhalb eines Isolates geworfen wird, kann nicht zu einem anderen hinüberspringen: Beide haben getrennte Stacks. `Isolate.run` überbrückt diese Lücke für dich, indem es den Fehler abfängt, ihn zurückkopiert und das zurückgegebene Future mit ihm fehlschlagen lässt. Auf deiner Seite ist er daher ein gewöhnlicher asynchroner Fehler, gefangen mit `try`/`catch` um das `await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

Das `await` innerhalb des `try` ist wichtig, genau wie bei jedem anderen Future auch: Ohne es würde das Future den `try`-Block unvollendet verlassen, und das `catch` würde nie laufen.

Bei `Isolate.spawn` gibt es keine solche Brücke. Ein unbehandelter Fehler beendet das gestartete Isolate still, und das Elternteil wartet weiter auf eine Nachricht, die nie ankommen wird — ein Grund mehr, zuerst zu `Isolate.run` zu greifen.

---

Der Fehler, der von `Isolate.run` zurückkommt, ist eine **Kopie** des auf der anderen Seite geworfenen, daher funktionieren die üblichen Prüfungen weiterhin: `catch (e)` gibt dir das Objekt, und `e is FormatException` sagt dir, welche Art von Fehler es war.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

Worauf du dich nicht verlassen kannst, ist der Stacktrace, der in dein eigenes Isolate zeigt: Der Fehler ist gereist, der Stack nicht.

---

Zusammengesetzt liest sich ein `Isolate.run`-Programm wie gewöhnlicher sequenzieller Code: Die Zeile vor dem Aufruf läuft im Main-Isolate, die Berechnung läuft woanders, und die Zeile nach dem `await` läuft wieder im Main-Isolate, mit dem Ergebnis in der Hand.

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

Da Isolates keinen Speicher teilen, wird jede Nachricht beim Überqueren **kopiert**. Zahlen, Booleans, Strings, `null`, Listen, Maps und die meisten einfachen Objekte können die Reise machen; ein paar Dinge können gar nicht kopiert werden, etwa ein offener Socket, und der Versuch, eines zu senden, wirft einen `ArgumentError`.

Die Konsequenz ist die Regel, die Isolates sicher macht: Nach dem Senden halten beide Seiten **zwei unabhängige Objekte**. Was auch immer ein Isolate mit seiner Kopie macht, ist für das andere unsichtbar.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // die Kopie wächst
print(numbers);                           // [1, 2, 3]
```

`SendPort` ist die Ausnahme, die die Regel bestätigt: Er wird geteilt statt kopiert, gerade damit er weiterhin auf den ursprünglichen Briefkasten zeigen kann.

---

Jedes `Isolate.run` startet sein eigenes Isolate, daher laufen mehrere davon wirklich zum selben Zeitpunkt, auf so vielen Kernen wie die Maschine hat. Das Muster kennst du bereits von Futures: Starte zuerst jede Berechnung, und warte dann mit `Future.wait` auf alle, was die Ergebnisse in der Reihenfolge der Eingabe behält.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Ein Isolate zu starten ist nicht kostenlos: Es kostet Speicher und ein paar Millisekunden. Eine lange Berechnung auf eine Handvoll Isolates aufzuteilen lohnt sich, tausend triviale Additionen an tausend Isolates zu senden nicht.
