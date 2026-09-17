Niektórych instrukcji nie da się wykonać: odczytanie tekstu, który nie jest liczbą, sięgnięcie po element za końcem listy, prośba o pierwszy element pustej listy. Gdy to się zdarza, Dart **rzuca** obiekt, który opisuje niepowodzenie.

Sam możesz rzucić taki obiekt słowem kluczowym `throw`. `Exception('message')` buduje gotowy obiekt niosący krótkie wyjaśnienie:

```dart
throw Exception('no fuel');
```

Rzucenie nie jest `return`. Porzuca ono instrukcję, funkcję i każdego wywołującego powyżej, szukając czegoś, co to obsłuży. Gdy nic tego nie robi, program zatrzymuje się i wypisuje niepowodzenie:

```
Unhandled exception:
Exception: no fuel
```

Wszystko po rzuceniu jest pomijane, więc linie, które miały się wykonać, nigdy tego nie robią. Właśnie o to chodzi w tym temacie: o zdecydowaniu, gdzie niepowodzenie jest obsługiwane, zamiast pozwolić mu zakończyć program.

---

Aby program pozostał przy życiu, owiń ryzykowną instrukcję w blok `try`, a wyjście z sytuacji opisz w bloku `catch`:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` rzuca, gdy tekst nie opisuje liczby całkowitej. Dart opuszcza blok `try` przy pierwszej instrukcji, która rzuca, pomija resztę tego bloku, wykonuje blok `catch`, a potem kontynuuje z następującym dalej kodem. Zmienna w nawiasach, tutaj `e`, to sam rzucony obiekt.

Nic wewnątrz bloku `try` nie jest cofane, więc trzymaj go tak krótkim, jak niepowodzenie, którego się spodziewasz.

---

Nagi `catch` łapie wszystko, co ukrywa także niepowodzenia, których nie przewidziałeś. Aby obsłużyć dokładnie jeden rodzaj, wymień jego typ w klauzuli `on`:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` rzuca **`FormatException`**, gdy tekst nie jest liczbą całkowitą, więc to ten typ wymienia się przy odczycie danych wejściowych. Klauzula `on` pasuje do tego typu i jego podtypów, i do niczego innego: każde inne niepowodzenie dalej wędruje na zewnątrz i nadal się pojawi, zamiast zostać połkniętym przez ratunek, który nigdy nie był dla niego przeznaczony.

---

Po bloku `try` może następować **kilka** klauzul, z których każda radzi sobie z innym niepowodzeniem. Dart porównuje rzucony obiekt z nimi od góry do dołu i wykonuje **pierwszą**, która pasuje:

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

Odczytanie listy indeksem, który nie istnieje, rzuca **`RangeError`**, więc dwa niepowodzenia tej jednej linii dostają różne odpowiedzi.

Ponieważ wygrywa pierwsze dopasowanie, kolejność ma znaczenie: klauzula dla ogólnego typu umieszczona nad bardziej konkretną zawsze wygrałaby, czyniąc konkretną klauzulę nieosiągalną. Zapisuj najpierw klauzule konkretne, a nagiego `catch` na końcu, jeśli chcesz mieć siatkę bezpieczeństwa.

Klauzula `on RangeError` powyżej jest tu tylko po to, aby pokazać, jak porządkuje się kilka klauzul. `RangeError` sygnalizuje błąd w kodzie, a nie warunek, nad którym program nie miał kontroli, a późniejsze ćwiczenie wyjaśnia, dlaczego takiemu niepowodzeniu należy zapobiegać, zamiast go łapać.

---

Często ratunek w ogóle nie potrzebuje rzuconego obiektu: typ mówi już wszystko. W takim przypadku usuń część `catch` i zostaw tylko klauzulę `on`:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

Obie formy różnią się tylko tym, czy dostajesz zmienną:

- `on FormatException catch (e)` — pasuje do tego typu i daje ci obiekt jako `e`
- `on FormatException` — pasuje do tego typu, bez zmiennej
- `catch (e)` — pasuje do wszystkiego i daje ci obiekt

Pominięcie nieużywanej zmiennej sprawia, że procedura obsługi uczciwie pokazuje, czego naprawdę używa.

---

Za procedurami obsługi może następować trzeci blok. `finally` wykonuje się **w każdym przypadku**: gdy blok `try` zakończył się normalnie, gdy procedura obsługi uporała się z niepowodzeniem, a także wtedy, gdy nic nie pasowało i niepowodzenie nadal wędruje na zewnątrz.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Wykonuje się nawet zanim `return` odda swoją wartość, dlatego komunikat powyżej jest wypisywany, zanim wywołujący zobaczy wynik. To czyni `finally` miejscem na pracę, która musi się zdarzyć w każdym razie, na przykład zamknięcie tego, co otworzyłeś.

---

Twój własny kod rzuca tak samo, jak robi to biblioteka. `Exception('message')` buduje zwykły wyjątek niosący krótkie wyjaśnienie, a `throw` wysyła go w drogę:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

Komunikat nie ginie: `toString()` składa razem słowo `Exception`, dwukropek i komunikat, i dokładnie to wypisuje raport o nieobsłużonym wyjątku.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Rzucenie wygrywa ze zwracaniem zmyślonej wartości takiej jak `-1`: wywołujący nie może zapomnieć na nią spojrzeć, a powód podróżuje razem z wyjątkiem.

---

Czasami procedura obsługi nie jest właściwym miejscem na ratunek: chcesz tylko *dostrzec* niepowodzenie i pozwolić mu dotrzeć do wywołującego, który faktycznie może się nim zająć. Słowo kluczowe `rethrow` robi to wewnątrz bloku `catch` lub `on ... catch`:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` wysyła **ten sam** obiekt dalej, więc wywołujący widzi pierwotne niepowodzenie. Zapisanie zamiast tego `throw e` też by zadziałało, ale rozpoczyna podróż od nowa i gubi miejsce, w którym niepowodzenie pierwotnie powstało.

Blok `finally` w tej samej instrukcji nadal się wykonuje, nawet przy wyjściu przez rzucenie.

---

Klauzula `catch` przyjmuje **drugi** parametr:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

Pierwszy to rzucony obiekt, drugi to `StackTrace`: łańcuch wywołań, które działały w momencie rzucenia. Odpowiada na pytanie, *skąd* przyszło niepowodzenie, na co sam komunikat rzadko pozwala.

Stack trace wymienia nazwy plików, numery linii i ramki, i zmienia się wraz z buildem oraz ścieżką wywołań. Wypisz go, dołącz do raportu, przekaż dalej — ale nigdy nie porównuj go ze stałym tekstem i nigdy nie buduj zachowania programu na jego zawartości. Proś o niego tylko wtedy, gdy zamierzasz go zapisać w dzienniku.

---

`Exception` jest interfejsem, więc twoja własna klasa też może nim być. Własny wyjątek nadaje niepowodzeniu nazwę, którą klauzula `on` może wybrać, oraz pola, które procedura obsługi może odczytać:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Trzy części warto zachować: `implements Exception`, aby klasa należała do pozostałych niepowodzeń, pole `final` niosące szczegóły oraz nadpisany `toString()`, aby raport o nieobsłużonym wyjątku był czytelny. Bez tego nadpisania Dart wypisuje samą nazwę klasy, a szczegóły giną.

---

Dart rzuca dwie rodziny obiektów, a znaczą one przeciwne rzeczy.

**`Exception`** opisuje warunek, nad którym program nie miał kontroli: tekst, który nie był liczbą, plik, którego nie było, sieć, która niczym nie odpowiedziała. `FormatException` jest jednym z nich. Są one oczekiwane, a łapanie ich to normalna reakcja.

**`Error`** opisuje błąd w samym kodzie:

- `ArgumentError` — funkcję wywołano z wartością, którą sama dokumentuje jako nieprawidłową
- `StateError` — obiekt użyto w momencie, w którym nie może zrobić tego, o co proszono
- `RangeError` — indeks lub wartość były poza dozwolonym zakresem

Łapanie `Error` ukrywa usterkę zamiast jej naprawiać. Właściwą odpowiedzią jest zmiana kodu tak, aby przestał być rzucany: sprawdź argument przed wywołaniem albo użyj API, które nie rzuca. Dlatego klauzula `on FormatException` to dobra praktyka, podczas gdy klauzula `on ArgumentError` prawie nigdy nią nie jest.

---

Niektóre biblioteki oferują wersję, która w ogóle nie rzuca. Obok `int.parse` Dart ma **`int.tryParse`**: tę samą konwersję, ale zwraca `null` zamiast rzucać, gdy tekst nie jest liczbą.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

Wynikiem jest `int?`, więc operator `??` zamienia go od razu w wartość domyślną:

```dart
final port = int.tryParse(text) ?? 8080;
```

Gdy niepowodzenie jest zwykłe i chcesz tylko wartości zapasowej, to rozwiązanie jest krótsze i jaśniejsze niż blok `try`. Zachowaj `int.parse` dla przypadków, w których zły tekst naprawdę jest niepowodzeniem, o którym ktoś powyżej musi się dowiedzieć.

---

`firstWhere` zwraca pierwszy element spełniający test. Gdy nic nie pasuje, nie ma elementu do zwrócenia, więc rzuca `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Podobnie jak `int.tryParse`, biblioteka oferuje wyjście z sytuacji. Nazwany parametr `orElse` przyjmuje funkcję, która produkuje wartość do użycia, gdy nic nie pasowało:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

Wybór jest taki sam jak wcześniej: `orElse`, gdy "nic nie pasowało" to zwykły wynik, nagie wywołanie, gdy oznaczałoby to, że dane są zepsute i ktoś musi się o tym dowiedzieć.

---

`throw` i `try` nie muszą mieszkać w tej samej funkcji. Funkcja, która nie może wykonać swojej pracy, rzuca, a wywołujący, który wie, co z tym zrobić, łapie:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` nie ma zdania na temat tego, czy zły wiek powinien kończyć program, pokazać komunikat czy zostać pominięty — to decyzja wywołującego, i to u wywołującego powinien znajdować się blok `try`. Ten podział sprawia, że rzucenie jest warte więcej niż zwrócenie `-1`: niepowodzenie dociera do jednego miejsca, które potrafi mu odpowiedzieć.

Pamiętaj, że blok `try` zatrzymuje się przy pierwszym niepowodzeniu, więc instrukcje po wywołaniu, które zawiodło, także są pomijane.

---

To, gdzie leży blok `try`, decyduje o tym, ile pracy zniszczy jedno niepowodzenie. Wokół pętli pierwszy zły element kończy całą partię; **wewnątrz** pętli ginie tylko ten element, a reszta jest nadal przetwarzana:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

To codzienny kształt importowania pliku, odczytu listy ustawień czy obsługi kolejki komunikatów: jeden uszkodzony wiersz nie powinien wyrzucać dobrych. Zasada pozostaje taka sama jak wcześniej — trzymaj blok `try` wokół instrukcji, która może zawieść, i żadnej większej.

---

Ostatnim elementem jest rzucanie `Error` celowo. Funkcja, która dokumentuje, co przyjmuje, powinna głośno odrzucać wszystko inne, a `ArgumentError` jest do tego odpowiednim obiektem:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

Komunikat jest dostępny jako `e.message`, a `toString()` wypisuje `Invalid argument(s): ` wraz z nim.

To nie przeczy zasadzie sprzed chwili. Rzucenie `ArgumentError` jest słuszne, łapanie go już nie: mówi autorowi *wywołującego*, że samo wywołanie jest złe, a poprawką jest sprawdzenie przed wywołaniem, a nie procedura obsługi wokół niego.
