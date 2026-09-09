`Future` reprezentuje **pojedynczą** wartość, która pojawia się później. **Stream** reprezentuje **sekwencję** wartości pojawiających się w czasie: naciśnięcia klawiszy, fragmenty pliku, wiadomości z serwera. Każda wartość nazywa się **zdarzeniem**, a po ostatnim zdarzeniu strumień jest **zakończony**.

Najprostszym sposobem zbudowania strumienia jest `Stream.fromIterable`, który emituje każdy element listy, jeden po drugim:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Aby konsumować zdarzenia po kolei, używasz pętli **`await for`**. Podobnie jak `await`, jest ona dozwolona tylko wewnątrz funkcji oznaczonej `async`, więc `main` staje się `Future<void> main() async`. Ciało pętli wykonuje się raz na zdarzenie, a pętla kończy się, gdy strumień jest zakończony:

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

Zwykła pętla `for` tu nie zadziała: `Stream` nie jest `Iterable`, jego wartości nie są dostępne wszystkie naraz.

---

`Stream.fromIterable` potrzebuje wszystkich wartości z góry. Aby **produkować** wartości po jednej, napisz **generator asynchroniczny**: funkcję, której ciało jest oznaczone `async*`, a typ zwracany to `Stream<T>`. W jej wnętrzu `yield` wysyła jedno zdarzenie do strumienia:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

Ciało nie wykonuje się, gdy wywołujesz `countTo(3)`: wykonuje się leniwie, w miarę jak słuchacz prosi o wartości, a strumień jest zakończony, gdy ciało się skończy.

Aby zebrać wszystkie zdarzenia do `List`, wywołaj `toList()`. Zwraca on `Future<List<T>>`, więc czekasz na niego przez `await`:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Pętla `await for` może robić więcej niż wypisywać: może aktualizować zmienną zadeklarowaną przed pętlą. Funkcja, która konsumuje strumień i oblicza wynik, musi być oznaczona `async` i zwraca `Future` tego wyniku:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

Funkcja dociera do `return` dopiero po zakończeniu strumienia, więc wywołujący otrzymuje wartość końcową, gdy czeka na future:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Każdy strumień kiedyś się kończy. W generatorze `async*` strumień jest **zakończony**, gdy tylko ciało funkcji dobiegnie końca, niezależnie od tego, czy dotarło do końca, czy trafiło na `return`. Pętla `await for` po zakończonym strumieniu kończy się, a każdy future z `toList()` zostaje spełniony.

Strumień nie startuje od nowa ani nie powtarza swoich wartości: raz zakończony, pozostaje zakończony.

---

`await for` wstrzymuje bieżącą funkcję, dopóki strumień nie zostanie zakończony. Gdy chcesz reagować na zdarzenia **bez czekania**, wywołaj `listen` i przekaż callback: jest wywoływany raz na zdarzenie, a kod po `listen` wykonuje się od razu.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` przyjmuje także nazwany parametr `onDone`, funkcję bez argumentów wywoływaną, gdy strumień się kończy:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Generator `async*` może przekazać dalej **każde zdarzenie innego strumienia** za pomocą `yield*` (yield-star). To jak pętla `await for`, która emituje każdą wartość, tyle że w jednej linii:

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

Zewnętrzny strumień kontynuuje własnymi `yield`, gdy wewnętrzny strumień jest zakończony.

---

Podobnie jak `Iterable`, `Stream` ma metody budujące **nowy strumień** na podstawie istniejącego:

- `map` przekształca każde zdarzenie
- `where` zachowuje tylko zdarzenia spełniające warunek
- `take` zatrzymuje się po zadanej liczbie zdarzeń

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Te metody są **leniwe**: nic się nie wykonuje, dopóki ktoś nie zacznie nasłuchiwać powstałego strumienia. Można je łączyć w łańcuch, a strumień źródłowy nigdy nie jest modyfikowany.

---

Ponieważ `where`, `map` i `take` zwracają strumień, możesz łączyć je w łańcuch i zakończyć przez `toList()`, aby otrzymać wynik jako listę. Tylko końcowe `toList()` potrzebuje `await`, bo jest to jedyne wywołanie zwracające `Future`:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Oprócz `toList()` strumień oferuje inne metody, które **konsumują** wszystkie jego zdarzenia i zwracają pojedynczy `Future`:

- `first` i `last` kończą się pierwszym lub ostatnim zdarzeniem
- `length` kończy się liczbą zdarzeń
- `join(separator)` kończy się wszystkimi zdarzeniami złączonymi w jeden `String`
- `reduce(combine)` łączy zdarzenia po dwa w jedną wartość

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` wywołuje `combine` z dotychczasowym wynikiem i kolejnym zdarzeniem. Rzuca wyjątek, gdy strumień jest pusty, więc używaj go tylko wtedy, gdy co najmniej jedno zdarzenie jest gwarantowane.

---

Metody `Stream` dzielą się na dwie grupy:

- metody **przekształcające**, takie jak `map`, `where`, `take` i `skip`, zwracają **nowy `Stream`** i są leniwe: żadne zdarzenie nie jest przetwarzane, dopóki nowy strumień nie jest nasłuchiwany
- metody **konsumujące**, takie jak `toList`, `reduce`, `join`, `first`, `last` i `length`, nasłuchują strumienia i zwracają **`Future`** z wynikiem końcowym

Łańcuch wygląda więc jak zero lub więcej wywołań przekształcających, po których następuje co najwyżej jedno wywołanie konsumujące.

---

Generatory produkują zdarzenia wewnątrz jednej funkcji. Gdy zdarzenia pochodzą **skądinąd** (z przycisku, z callbacku sieciowego, z innego obiektu), potrzebujesz **`StreamController`**. Znajduje się on w bibliotece `dart:async`, więc plik musi zaczynać się od `import 'dart:async';`.

Kontroler jest właścicielem strumienia i pozwala wpychać do niego zdarzenia:

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

- `add(value)` wysyła jedno zdarzenie
- `close()` kończy strumień; zapomnienie o nim oznacza, że słuchacze czekają w nieskończoność
- `stream` to `Stream`, który konsumują słuchacze

Zdarzenia dodane, zanim ktokolwiek zacznie nasłuchiwać, są przechowywane w buforze, więc powyższy kod jest bezpieczny: słuchacz, który pojawia się później, i tak otrzyma `4` i `2`.

---

`StreamController` często jest tworzony i konsumowany w tym samym miejscu: subskrybujesz `controller.stream` przez `listen`, potem dodajesz zdarzenia przez `add` i zamykasz kontroler przez `close`. Ponieważ `listen` nie czeka, zdarzenia są dostarczane po zakończeniu bieżącego kodu, ale zawsze w kolejności, w jakiej zostały dodane:

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

Strumienie widziane do tej pory są **jednosubskrypcyjne**: pozwalają na dokładnie jednego słuchacza. Wywołanie `listen`, `await for` lub dowolnej metody konsumującej po raz drugi rzuca `StateError` ("Stream has already been listened to").

Aby współdzielić strumień między kilku słuchaczy, zamień go na strumień **broadcast** za pomocą `asBroadcastStream()`:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Strumień broadcast nie buforuje: słuchacz otrzymuje tylko zdarzenia wyemitowane **po** jego subskrypcji. W przykładzie obaj słuchacze subskrybują przed pierwszym `await`, więc obaj otrzymują każde zdarzenie.

---

Kontroler może utworzyć strumień broadcast bezpośrednio, za pomocą nazwanego konstruktora `StreamController<T>.broadcast()`. Jego `stream` przyjmuje dowolną liczbę słuchaczy, a każde zdarzenie jest dostarczane do wszystkich, w kolejności, w jakiej się zasubskrybowali:

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

Jak każdy strumień broadcast, nie buforuje: zdarzenia dodane, zanim słuchacz się zasubskrybuje, są dla niego stracone.

---

Strumień może przenosić nie tylko wartości, ale też **błędy**. Wewnątrz generatora `async*` `throw` wysyła zdarzenie błędu i kończy strumień; `StreamController` może wysłać takie zdarzenie przez `addError`.

Po stronie konsumenta pętla `await for` rzuca błąd ponownie w miejscu pętli, więc obsługujesz go zwykłym `try`/`catch` wokół pętli:

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

Przy `listen` przekaż zamiast tego callback `onError`: `stream.listen(print, onError: (e) => print('caught: $e'));`
