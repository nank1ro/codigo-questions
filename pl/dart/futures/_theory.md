Niektóre operacje zajmują czas: odczyt pliku, wywołanie serwera, oczekiwanie na timer. Dart nie blokuje programu, gdy one trwają. Zamiast tego taka funkcja zwraca **`Future<T>`**: obietnicę, że wartość typu `T` będzie dostępna **później**.

Najprostszy future to taki, który już ma swoją wartość, zbudowany za pomocą `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Aby wydobyć wartość z future, używasz **`await`**. `await` wstrzymuje bieżącą funkcję, dopóki future się nie zakończy, a potem daje ci zwykłą wartość. Jest dozwolony tylko wewnątrz funkcji oznaczonej **`async`**, więc `main` staje się `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Bez `await` `n` byłoby samym obiektem `Future`, a `print(n)` pokazałoby `Instance of 'Future<int>'` zamiast liczby.

---

Oznaczenie funkcji jako `async` robi dwie rzeczy: pozwala używać `await` w ciele i sprawia, że funkcja **zwraca `Future`**. To, co zwrócisz przez `return`, staje się wartością, którą future się kończy, więc zadeklarowany typ zwracany to `Future<T>`, mimo że ciało zwraca zwykłe `T`:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

Nie potrzebujesz tu `Future.value`: słowo kluczowe `async` samo opakowuje zwróconą wartość.

---

`Future.value` kończy się natychmiast. Aby zasymulować pracę, która zajmuje czas, użyj **`Future.delayed`**: przyjmuje `Duration` i funkcję, czeka przez podany czas, a potem kończy się tym, co zwróci funkcja:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` buduje się za pomocą parametrów nazwanych, takich jak `seconds`, `milliseconds` czy `minutes`. Wewnątrz funkcji `async` możesz też poczekać na samo opóźnienie, bez wartości, wyłącznie po to, by zrobić pauzę:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Oba style są powszechne; drugi czyta się jak zwykły kod sekwencyjny.

---

Miej jasno w głowie dwie strony future:

- funkcja `async` **deklaruje** `Future<T>` i **zwraca** zwykłe `T`: opakowanie jest automatyczne
- wywołujący, który robi `await` na `Future<T>`, **otrzymuje** zwykłe `T`: rozpakowanie jest automatyczne

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Napisanie `int count() async` to błąd: funkcja `async` musi deklarować typ zwracany `Future` (albo `void`).

---

`await` to nie jedyny sposób na użycie future. Możesz też zarejestrować **callback** za pomocą **`then`**: funkcja, którą przekażesz, zostanie wywołana z wartością, gdy future się zakończy. W przeciwieństwie do `await`, `then` **nie** wstrzymuje bieżącej funkcji, więc kod po nim wykonuje się jako pierwszy:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Nawet future zbudowany za pomocą `Future.value` dostarcza swoją wartość dopiero po zakończeniu bieżącego kodu, dlatego `waiting` jest wypisywane najpierw. `then` działa w każdej funkcji, `async` czy nie.

---

Wewnątrz funkcji `async` `await` pozwala pisać kroki asynchroniczne tak, jakby były zwykłym kodem sekwencyjnym. Każdy `await` czeka na swoje future, a następna linia wykonuje się dopiero wtedy, gdy wartość jest już dostępna:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` można też stosować bezpośrednio w wyrażeniu: `return await width() * await height();` daje ten sam wynik.

---

Gdy funkcja napotka `await`, **wstrzymuje się** w tej linii, a reszta programu działa dalej. Linie po `await` wykonają się dopiero wtedy, gdy future się zakończy. Czytanie funkcji `async` od góry do dołu mówi ci więc dokładną kolejność jej efektów:

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

Future może też zakończyć się **błędem**. Gdy funkcja `async` rzuca wyjątek, nie wydostaje się on natychmiast: staje się błędem zwróconego future. Kto zrobi `await` na tym future, zobaczy błąd rzucony w miejscu `await`, można go więc obsłużyć zwykłym `try`/`catch`:

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

`await` wewnątrz `try` jest kluczowy: `return parseLater(s);` przekazałoby future wywołującemu **bez czekania**, więc błąd dotarłby, gdy blok `try` już się skończył, a `catch` nigdy by się nie wykonał.

---

Błędy podróżują razem z future, a nie przez stos wywołań. Wywołanie funkcji `async`, która rzuca wyjątek, samo w sobie nigdy nie wywala wywołującego: błąd jest przechowywany w zwróconym future i pojawia się później, w miejscu, w którym future jest oczekiwane. `try`/`catch` musi więc obejmować **`await`**, a nie wywołanie, które utworzyło future.

Jeśli nikt nigdy nie zaczeka na nieudane future ani go nie obsłuży, Dart zgłasza *unhandled exception*, a w programie wiersza poleceń kończy się błędem.

---

Przy callbackach błędy obsługuje **`catchError`**, odpowiednik `then`. Oba zwracają nowe future, więc zwykle się je łączy w łańcuch: `then` dostaje wartość, jeśli future się powiedzie, `catchError` dostaje błąd, jeśli zawiedzie, i wykonuje się tylko jeden z dwóch callbacków:

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

`catchError` umieszczony po `then` łapie też błędy rzucone wewnątrz callbacku `then`. Tak jak przy `then`, kod po łańcuchu wykonuje się jako pierwszy, bo callbacki są wywoływane dopiero po zakończeniu bieżącego kodu.

---

Gdy kilka future nie zależy od siebie nawzajem, przekaż je wszystkie do **`Future.wait`**: przyjmuje `List<Future<T>>`, pozwala im działać w tym samym czasie i zwraca jedno `Future<List<T>>`, które kończy się, gdy **wszystkie** są gotowe. Wyniki zachowują kolejność listy wejściowej, niezależnie od tego, które future skończyło pierwsze:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` zajmuje `25` milisekund, bo `fast()` jest wywoływane dopiero, gdy `slow()` się zakończy; `await Future.wait([slow(), fast()])` zajmuje około `20`, czyli tyle, ile trwa najdłuższe.

---

`Future.wait` to narzędzie do "wczytaj kilka rzeczy, a potem działaj dalej". Typowy schemat to: zbuduj listę future, zrób na niej `await Future.wait`, a potem użyj powstałej listy:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` kończy się pierwsze, ale lista i tak zachowuje kolejność wywołań: najpierw `stock()`, potem `orders()`.

---

Nie potrzebujesz `Future.wait`, aby uruchomić dwa future w tym samym czasie. Funkcja `async` zaczyna działać, gdy tylko zostanie **wywołana**, aż do swojego pierwszego `await`; future, które dostajesz, to praca już w toku. Sztuczka polega więc na tym, by **najpierw wywołać, a poczekać później**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Porównaj z `return await words() / await pages();`, gdzie `pages()` jest wywoływane dopiero po zakończeniu `words()`: ten sam wynik, dwa razy dłużej. Wybieraj formę współbieżną zawsze, gdy drugie wywołanie nie potrzebuje wyniku pierwszego.

---

Błąd **propaguje się** przez każdy `await`, który go nie łapie. Jeśli `load()` zawiedzie, `await load()` wewnątrz `loadTwice()` rzuca wyjątek; ponieważ `loadTwice` nie ma `try`/`catch`, jego własne future kończy się tym samym błędem; i tak dalej w górę łańcucha, aż któryś `await` zostanie otoczony przez `try`/`catch`:

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

Odzwierciedla to sposób, w jaki wyjątki propagują się przez wywołania synchroniczne: obsługujesz je raz, na poziomie, który wie, co zrobić.

---

`Future.wait` działa według tej samej reguły: jeśli **którekolwiek** z future zawiedzie, połączone future kończy się tym błędem, a `await Future.wait(...)` rzuca wyjątek. Nigdy nie dostajesz częściowej listy udanych wartości. Aby zachować pozostałe, obsłuż błąd wewnątrz każdego pojedynczego future, na przykład za pomocą `catchError`, zanim przekażesz je do `Future.wait`.

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

Ponieważ `await` zamienia błędy future w zwykłe wyjątki, do kodu asynchronicznego stosują się wszystkie typowe wzorce `try`/`catch`, w tym pętle z ponawianiem. Wewnątrz bloku `catch` **`rethrow`** rzuca ten sam błąd ponownie i w ten sposób poddajesz się po ostatniej próbie:

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

Parametr o typie funkcyjnym, taki jak `Future<String> Function() task`, otrzymuje samą **funkcję**, a nie future: każde wywołanie `task()` rozpoczyna nową próbę.
