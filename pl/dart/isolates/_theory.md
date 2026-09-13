Każda linia Darta napisana do tej pory działa wewnątrz **izolatu**: wątku z własną pamięcią i własną pętlą zdarzeń. Program startuje z jednym izolatem, izolatem *głównym*, i może uruchomić kolejne.

Izolaty wyróżnia to, że nie współdzielą **niczego**. Dwa izolaty nigdy nie widzą tego samego obiektu, więc nie ma blokad, wyścigu danych ani częściowo zaktualizowanej wartości. Komunikują się ze sobą wyłącznie przez przekazywanie **kopii** wiadomości.

Najkrótszy sposób użycia drugiego izolatu to **`Isolate.run`**. Przyjmuje on funkcję, uruchamia ją na zupełnie nowym izolacie i oddaje `Future` z jej wynikiem:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` mieszka w bibliotece `dart:isolate`, więc plik musi zaczynać się od `import 'dart:isolate';`. Dopóki nowy izolat liczy, izolat główny pozostaje wolny: to prawdziwa **równoległość**, praca dzieje się na innym rdzeniu procesora.

---

Funkcja przekazana do `Isolate.run` może **przechwytywać** zmienne ze swojego otoczenia. Te wartości są kopiowane do nowego izolatu razem z funkcją, więc obliczenie może zależeć od wywołującego:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` zwraca `Future` z tym, co zwraca funkcja, więc `triple` może po prostu go zwrócić: nie potrzeba `async` ani `await`, kiedy tylko przekazujesz future dalej.

Cała idea przenoszenia pracy do innego izolatu polega na tym, że długie obliczenia przestają zamrażać izolat główny. Pętla działająca przez sekundę blokuje wszystko, gdy działa na izolacie głównym; wewnątrz `Isolate.run` działa gdzie indziej, a izolat główny wciąż obsługuje własne zdarzenia.

---

Między izolatami kopiowane są tylko **dane**; **kod** nie. Każdy izolat programu i tak widzi wszystkie funkcje i klasy najwyższego poziomu tego programu, więc obliczenie przekazane do `Isolate.run` może je swobodnie wywoływać:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

W podróż udają się przechwycone `text` w jedną stronę i powstały `int` w drugą, każdy jako kopia. Schemat jest zawsze ten sam: zostaw ciężką funkcję tam, gdzie jest, i opakuj **wywołanie** w `Isolate.run`.

---

`await` i `Isolate.run` rozwiązują dwa różne problemy i warto je wyraźnie rozdzielać.

`await` daje ci **współbieżność** na pojedynczym izolacie: podczas gdy jedna funkcja czeka na timer albo serwer, izolat wykonuje inny oczekujący kod. Nic nie działa w tym samym momencie, izolat po prostu przestaje marnować czas. To właściwe narzędzie do czekania.

`Isolate.run` daje ci **równoległość**: drugi izolat na drugim rdzeniu procesora, wykonujący własny kod w tym samym momencie co pierwszy. To właściwe narzędzie do obliczeń.

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

Czekanie `await` na wolne obliczenie nie pomaga wcale: `await bigSum()` nadal wykonuje `bigSum` na bieżącym izolacie i blokuje go do ostatniej linii. Tylko drugi izolat przenosi tę pracę gdzie indziej.

---

`Isolate.run` to skrót dla pojedynczego wyniku. Kiedy chcesz izolat, który działa dalej i zgłasza się więcej niż raz, uruchom go sam za pomocą **`Isolate.spawn`** i daj mu sposób na odpowiedź.

Tym sposobem jest para portów. **`ReceivePort`** to skrzynka pocztowa: tworzysz ją u siebie i odczytujesz wiadomości, które przychodzą. Jej **`sendPort`** to adres tej skrzynki i jedyna rzecz, której drugi izolat potrzebuje, żeby odpowiedzieć.

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

`Isolate.spawn` przyjmuje funkcję do uruchomienia i pojedynczą wiadomość do przekazania jej, tutaj `SendPort`. Po drugiej stronie `send` wrzuca wartość do skrzynki, a `await receivePort.first` czeka na pierwszą wiadomość i zamyka port.

---

Funkcja przekazywana do `Isolate.spawn` nazywa się **punktem wejścia**. Musi to być funkcja najwyższego poziomu (albo statyczna), która przyjmuje dokładnie jeden parametr: wiadomość, którą przekazuje jej `Isolate.spawn`.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

Wiadomości przychodzące do `ReceivePort` mają statyczny typ `dynamic`, bo wysłana mogła być dowolna wartość. Kiedy wiesz, co wysyła drugi izolat, zrzuć typ:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Uruchomiony izolat zawsze przechodzi te same cztery kroki: otwórz skrzynkę, uruchom pracownika z jego adresem, poczekaj na odpowiedź, użyj jej.

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

`await` przed `Isolate.spawn` czeka, aż izolat się *rozpocznie*, a nie aż skończy swoją pracę: wynik przychodzi później, przez port.

---

`Isolate.spawn` przekazuje dokładnie **jedną** wiadomość do punktu wejścia, a pracownik zwykle potrzebuje zarówno `SendPort` do odpowiedzi, jak i danych do pracy. Zwykłym trikiem jest spakowanie wszystkiego w jedną `List` i rozpakowanie jej po drugiej stronie:

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

Lista jest kopiowana w drodze do środka, więc pracownik czyta własne wartości. `SendPort` to jedna z niewielu rzeczy, które nie są kopiowane, lecz współdzielone: wciąż wskazuje na skrzynkę izolatu, który go utworzył, i właśnie dlatego może służyć za adres zwrotny.

---

`first` odczytuje jedną wiadomość i zamyka skrzynkę. `ReceivePort` jest też **`Stream`em**, więc żeby odczytać wiele wiadomości, iterujesz po nim pętlą `await for`.

Pętla nigdy nie kończy się sama: port pozostaje otwarty i czeka na wiadomość, która może nigdy nie przyjść. Pracownik wysyła więc ostatnią wartość jako sygnał, często `null`, a słuchacz reaguje wywołaniem **`close()`**, które kończy strumień i pętlę:

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

Zebranie całej serii wiadomości trzyma się jednego przepisu: pusta lista przed pętlą, jedno `add` na każdą prawdziwą wiadomość i `close()` na sygnał kończący strumień. Gdy port zostanie zamknięty, `await for` się kończy i funkcja może zwrócić wynik:

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

Wiadomości zachowują kolejność, w jakiej zostały wysłane, więc budowana lista odzwierciedla pracę drugiego izolatu krok po kroku.

---

Otwarty `ReceivePort` liczy się jako oczekująca praca: dopóki jakiś istnieje, izolat, który go posiada, ma powód, żeby żyć dalej, a jego pętla zdarzeń wciąż czeka na wiadomość. W programie z linii poleceń izolat główny z otwartym portem po prostu **nigdy się nie kończy** i trzeba zatrzymać go ręcznie.

Zamknięcie portu jest więc częścią pracy, a nie optymalizacją:

- `await port.first` zamyka go za ciebie po jednej wiadomości
- `port.close()` zamyka go jawnie, czego potrzebujesz po pętli `await for`

`Isolate.run` nie ma żadnej z tej księgowości: tworzy porty, zamyka je i wyłącza izolat za ciebie. Preferuj je, kiedy wszystko, czego potrzebujesz, to jeden wynik.

---

Wyjątek wyrzucony wewnątrz izolatu nie może przeskoczyć do innego: oba mają osobne stosy. `Isolate.run` buduje za ciebie most nad tą przepaścią: łapie błąd, kopiuje go z powrotem i sprawia, że zwrócony future zawodzi z nim. Po twojej stronie jest to więc zwykły błąd asynchroniczny, łapany przez `try`/`catch` wokół `await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

`await` wewnątrz `try` ma znaczenie, dokładnie tak samo jak przy każdym innym future: bez niego future opuściłby blok `try` niedokończony, a `catch` nigdy by się nie wykonał.

Z `Isolate.spawn` takiego mostu nie ma. Niezłapany błąd po cichu zabija uruchomiony izolat, a rodzic wciąż czeka na wiadomość, która nigdy nie przyjdzie: to jeszcze jeden powód, żeby najpierw sięgać po `Isolate.run`.

---

Błąd, który wraca z `Isolate.run`, jest **kopią** tego rzuconego po drugiej stronie, więc zwykłe sprawdzenia nadal działają: `catch (e)` daje ci obiekt, a `e is FormatException` mówi, jaki to był rodzaj awarii.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

Na czym nie możesz polegać, to stack trace wskazujący w twój własny izolat: błąd podróżował, stos nie.

---

Złożone w całość, program z `Isolate.run` czyta się jak zwykły kod sekwencyjny: linia przed wywołaniem działa na izolacie głównym, obliczenie działa gdzie indziej, a linia po `await` znów działa na izolacie głównym, z wynikiem w ręku.

```dart
import 'dart:isolate';

int double(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => double(4));
  print(result);
}
// start
// 8
```

---

Ponieważ izolaty nie współdzielą pamięci, każda wiadomość jest **kopiowana**, gdy ją przekracza. Liczby, booleany, napisy, `null`, listy, mapy i większość zwykłych obiektów mogą odbyć tę podróż; kilku rzeczy nie da się skopiować wcale, jak otwartego gniazda, a próba wysłania takiej rzeczy rzuca `ArgumentError`.

Konsekwencją jest reguła, która czyni izolaty bezpiecznymi: po wysłaniu obie strony mają **dwa niezależne obiekty**. Cokolwiek jeden izolat zrobi ze swoją kopią, jest niewidoczne dla drugiego.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort` jest wyjątkiem potwierdzającym regułę: jest współdzielony, a nie kopiowany, właśnie po to, żeby nadal wskazywać na oryginalną skrzynkę.

---

Każde `Isolate.run` uruchamia własny izolat, więc kilka z nich naprawdę działa w tym samym momencie, na tylu rdzeniach, ile ma maszyna. Schemat jest ten, który już znasz z future: najpierw wystartuj każde obliczenie, a potem poczekaj na wszystkie za pomocą `Future.wait`, które zachowuje wyniki w kolejności wejścia.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Uruchomienie izolatu nie jest darmowe: kosztuje pamięć i kilka milisekund. Podzielenie jednego długiego obliczenia między garstkę izolatów się opłaca, wysyłanie tysiąca trywialnych dodań do tysiąca izolatów już nie.
