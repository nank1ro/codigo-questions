Manche Operationen brauchen Zeit: eine Datei lesen, einen Server aufrufen, auf einen Timer warten. Dart blockiert das Programm nicht, während sie laufen. Stattdessen liefert eine solche Funktion ein **`Future<T>`**: das Versprechen, dass ein Wert vom Typ `T` **später** verfügbar sein wird.

Das einfachste Future ist eines, das seinen Wert bereits hat, gebaut mit `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Um den Wert aus einem Future herauszuholen, verwendest du **`await`**. `await` pausiert die aktuelle Funktion, bis das Future abgeschlossen ist, und gibt dir dann den einfachen Wert. Es ist nur innerhalb einer mit **`async`** markierten Funktion erlaubt, `main` wird also zu `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Ohne `await` wäre `n` das `Future` selbst, und `print(n)` würde `Instance of 'Future<int>'` statt der Zahl anzeigen.

---

Eine Funktion als `async` zu markieren bewirkt zweierlei: Es erlaubt `await` im Rumpf, und es lässt die Funktion **ein `Future` zurückgeben**. Was auch immer du mit `return` zurückgibst, wird zum Wert, mit dem das Future abschließt, der deklarierte Rückgabetyp ist also `Future<T>`, obwohl der Rumpf ein einfaches `T` zurückgibt:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

`Future.value` brauchst du hier nicht: Das Schlüsselwort `async` verpackt den zurückgegebenen Wert für dich.

---

`Future.value` schließt sofort ab. Um Arbeit zu simulieren, die Zeit braucht, verwendest du **`Future.delayed`**: Es nimmt eine `Duration` und eine Funktion entgegen, wartet die Dauer ab und schließt dann mit dem ab, was die Funktion zurückgibt:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` wird mit benannten Parametern wie `seconds`, `milliseconds` oder `minutes` gebaut. Innerhalb einer `async`-Funktion kannst du auch eine Verzögerung für sich allein awaiten, ohne Wert, nur um zu pausieren:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Beide Stile sind üblich; der zweite liest sich wie gewöhnlicher sequenzieller Code.

---

Halte die zwei Seiten eines Futures klar auseinander:

- eine `async`-Funktion **deklariert** `Future<T>` und **gibt** ein einfaches `T` **zurück**: das Verpacken passiert automatisch
- ein Aufrufer, der ein `Future<T>` **awaitet**, **erhält** ein einfaches `T`: das Auspacken passiert automatisch

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

`int count() async` zu schreiben ist ein Fehler: Eine `async`-Funktion muss einen `Future`- (oder `void`-) Rückgabetyp deklarieren.

---

`await` ist nicht der einzige Weg, ein Future zu nutzen. Du kannst auch mit **`then`** einen **Callback** registrieren: Die Funktion, die du übergibst, wird mit dem Wert aufgerufen, sobald das Future abschließt. Anders als `await` pausiert `then` die aktuelle Funktion **nicht**, der Code danach läuft also zuerst:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Selbst ein mit `Future.value` gebautes Future liefert seinen Wert erst, nachdem der aktuelle Code fertig ist, deshalb wird `waiting` zuerst ausgegeben. `then` funktioniert in jeder Funktion, ob `async` oder nicht.

---

Innerhalb einer `async`-Funktion erlaubt dir `await`, asynchrone Schritte wie gewöhnlichen sequenziellen Code zu schreiben. Jedes `await` wartet auf sein Future, und die nächste Zeile läuft erst, wenn der Wert da ist:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` kann auch direkt in einem Ausdruck verwendet werden: `return await width() * await height();` ergibt dasselbe Resultat.

---

Wenn eine Funktion auf ein `await` trifft, **pausiert** sie an dieser Zeile und der Rest des Programms läuft weiter. Die Zeilen nach dem `await` laufen erst, wenn das Future abgeschlossen ist. Eine `async`-Funktion von oben nach unten zu lesen verrät dir daher die genaue Reihenfolge ihrer Wirkungen:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

Ein Future kann auch mit einem **Fehler** abschließen. Wenn eine `async`-Funktion wirft, entkommt die Ausnahme nicht sofort: Sie wird zum Fehler des zurückgegebenen Futures. Wer dieses Future **awaitet**, sieht den Fehler beim `await` geworfen, er lässt sich also mit einem gewöhnlichen `try`/`catch` behandeln:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

Das `await` innerhalb des `try` ist entscheidend: `return parseLater(s);` würde das Future **ohne zu warten** an den Aufrufer weiterreichen, der Fehler käme also an, wenn der `try`-Block schon vorbei ist, und das `catch` würde nie laufen.

---

Fehler reisen mit dem Future, nicht über den Aufrufstapel. Eine `async`-Funktion aufzurufen, die wirft, bringt den Aufrufer von sich aus nie zum Absturz: Der Fehler wird im zurückgegebenen Future gespeichert und taucht später auf, an der Stelle, wo das Future awaitet wird. Ein `try`/`catch` muss daher das **`await`** umschließen, nicht den Aufruf, der das Future erzeugt hat.

Wenn niemand das fehlgeschlagene Future jemals awaitet oder behandelt, meldet Dart eine *unhandled exception* und beendet ein Kommandozeilenprogramm mit einem Fehler.

---

Mit Callbacks werden Fehler von **`catchError`** behandelt, dem Gegenstück zu `then`. Beide geben ein neues Future zurück, sie werden daher meist verkettet: `then` erhält den Wert, wenn das Future gelingt, `catchError` erhält den Fehler, wenn es fehlschlägt, und nur einer der beiden Callbacks läuft:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

Ein `catchError` nach `then` fängt auch Fehler, die im `then`-Callback geworfen werden. Wie bei `then` läuft der Code nach der Kette zuerst, denn Callbacks werden erst aufgerufen, wenn der aktuelle Code fertig ist.

---

Wenn mehrere Futures nicht voneinander abhängen, übergib sie alle an **`Future.wait`**: Es nimmt eine `List<Future<T>>` entgegen, lässt sie gleichzeitig laufen und liefert ein einziges `Future<List<T>>`, das abschließt, wenn **alle** fertig sind. Die Ergebnisse behalten die Reihenfolge der Eingabeliste, unabhängig davon, welches Future zuerst fertig wurde:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` braucht `25` Millisekunden, denn `fast()` wird erst aufgerufen, wenn `slow()` abgeschlossen ist; `await Future.wait([slow(), fast()])` braucht etwa `20`, die Dauer des längsten.

---

`Future.wait` ist das Werkzeug für "mehrere Dinge laden, dann weitermachen". Die typische Form ist: die Liste der Futures bauen, darauf `await Future.wait` anwenden und dann die entstandene Liste verwenden:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` schließt zuerst ab, aber die Liste folgt trotzdem der Reihenfolge der Aufrufe: `stock()` zuerst, `orders()` als zweites.

---

Du brauchst `Future.wait` nicht, um zwei Futures gleichzeitig laufen zu lassen. Eine `async`-Funktion beginnt zu laufen, sobald sie **aufgerufen** wird, bis zu ihrem ersten `await`; das Future, das du zurückbekommst, ist die bereits laufende Arbeit. Der Trick ist also: **zuerst aufrufen, später awaiten**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Vergleiche mit `return await words() / await pages();`, wo `pages()` erst aufgerufen wird, nachdem `words()` abgeschlossen ist: gleiches Ergebnis, doppelte Zeit. Bevorzuge die nebenläufige Form, wann immer der zweite Aufruf das Ergebnis des ersten nicht braucht.

---

Ein Fehler **pflanzt sich** durch jedes `await` **fort**, das ihn nicht fängt. Wenn `load()` fehlschlägt, wirft `await load()` innerhalb von `loadTwice()`; da `loadTwice` kein `try`/`catch` hat, schlägt sein eigenes Future mit demselben Fehler fehl; und so weiter die Kette hinauf, bis irgendein `await` von einem `try`/`catch` umschlossen ist:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

Das entspricht dem, wie sich Ausnahmen durch synchrone Aufrufe fortpflanzen: Du behandelst sie einmal, auf der Ebene, die weiß, was zu tun ist.

---

`Future.wait` folgt derselben Regel: Wenn **irgendeines** der Futures fehlschlägt, schließt das kombinierte Future mit diesem Fehler ab und `await Future.wait(...)` wirft. Du bekommst nie eine Teilliste der erfolgreichen Werte. Um die anderen zu behalten, behandle den Fehler innerhalb jedes einzelnen Futures, zum Beispiel mit `catchError`, bevor du es an `Future.wait` übergibst.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

Weil `await` Future-Fehler in gewöhnliche Ausnahmen verwandelt, gelten für asynchronen Code alle üblichen `try`/`catch`-Muster, einschließlich Schleifen, die es erneut versuchen. Innerhalb eines `catch`-Blocks wirft **`rethrow`** denselben Fehler erneut, so gibst du nach dem letzten Versuch auf:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

Ein Parameter mit Funktionstyp wie `Future<String> Function() task` erhält die **Funktion** selbst, nicht ein Future: Jeder Aufruf von `task()` startet einen frischen Versuch.
