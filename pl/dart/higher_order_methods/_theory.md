**Metoda wyższego rzędu** to metoda, która przyjmuje funkcję jako argument. Kolekcje Dart oferują wiele z nich, a przekazywana funkcja jest zazwyczaj funkcją anonimową zapisaną składnią strzałkową `(x) => ...`.

`map` jest najpopularniejszą z nich: wywołuje funkcję dla każdego elementu i produkuje wyniki, po jednym dla każdego elementu, pozostawiając oryginalną kolekcję nietkniętą:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Zwróć uwagę na **nawiasy okrągłe** w wyniku. `map` nie zwraca `List`: zwraca `Iterable`, sekwencję, którą można przejść. Aby otrzymać prawdziwą listę, wywołaj na niej **`toList()`**:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Nawiasy kwadratowe w wyniku oznaczają, że patrzysz na `List`, a nawiasy okrągłe, że patrzysz na zwykły `Iterable`.

---

`where` przyjmuje funkcję zwracającą `bool`, nazywaną **predykatem**, i zachowuje tylko elementy, dla których odpowiada ona `true`. Kolejność przetrwałych elementów nigdy się nie zmienia:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Podobnie jak `map`, `where` zwraca `Iterable` i nigdy nie modyfikuje oryginalnej kolekcji, więc `toList()` ponownie zamienia wynik w `List`.

W innych językach ta metoda nazywa się `filter`; w Dart to `where`.

---

Funkcja przekazana do `map` nie musi zwracać tego samego typu, jaki mają otrzymywane elementy. Przekształcenie listy ciągów znaków w ich długości zamienia `List<String>` w `Iterable<int>`, który `toList()` następnie zamienia w `List<int>`:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

Wynik zawsze ma **dokładnie tyle samo elementów co oryginał**, w tej samej kolejności: `map` przekształca elementy, nigdy ich nie dodaje ani nie usuwa.

---

Niektóre metody wyższego rzędu odpowiadają na pytanie o kolekcję zamiast budować nową. Przyjmują predykat i zwracają `bool`:

- `any` jest `true`, gdy **co najmniej jeden** element spełnia predykat
- `every` jest `true`, gdy **wszystkie** elementy go spełniają

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Obie zatrzymują się, gdy tylko odpowiedź jest pewna: `any` na pierwszym elemencie, który pasuje, `every` na pierwszym, który nie pasuje.

Na pustej kolekcji `any` jest `false`, a `every` jest `true`: nie ma elementu, który potwierdziłby pierwszą, ani takiego, który złamałby drugą.

---

`map` i `where` są **leniwe**: ich wywołanie niczego nie wykonuje. Zwracają `Iterable`, który zapamiętuje źródło i funkcję, a funkcja jest wywoływana dopiero wtedy, gdy coś przechodzi przez wynik, element po elemencie.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // jeszcze nic nie obliczone
print(doubled.first);                      // oblicza tylko 2
```

`toList()` to operacja, która **materializuje** sekwencję: przechodzi przez nią od początku do końca i zapisuje każdy wynik w prawdziwej `List`.

Leniwość ma dwie konsekwencje warte zapamiętania. Leniwy `Iterable` jest przeliczany za każdym razem, gdy po nim iterujesz, więc zmaterializowanie go raz za pomocą `toList()` jest tańsze, gdy potrzebujesz wartości więcej niż raz. I cały czas odnosi się do oryginalnej kolekcji, więc zmiana tej kolekcji zmienia to, co produkuje `Iterable`:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` łączy całą kolekcję w **jedną wartość**. Przyjmuje dwa argumenty: wartość początkową **akumulatora** oraz funkcję, która otrzymuje dotychczasowy akumulator i następny element, a zwraca nowy akumulator:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Tutaj `acc` zaczyna od `0`, potem staje się `1`, `3`, `6` i wreszcie `10`.

Akumulator nie musi być liczbą ani mieć tego samego typu co elementy: zaczynając od `''` i dodając tekst, zbudujesz `String` z listy czegokolwiek.

Szczegół, o którym warto pamiętać: Dart ustala typ akumulatora na podstawie wartości początkowej **oraz** miejsca, w którym wynik jest używany. Wewnątrz `print(...)` oczekiwany typ jest nieznany, więc najpierw zapisz wynik w zmiennej (albo napisz `fold<int>(...)`), w przeciwnym razie kompilator zgłosi, że nie może użyć `+` na akumulatorze.

---

`reduce` to krótszy krewny `fold`. Nie przyjmuje wartości początkowej: **pierwszy element** jest początkowym akumulatorem, a funkcja jest wykonywana dla każdego pozostałego elementu:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Ponieważ nie ma wartości początkowej, wynik zawsze ma **ten sam typ co elementy**, a wywołanie `reduce` na pustej kolekcji rzuca `StateError`: nie ma pierwszego elementu, od którego można zacząć. `fold` nie ma takiego problemu, dlatego jest bezpieczniejszym domyślnym wyborem.

`reduce` sprawdza się najlepiej, gdy szukasz jednego elementu wśród wielu, na przykład największego:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` zwraca **pierwszy** element pasujący do predykatu, zamiast wszystkich:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Gdy nic nie pasuje, nie ma elementu do zwrócenia, więc `firstWhere` rzuca `StateError`. Aby otrzymać odpowiedź zamiast błędu, przekaż nazwany argument **`orElse`**: funkcję bez parametrów, która produkuje wartość zapasową.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` jest funkcją, a nie zwykłą wartością, więc jest wywoływana tylko wtedy, gdy wyszukiwanie się nie powiedzie. Zapis `orElse: 'none'` nie skompiluje się.

---

Gdy funkcja przekazana do `map` zwraca kolekcję dla każdego elementu, kończysz z sekwencją kolekcji. **`expand`** wykonuje tę samą pracę, ale następnie łączy je wszystkie w jedną płaską sekwencję:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

Kolejność jest zachowana: najpierw pojawia się wszystko wyprodukowane przez pierwszy element, potem wszystko wyprodukowane przez drugi i tak dalej.

Ponieważ zwracana kolekcja może mieć dowolny rozmiar, `expand` to również sposób na wyprodukowanie **więcej lub mniej** elementów niż na początku: zwrócenie pustej listy dla elementu po prostu go pomija.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` zachowuje **pierwsze** `n` elementów, a `skip(n)` wyrzuca je. Żadna nie przyjmuje funkcji, ale obie zwracają leniwy `Iterable`, więc naturalnie wpisują się między pozostałe metody wyższego rzędu:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Prośba o więcej elementów, niż faktycznie jest, nie jest błędem: po prostu dostajesz to, co istnieje, albo pusty wynik.

`takeWhile` i `skipWhile` to wersje z predykatem. Pobierają lub pomijają elementy od początku **dopóki** predykat jest spełniony i zatrzymują się na pierwszym elemencie, który go nie spełnia, nawet jeśli późniejsze znów by go spełniały:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart nie ma metody `sorted`. `sort` należy do `List`, porządkuje listę **w miejscu** i nic nie zwraca:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Ponieważ zwraca `void`, nie możesz w ogóle użyć wyniku: `final sorted = numbers.sort();` daje wartość, której kompilator nie pozwala ci odczytać. Idiomem na uporządkowaną **kopię** jest `toList()` z kaskadą `..sort()`: `toList()` tworzy kopię, a `..` wykonuje na niej `sort`, jednocześnie zwracając samą kopię.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], niezmienione
```

`sort` przyjmuje też **komparator**: funkcję dwóch elementów zwracającą liczbę ujemną, gdy pierwszy poprzedza drugi, `0`, gdy są równe, i liczbę dodatnią w przeciwnym razie. `compareTo` produkuje dokładnie to, więc uporządkowanie według dowolnego klucza to jedna linijka:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` i `reduce` wyglądają podobnie, a wybór między nimi sprowadza się do dwóch pytań: czy kolekcja może być pusta i czy wynik ma ten sam typ co elementy?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String z Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int z Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` może zwrócić wyłącznie typ elementu, ponieważ zaczyna od elementu. `fold` zaczyna od wartości, którą wybierasz, więc akumulatorem może być liczący `int`, rosnący `String`, a nawet budowany `List`. A ponieważ ta wartość początkowa już istnieje, pusta kolekcja to po prostu odpowiedź, którą `fold` zwraca bez zmian, podczas gdy `reduce` nie ma czego zwrócić i rzuca wyjątek.

---

Każda z tych metod zwraca `Iterable`, a każdy `Iterable` znów ma te same metody. To pozwala je **łączyć w łańcuchy**: całe obliczenie czyta się jak potok od lewej do prawej, gdzie każdy krok pracuje na tym, co wyprodukował poprzedni.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Tylko ostatni krok potrzebuje `toList()`: wywołanie go w środku zbudowałoby listę, której nikt nie zachowa.

Typ zmienia się wzdłuż łańcucha, a wraz z nim to, co otrzymuje następna funkcja: po `where` na `List<String>` nadal masz ciągi znaków, ale po `map((w) => w.length)` następny krok widzi liczby.

Ponieważ każdy krok jest leniwy, kolejność ma znaczenie dla wykonanej pracy, a nie tylko dla wyniku: filtrowanie najpierw za pomocą `where` oznacza, że `map` jest wywoływane na mniejszej liczbie elementów.

---

Nie ma w tych metodach nic specjalnego: po prostu mają **funkcję jako parametr**, a twoje własne funkcje mogą robić to samo. Typ parametru funkcyjnego zapisuje się jako typ zwracany, następnie `Function`, a potem typy parametrów w nawiasach:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

Wywołujący decyduje, **co** się dzieje, a funkcja decyduje, **na czym**. Zauważ, jak `operation` jest przekazywane prosto do `map`: wartość funkcyjna może być przekazana dalej jak każda inna wartość.

Argumentem może być funkcja anonimowa albo **nazwa** istniejącej funkcji, zapisana bez nawiasów. Dodanie nawiasów wywołałoby ją zamiast jej przekazania:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Funkcja może też **zwracać** funkcję. Typ zwracany zapisuje się dokładnie tak samo jak typ parametru funkcyjnego, a zwracaną wartością jest zwykle funkcja anonimowa:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` niczego nie mnoży: buduje i zwraca nową funkcję, która mnoży przez `3`. Ta funkcja jest potem zapisywana, wywoływana lub przekazywana do `map` jak każda inna:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

Zwrócona funkcja nadal pamięta `factor` po zakończeniu działania `multiplier`. Funkcja, która zachowuje zmienne zakresu, w którym została utworzona, nazywa się **domknięciem** i to właśnie ona umożliwia fabryki funkcji, takie jak ta.

---

Zebrane razem, te metody zastępują większość pętli pisanych ręcznie. Potok zwykle czyta się w trzech etapach: **wybierz** elementy za pomocą `where`, **przekształć** je za pomocą `map`, a następnie **połącz** je za pomocą `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Ponieważ `fold` wybiera własną wartość początkową, może też kończyć łańcuch typem, który nie ma nic wspólnego z elementami, na przykład `String` rosnącym kawałek po kawałku:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Każdy etap pozostaje krótki i mówi, co robi, i to jest prawdziwy powód, aby przedkładać je nad pętlę robiącą wszystkie trzy naraz.
