Manche Anweisungen lassen sich nicht ausführen: einen Text lesen, der keine Zahl ist, hinter das Ende einer Liste greifen, das erste Element einer leeren Liste anfordern. Wenn das passiert, **wirft** Dart ein Objekt, das den Fehler beschreibt.

Eine solche Ausnahme kannst du selbst mit dem Schlüsselwort `throw` werfen. `Exception('message')` erzeugt ein fertiges Objekt mit einer kurzen Erklärung:

```dart
throw Exception('no fuel');
```

Ein `throw` ist kein `return`. Er verlässt die Anweisung, die Funktion und jeden Aufrufer darüber und sucht nach etwas, das die Ausnahme behandelt. Wenn nichts sie behandelt, stoppt das Programm und gibt den Fehler aus:

```
Unhandled exception:
Exception: no fuel
```

Alles nach dem `throw` wird übersprungen, daher werden die Zeilen, die sonst laufen würden, nie ausgeführt. Genau darum geht es in diesem Thema: zu entscheiden, wo ein Fehler behandelt wird, statt ihn das Programm beenden zu lassen.

---

Um das Programm am Leben zu halten, packst du die riskante Anweisung in einen `try`-Block und beschreibst die Wiederherstellung in einem `catch`-Block:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` wirft eine Ausnahme, wenn der Text keine ganze Zahl beschreibt. Dart verlässt den `try`-Block bei der ersten Anweisung, die wirft, überspringt den Rest, führt den `catch`-Block aus und macht dann mit dem folgenden Code weiter. Die Variable in den Klammern, hier `e`, ist das geworfene Objekt selbst.

Nichts innerhalb des `try`-Blocks wird rückgängig gemacht, halte ihn also so kurz wie den Fehler, den du erwartest.

---

Ein bloßes `catch` fängt alles, versteckt damit aber auch die Fehler, mit denen du nicht gerechnet hast. Um genau eine Art zu behandeln, nennst du ihren Typ in einer `on`-Klausel:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` wirft eine **`FormatException`**, wenn der Text keine ganze Zahl ist, das ist also der Typ, den du beim Einlesen von Eingaben nennst. Eine `on`-Klausel passt zu diesem Typ und seinen Subtypen, und zu nichts anderem: Jeder andere Fehler reist weiter nach außen und zeigt sich weiterhin, statt von einer Wiederherstellung verschluckt zu werden, die nie für ihn gedacht war.

---

Auf einen `try`-Block können **mehrere** Klauseln folgen, die jeweils von einem anderen Fehler wiederherstellen. Dart vergleicht das geworfene Objekt von oben nach unten damit und führt die **erste** passende Klausel aus:

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

Das Lesen einer Liste mit einem Index, der nicht existiert, wirft einen **`RangeError`**, daher bekommen die zwei Fehler dieser einen Zeile unterschiedliche Antworten.

Da der erste Treffer gewinnt, ist die Reihenfolge wichtig: Eine Klausel für einen allgemeinen Typ über einer spezielleren würde immer gewinnen und die spezielle Klausel unerreichbar machen. Schreibe die speziellen Klauseln zuerst und ein bloßes `catch` ans Ende, wenn du ein Sicherheitsnetz willst.

Die `on RangeError`-Klausel oben dient nur dazu zu zeigen, wie mehrere Klauseln geordnet werden. Ein `RangeError` signalisiert einen Fehler im Code und keine Bedingung, die das Programm nicht kontrollieren konnte; eine spätere Übung erklärt, warum man einen solchen Fehler verhindern statt abfangen sollte.

---

Oft braucht die Wiederherstellung das geworfene Objekt gar nicht: Der Typ sagt bereits alles. In dem Fall lässt du den `catch`-Teil weg und behältst nur die `on`-Klausel:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

Die beiden Formen unterscheiden sich nur darin, ob du eine Variable bekommst:

- `on FormatException catch (e)` — passt zu diesem Typ und gibt dir das Objekt als `e`
- `on FormatException` — passt zu diesem Typ, ohne Variable
- `catch (e)` — passt zu allem und gibt dir das Objekt

Eine unbenutzte Variable wegzulassen hält den Handler ehrlich darin, was er wirklich verwendet.

---

Auf die Handler kann ein dritter Block folgen. `finally` läuft **in jedem Fall**: nachdem der `try`-Block normal beendet wurde, nachdem ein Handler wiederhergestellt hat und auch dann, wenn nichts gepasst hat und der Fehler noch nach außen reist.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Er läuft sogar, bevor ein `return` seinen Wert zurückgibt, deshalb wird die Nachricht oben ausgegeben, bevor der Aufrufer das Ergebnis sieht. Das macht `finally` zum Ort für Arbeit, die in jedem Fall passieren muss, etwa zum Schließen von dem, was du geöffnet hast.

---

Dein eigener Code wirft auf dieselbe Weise wie die Bibliothek. `Exception('message')` erzeugt eine simple Ausnahme mit einer kurzen Erklärung, und `throw` schickt sie auf den Weg:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

Die Nachricht geht nicht verloren: `toString()` setzt das Wort `Exception`, einen Doppelpunkt und die Nachricht zusammen, und genau das gibt der Bericht über unbehandelte Ausnahmen aus.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Werfen ist besser, als einen ausgedachten Wert wie `-1` zurückzugeben: Der Aufrufer kann nicht vergessen hinzusehen, und der Grund reist mit.

---

Manchmal ist ein Handler nicht der richtige Ort, um wiederherzustellen: Du willst den Fehler nur *bemerken* und ihn zu dem Aufrufer weiterziehen lassen, der sich tatsächlich darum kümmern kann. Das Schlüsselwort `rethrow` macht das, innerhalb eines `catch`- oder `on ... catch`-Blocks:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` schickt **dasselbe** Objekt weiter, daher sieht der Aufrufer den ursprünglichen Fehler. `throw e` zu schreiben würde auch funktionieren, aber es startet die Reise neu und verliert, wo der Fehler zuerst passiert ist.

Ein `finally`-Block in derselben Anweisung läuft trotzdem, auch auf dem Weg nach draußen.

---

Eine `catch`-Klausel akzeptiert einen **zweiten** Parameter:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

Der erste ist das geworfene Objekt, der zweite ist ein `StackTrace`: die Kette der Aufrufe, die im Moment des Wurfs liefen. Er beantwortet, *woher* der Fehler kam, was die Nachricht allein selten tut.

Ein Stack Trace listet Dateinamen, Zeilennummern und Frames auf, und er ändert sich mit dem Build und dem Aufrufpfad. Gib ihn aus, hänge ihn an einen Bericht an, reiche ihn weiter — aber vergleiche ihn nie mit einem festen Text und baue nie Programmverhalten auf seinem Inhalt auf. Fordere ihn nur an, wenn du ihn loggen willst.

---

`Exception` ist ein Interface, also kann deine eigene Klasse eines sein. Eine eigene Ausnahme gibt dem Fehler einen Namen, den eine `on`-Klausel auswählen kann, und Felder, die ein Handler lesen kann:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Drei Teile solltest du beibehalten: `implements Exception`, damit die Klasse zu den anderen Fehlern gehört, ein `final`-Feld mit dem Detail und ein überschriebenes `toString()`, damit der Bericht über unbehandelte Ausnahmen lesbar ist. Ohne diese Überschreibung gibt Dart nur den nackten Klassennamen aus, und das Detail geht verloren.

---

Dart wirft zwei Familien von Objekten, und sie bedeuten das Gegenteil voneinander.

Eine **`Exception`** beschreibt eine Bedingung, die das Programm nicht kontrollieren konnte: ein Text, der keine Zahl war, eine Datei, die nicht da war, ein Netzwerk, das nichts antwortete. `FormatException` ist eine davon. Sie werden erwartet, und sie abzufangen ist die normale Reaktion.

Ein **`Error`** beschreibt einen Fehler im Code selbst:

- `ArgumentError` — eine Funktion wurde mit einem Wert aufgerufen, den sie als ungültig dokumentiert
- `StateError` — ein Objekt wurde in einem Moment verwendet, in dem es nicht tun kann, was verlangt wurde
- `RangeError` — ein Index oder ein Wert war außerhalb des erlaubten Bereichs

Einen `Error` abzufangen versteckt den Bug, statt ihn zu beheben. Die richtige Antwort ist, den Code zu ändern, sodass er nicht mehr geworfen wird: Prüfe das Argument vor dem Aufruf oder verwende eine API, die nicht wirft. Deshalb ist eine `on FormatException`-Klausel gute Praxis, während eine `on ArgumentError`-Klausel es fast nie ist.

---

Manche Bibliotheken bieten eine Version an, die gar nicht wirft. Neben `int.parse` hat Dart **`int.tryParse`**: dieselbe Umwandlung, aber sie gibt `null` zurück, statt zu werfen, wenn der Text keine Zahl ist.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

Das Ergebnis ist ein `int?`, daher verwandelt der `??`-Operator ihn direkt in einen Standardwert:

```dart
final port = int.tryParse(text) ?? 8080;
```

Wenn der Fehler gewöhnlich ist und du nur einen Ausweichwert willst, ist das kürzer und klarer als ein `try`-Block. Behalte `int.parse` für die Fälle, in denen schlechter Text wirklich ein Fehler ist, den jemand weiter oben hören muss.

---

`firstWhere` gibt das erste Element zurück, das einen Test erfüllt. Wenn nichts passt, gibt es kein Element zum Zurückgeben, also wirft es einen `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Wie `int.tryParse` bietet die Bibliothek einen Ausweg an. Der benannte Parameter `orElse` nimmt eine Funktion entgegen, die den Wert erzeugt, den man verwendet, wenn nichts gepasst hat:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

Die Wahl ist dieselbe wie zuvor: `orElse`, wenn „nichts passte“ ein gewöhnliches Ergebnis ist, der bloße Aufruf, wenn es bedeuten würde, dass die Daten kaputt sind und jemand davon hören muss.

---

Der `throw` und der `try` müssen nicht in derselben Funktion leben. Eine Funktion, die ihre Arbeit nicht erledigen kann, wirft, und der Aufrufer, der weiß, was zu tun ist, fängt ab:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` hat keine Meinung dazu, ob ein schlechtes Alter das Programm beenden, eine Nachricht zeigen oder übersprungen werden soll — das entscheidet der Aufrufer, und der Aufrufer ist der Ort, an den der `try`-Block gehört. Diese Aufteilung ist der Grund, warum Werfen mehr wert ist als das Zurückgeben von `-1`: Der Fehler erreicht den einen Ort, der ihn beantworten kann.

Denk daran, dass der `try`-Block beim ersten Fehler stoppt, sodass auch die Anweisungen nach dem fehlgeschlagenen Aufruf übersprungen werden.

---

Wo der `try`-Block sitzt, entscheidet, wie viel Arbeit ein einzelner Fehler vernichtet. Um eine Schleife herum beendet das erste schlechte Element die ganze Charge; **innerhalb** der Schleife geht nur dieses Element verloren und der Rest wird trotzdem verarbeitet:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

Das ist die alltägliche Form, um eine Datei zu importieren, eine Liste von Einstellungen zu lesen oder eine Warteschlange von Nachrichten zu behandeln: Eine beschädigte Zeile soll die guten nicht wegwerfen. Die Regel bleibt dieselbe wie zuvor — halte den `try`-Block um die Anweisung, die fehlschlagen kann, und nicht größer.

---

Das letzte Teilstück ist das absichtliche Werfen eines `Error`. Eine Funktion, die dokumentiert, was sie akzeptiert, sollte alles andere laut ablehnen, und `ArgumentError` ist das Objekt dafür:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

Die Nachricht ist als `e.message` erreichbar, und `toString()` gibt `Invalid argument(s): ` gefolgt von ihr aus.

Das widerspricht nicht der Regel von zuvor. Einen `ArgumentError` zu werfen ist richtig, einen abzufangen nicht: Er sagt dem Autor des *Aufrufers*, dass der Aufruf selbst falsch ist, und die Lösung ist eine Prüfung vor dem Aufruf, kein Handler darum herum.
