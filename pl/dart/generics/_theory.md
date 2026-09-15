`List` nie tylko przechowuje wartości, przechowuje wartości **jednego typu**. Typ zapisuje się w nawiasach kątowych bezpośrednio po nazwie kolekcji:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` i `int` są tutaj **argumentami typu**, a typ, który taki argument przyjmuje, nazywamy **generycznym**. Klasa listy jest napisana raz, a `List<String>` i `List<int>` to dwa różne typy, które z niej powstają.

Korzyść jest taka, że kompilator wie, co jest w środku:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // dobrze: first jest typu String
```

---

`List` nie jest jedyną generyczną kolekcją. `Set` przyjmuje jeden argument typu, a `Map` przyjmuje **dwa**: jeden dla kluczy i jeden dla wartości, w tej kolejności.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

Pustego literału kolekcji nie da się odczytać z jego zawartości, więc argumenty typu zapisuje się na samym literale:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Gdy typy są już znane, wszystko, co wyjmujesz z kolekcji, ma właściwy typ: `ages['Ada']` to `int?`, nigdy tajemnicza wartość.

---

Dart ma też typ `dynamic`, który oznacza „wolno wszystko”. `List<dynamic>` przyjmuje każdą wartość, więc wygląda na wygodniejszą niż `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

Haczyk polega na tym, że podczas pisania kodu nic nie jest sprawdzane. Każde wywołanie na wartości `dynamic` jest rozwiązywane w czasie działania programu, więc literówka taka jak `things.first.toUpperCse()` kompiluje się bez przeszkód i wywala program na oczach użytkownika.

Generyki są alternatywą: jeden fragment kodu, który działa z **dowolnym** typem, podczas gdy każde jego użycie jest nadal sprawdzane dla **jednego** typu. W tym jest cały sens tego tematu.

---

Nie ograniczasz się do klas generycznych dostarczanych z Dartem: możesz deklarować własne. **Parametr typu** zapisuje się w nawiasach kątowych po nazwie klasy, a od tej chwili jest to zwykły typ wewnątrz jej ciała:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` to jedynie nazwa zastępcza. Jest uzupełniana w momencie tworzenia `Box`, jawnie albo dzięki inferencji:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, wywnioskowany z argumentu
print(a.value + 1);      // 8, kompilator wie, że value jest typu int
```

Litera nie ma znaczenia: `T` to konwencja oznaczająca „typ” i nic więcej.

---

Funkcja może być generyczna sama w sobie, bez życia w klasie generycznej. Parametr typu zapisuje się między nazwą a listą parametrów:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T to tutaj String
print(firstOf([10, 20]));        // 10, T to tutaj int
```

Jedno ciało funkcji, sprawdzane raz, używane ponownie dla każdego typu. Argument typu jest zwykle wnioskowany z argumentów, ale można go zapisać jawnie, gdy inferencja nie ma na czym pracować:

```dart
final empty = firstOf<String>(<String>[]); // rzuca, ale typ jest jasny
```

Metody wewnątrz klasy podlegają dokładnie tej samej regule.

---

Wewnątrz klasy generycznej parametr typu jest widoczny wszędzie: w polach, w parametrach konstruktora, w sygnaturach metod i w ciałach metod. Deklaruje się go raz, obok nazwy klasy, i może używać go każda składowa.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

O typie decyduje dopiero utworzenie obiektu: `Holder<String>('fig')` sprawia, że `item` jest typu `String`, a `Holder<int>(3)` sprawia, że jest typu `int`.

---

Klasa może deklarować więcej niż jeden parametr typu, oddzielonych przecinkami. `Map<K, V>` to wbudowany przykład: jeden typ dla kluczy, jeden dla wartości.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

**Kolejność** jest częścią typu: `Entry<String, int>` i `Entry<int, String>` to niespokrewnione typy i wartości jednego nie można przypisać do drugiego. Parametry typu można też przestawiać w typie zwracanym — dzięki temu metoda może oddać odwróconą wersję obiektu:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

Przy sound null safety znak zapytania może wylądować w dwóch różnych miejscach i oznaczają one dwie różne rzeczy:

```dart
Box<int?> a = Box(null); // pudełko, które istnieje i przechowuje nullable int
Box<int>? b = null;      // brak pudełka w ogóle, ale jeśli jest, przechowuje int
```

W `Box<int?>` **argument typu** jest nullowalny, więc `a.value` ma typ `int?` i może być `null`, podczas gdy samo `a` zawsze istnieje. W `Box<int>?` **zmienna** jest nullowalna, więc `b` może być `null` i żeby sięgnąć do środka, potrzebujesz `b?.value` albo `b!.value`.

Zwykłe `T` oznacza `T extends Object?`, więc nullowalny argument typu, taki jak `Box<int?>`, jest całkowicie legalny.

---

Różnica ma znaczenie, gdy tylko użyjesz wartości. Na `Box<int?>` sięgasz do pola normalnie, a potem radzisz sobie z `null` w środku, natomiast na `Box<int>?` musisz najpierw ominąć brakujące pudełko:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, pudełko istnieje, jego zawartość jest null

Box<int>? b = null;
print(b?.value ?? 0); // 0, samego pudełka brakuje
```

Zapisanie `b.value` na `Box<int>?` w ogóle się nie skompiluje: Dart odmawia odczytania pola czegoś, co może nie istnieć.

---

Nieograniczony `T` mógłby być czegokolwiek, więc wewnątrz ciała możesz używać tylko tego, co ma każdy obiekt. To się nie kompiluje:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

Naprawia to **ograniczenie**. Zapis `T extends num` mówi, że „`T` może być tylko liczbą”, a w zamian ciało może używać wszystkiego, co oferuje `num`:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

Ograniczenie jest sprawdzane w miejscu wywołania: `half(4)` i `half(2.5)` są w porządku, a `half('fig')` to błąd czasu kompilacji. Ograniczenie to obietnica w obie strony: węższe argumenty w zamian za większe możliwości w środku.

---

Słowem kluczowym dla ograniczenia jest zawsze `extends`, nawet gdy ograniczeniem jest interfejs, a nie nadklasa. W liście parametrów typu nie ma `implements`.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Bez ograniczenia `a > b` nie skompilowałoby się: operator porównania należy do `num`, a nie do każdego obiektu.

---

Ograniczenie może wspominać sam parametr typu. `Comparable<T>` to interfejs wszystkiego, co wie, jak porównać się ze swoim własnym rodzajem, za pomocą `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // ujemne: fig jest pierwsze
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

Tak więc `T extends Comparable<T>` czyta się jako „dowolny typ, który można porównać z nim samym”, co jest dokładnie tym, czego potrzebują funkcje sortujące albo szukające maksimum:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` i `DateTime` spełniają go bezpośrednio. `int` i `double` implementują `Comparable<num>`, więc lista liczb jest po prostu porównywana jako `num`.

---

To samo ograniczenie działa równie dobrze dla najmniejszego elementu: zmienia się tylko znak porównania. `compareTo` zwraca liczbę ujemną, gdy odbiorca jest pierwszy, więc `item.compareTo(best) < 0` znaczy „ten jest mniejszy”.

---

Generyczna klasa może mieć nazwane i **fabryczne** konstruktory jak każda inna klasa, a parametr typu jest dostępny w ich wnętrzu. Konstruktor fabryczny sam nie tworzy obiektu: wykonuje ciało i zwraca jeden, co pozwala mu wybrać, ponownie użyć albo zbudować instancję na dowolny sposób.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

Argument typu zapisuje się przy klasie, a nie przy nazwie konstruktora: `Box<int>.first(...)`. Wewnątrz fabryki `<T>[]` to prawdziwa pusta `List<T>`, więc fabryka to naturalne miejsce do budowania wartości domyślnej dla typu, którego jeszcze nie znasz.

---

Parametr typu zapisany bez ograniczenia wcale nie jest nieograniczony: `class Box<T>` to skrót od `class Box<T extends Object?>`. Dlatego `Box<int?>` jest akceptowane i dlatego wewnątrz klasy nigdy nie wolno ci zakładać, że `value` nie jest nullem.

Aby zabronić nullowalnych argumentów typu, ogranicz parametr przez `Object`:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` to typ wszystkiego oprócz `null`, więc `T extends Object` czyta się jako „cokolwiek, byle naprawdę istniało”.

---

`typedef` nadaje nazwę typowi i może przyjmować własne parametry typu. Zwykłym powodem jest nazwanie rodziny typów funkcyjnych raz, zamiast zapisywać ją przy każdym użyciu:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` to tylko inny sposób zapisania `int Function(String)`, więc oba zapisy są zamienne. Zyskiem jest czytelność: parametr zadeklarowany jako `Transform<I, O> transform` mówi, do czego funkcja służy, a `O Function(I)` mówi tylko, jak wygląda.

Generyczny typedef i generyczna funkcja łączą się naturalnie: własne parametry typu funkcji wypełniają parametry typedefa.
