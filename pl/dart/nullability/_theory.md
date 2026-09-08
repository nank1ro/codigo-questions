Wiesz już, jak zadeklarować zmienną z typem, np. `String name = 'Ada';`. Czasem jednak wartości po prostu **brakuje**: użytkownik bez pseudonimu, wyszukiwanie, które nic nie znajduje, tekst, którego nie da się zamienić na liczbę. Dart reprezentuje brakującą wartość przez `null`.

Od Darta 2.12 język ma **sound null safety**: zwykły typ taki jak `String` **nigdy** nie może przechowywać `null`. Próba przypisania jest błędem kompilacji, więc program nawet się nie uruchomi:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Aby dopuścić brakującą wartość, dodajesz znak zapytania `?` po typie. `String?` przechowuje albo `String`, albo `null`, a wypisanie `null` pokazuje słowo `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

Typy bez `?` nazywamy **non-nullable**, typy z `?` są **nullable**.

---

Zmienna nullable zadeklarowana **bez wartości** zaczyna od `null`, więc `= null` można pominąć:

```dart
int? age;
print(age); // null
```

Zmienna non-nullable nie ma takiej wartości domyślnej: Dart odmawia skompilowania kodu, który ją odczytuje, zanim wartość zostanie przypisana.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Wywołanie metody lub odczyt właściwości na `null` spowodowałoby awarię, więc Dart nie pozwala robić tego na wartości nullable za pomocą zwykłej kropki:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

Rozwiązuje to operator **dostępu null-aware** `?.`: jeśli wartość jest `null`, całe wyrażenie jest `null` i nic więcej nie jest obliczane, w przeciwnym razie działa jak zwykła `.`:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Ponieważ wynik może być `null`, jego typ jest nullable: `text?.length` to `int?`, a nie `int`.

---

Często brakującą wartość należy zastąpić **wartością domyślną**. Operator **if-null** `??` zwraca lewy operand, gdy nie jest on `null`, a w przeciwnym razie prawy:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` reaguje wyłącznie na `null`: pusty łańcuch `''` czy liczba `0` to prawdziwe wartości, więc zostają zachowane.

`??` dobrze łączy się z `?.`, ponieważ `?.` daje wynik typu nullable:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

Wielką zaletą null safety jest to, że większość błędów z `null` wykrywa **kompilator**, a nie twoi użytkownicy. Dotychczasowe zasady:

- typ non-nullable (`String`, `int`, `List<int>`...) nigdy nie może być `null`
- typ nullable (`String?`, `int?`, `List<int>?`...) może i zaczyna od `null`, gdy zadeklarowano go bez wartości
- `.` na wartości nullable nie kompiluje się: użyj `?.` albo podaj wartość domyślną przez `??`

---

Operator **przypisania if-null** `??=` przypisuje wartość do zmiennej **tylko wtedy**, gdy ta zmienna jest aktualnie `null`; w przeciwnym razie zostawia ją nietkniętą:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

Działa też na wpisach mapy, które są nullable, ponieważ klucza może brakować:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

Czasem **ty** wiesz, że wartość nullable nie jest `null` w danym miejscu, nawet jeśli kompilator tego nie widzi. Operator **null assertion** `!` zamienia `String?` w `String`, obiecując, że wartość jest obecna:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Uwaga: `!` przenosi sprawdzenie z czasu kompilacji na czas działania. Jeśli wartość **jest** `null`, program zgłasza błąd i się zatrzymuje:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Używaj `!` oszczędnie i tylko wtedy, gdy `null` w tym miejscu i tak byłby błędem.

---

Zapamiętaj różnicę między trzema operatorami, które poznałeś dla wartości nullable:

- `?.` zwraca `null`, gdy wartość jest `null`, i nigdy nie zgłasza błędu
- `??` zastępuje `null` wartością domyślną
- `!` zakłada, że wartość jest obecna, i **zgłasza błąd w czasie działania**, gdy jej nie ma

Żaden z nich nie jest błędem kompilacji: kompilator ufa twojemu `!`, a dopiero działający program może się przekonać, że obietnica została złamana.

---

Sprawdzenie wartości nullable za pomocą `if` jest bezpieczniejsze niż `!`, a Dart cię za to nagradza. Po sprawdzeniu takim jak `if (x != null)` kompilator wie, że `x` nie może być `null` wewnątrz bloku, więc traktuje tam `x` jako non-nullable. Nazywa się to **promocją typu**:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

Promocja działa też po wcześniejszym zwrocie:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

Promocja dotyczy **zmiennych lokalnych i parametrów**, których wartość nie może zmienić się za twoimi plecami między sprawdzeniem a użyciem.

---

Promocja typu **nie** działa na **polu** klasy, które może zostać zmienione z zewnątrz, ponieważ między sprawdzeniem a użyciem inny fragment kodu (getter nadpisany w podklasie, inna metoda) mógłby ustawić je z powrotem na `null`:

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

Standardowe rozwiązanie to skopiowanie pola do **zmiennej lokalnej**, która podlega promocji:

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

Pole non-nullable musi zwykle otrzymać wartość w konstruktorze. Gdy wartość jest znana dopiero **później** (po odczytaniu pliku, otwarciu połączenia...), możesz oznaczyć pole jako `late`: kompilator akceptuje brak inicjalizatora i ufa, że przypiszesz polu wartość przed jego odczytem.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Odczyt pola `late`, któremu nie przypisano jeszcze wartości, zgłasza `LateInitializationError` w czasie działania. Podobnie jak `!`, `late` wymienia gwarancję z czasu kompilacji na sprawdzenie w czasie działania, więc jest to obietnica, której musisz dotrzymać.

`late` można też połączyć z inicjalizatorem, który wykonuje się wtedy **leniwie**, przy pierwszym odczycie zmiennej:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

Nullowalność kształtuje sposób deklarowania **parametrów nazwanych**. Parametr nazwany o typie nullable jest opcjonalny: gdy wywołujący go pominie, jest po prostu `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Parametr nazwany o typie non-nullable i bez wartości domyślnej nie miałby wartości, gdyby go pominięto, więc Dart wymaga oznaczenia go jako `required`; wywołujący musi go wtedy zawsze przekazać:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

Nullowalność dotyczy również **elementów** kolekcji. `List<int>` nigdy nie zawiera `null`, natomiast `List<int?>` może:

```dart
List<int?> scores = [7, null, 9];
```

Zwróć uwagę na różnicę wobec `List<int>?`, czyli listy, której samej może brakować, ale która — gdy jest obecna — zawiera wyłącznie prawdziwe liczby.

Aby pozbyć się elementów `null`, `nonNulls` zwraca `Iterable` zawierający tylko obecne wartości, o typie bez `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` robi to samo i działa też wtedy, gdy lista miesza kilka typów.

---

Wiele funkcji bibliotecznych używa `null`, aby zgłosić, że czegoś **nie dało się zrobić**. Zamiana tekstu na liczbę to klasyczny przykład: `int.parse` zgłasza `FormatException`, gdy tekst nie jest liczbą, natomiast `int.tryParse` zwraca zamiast tego `null` i pozwala ci zdecydować, co dalej:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

Typem zwracanym przez `int.tryParse` jest `int?`, więc wszystko, czego się nauczyłeś, ma zastosowanie: `??` dla wartości domyślnej, `?.` do łączenia wywołań i sprawdzenie `if` dla promocji. `double.tryParse` działa tak samo.

---

Jeszcze dwa operatory mają wariant null-aware.

**Kaskada null-aware** `?..` wykonuje łańcuch operacji kaskadowych tylko wtedy, gdy obiekt nie jest `null`, a w przeciwnym razie pomija je wszystkie:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

**Rozwinięcie null-aware** `...?` wstawia elementy kolekcji typu nullable do literału, nie dodając nic, gdy kolekcja jest `null`:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Bez `?` zapis `...extra` na `List<int>?` byłby błędem kompilacji.

---

Prawdziwe dane są pełne luk: puste pole formularza, brakująca kolumna w pliku, tekst, który nie całkiem jest liczbą. Narzędzia z tego rozdziału naturalnie się uzupełniają: `nonNulls`, aby odrzucić brakujące elementy, `int.tryParse`, aby bezpiecznie konwertować, oraz `??` lub sprawdzenie `if`, aby poradzić sobie z tym, czego nie udało się przekonwertować.
