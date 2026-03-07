Zmienne to kontenery do przechowywania wartości.
Każda zmienna w Dart jest obiektem (`Object`).
Aby utworzyć zmienną, musimy nadać jej __nazwę__, pamiętając, że nie może zawierać spacji.
Przyjrzyj się poniższemu:

```dart
int number = 1;
```

Ta instrukcja deklaruje zmienną o nazwie `number` typu `int`.
Następnie ustawia wartość zmiennej na liczbę `1`.
Część `int` deklaracji jest znana jako __adnotacja typu__ i jawnie mówi Dart, jakiego typu jest zmienna.

---

W poprzednim przykładzie widzieliśmy tworzenie zmiennej:

```dart
int number = 1;
```

Nie daj się zmylić symbolem `=`.
Nie jest to symbol równości jak w matematyce, ale jest znany jako __operator przypisania__, ponieważ przypisuje wartość zmiennej.
Znak równości natomiast to `==`.

---

Jeśli chcesz zmienić wartość zmiennej, po prostu przypisz jej inną wartość tego samego typu:

```dart
int number = 1;
number = 2;
```

---

Typ `int` pozwala przechowywać liczby całkowite.
Aby zamiast tego zapisać liczby dziesiętne, możemy użyć typu `double`:

```dart
double pi = 3.14159;
```

Ten przykład jest podobny do poprzedniego. Tym razem jednak zmienna jest typu `double`, który pozwala przechowywać liczby dziesiętne z wysoką precyzją.

---

Dart jest językiem __bezpiecznym pod względem typów__.
Oznacza to, że gdy przypisujesz typ do zmiennej, nie możesz go później zmienić. Oto przykład:

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

`3.14159` jest typu `double`, ale już zdefiniowałeś `integerNumber` z typem `int`.

Oczywiście, czasami może być przydatne przypisanie powiązanych typów do tej samej zmiennej. Na przykład możesz chcieć zmiennej `integerNumber`, która akceptuje zarówno liczby `int`, jak i `double`, jak tutaj:

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

Zarówno `int`, jak i `double` rozszerzają `num`, więc oba typy są akceptowane.
Jednak jeśli spróbujemy przypisać `String`, kompilator zwróci błąd.

---

Jeśli lubisz ryzyko, możemy całkowicie zignorować __bezpieczeństwo typów__ języka, używając typu `dynamic`.
Pozwala to przypisać dowolny typ wartości do zmiennej.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

To podejście jest zdecydowanie odradzane, ponieważ błędy nie są już przechwytywane przez _analizator_ kodu, ale tylko w _czasie wykonania_ (gdy program działa).

---

Dart obsługuje __wnioskowanie o typie__.
Nie jest konieczne podawanie typu zmiennej, ponieważ Dart może wywnioskować jej typ.
Słowo kluczowe `var` mówi Dart, aby użył najbardziej odpowiedniego typu.

```dart
var number = 5;
```

Nie jest konieczne informowanie Dart, że liczba `5` jest typu `int`.
Dart wnioskuje typ i sprawia, że `number` jest typu `int`.

---

Dart obsługuje dwa różne typy "_zmiennych_", których wartość nigdy się nie zmienia. Są one deklarowane za pomocą słów kluczowych `const` i `final`.
Zacznijmy od zobaczenia, co oznacza `const`.

## const (stałe)

Zmienne, których wartość można zmieniać, są znane jako __dane mutowalne__. Dane mutowalne są często nadużywane i mogą powodować problemy. Łatwo jest stracić kontrolę nad wszystkimi miejscami w kodzie, które mogą zmienić wartość zmiennej.

Z tego powodu powinieneś używać `const`ant zamiast `var`iables, gdy tylko jest to możliwe. Te zmienne, których wartość nie może się zmieniać, są również nazywane __danymi niemutowalnymi__.

Aby stworzyć stałą w Dart, używamy słowa kluczowego `const`:

```dart
const number = 5;
```

Podobnie jak `var`, Dart z __wnioskowaniem o typie__ określa, że `number` jest typu `int`.

---

Gdy zadeklarowałeś stałą zmienną, nie możesz już zmieniać jej wartości. Na przykład:

```dart
const number = 2;
number = 3; // Error
```

Ten kod powoduje błąd:
> Constant variables can't be assigned a value.

Oznacza to, że nie jest możliwa zmiana wartości stałej zmiennej.

---

Często znajdziesz się w sytuacji, gdy chcesz użyć stałej, ale nie znasz wartości w czasie kompilacji. Poznasz ją dopiero po uruchomieniu programu.
Ten typ stałej jest znany jako __stała czasu wykonania__.

W Dart `const` jest używane tylko dla __stałych czasu kompilacji__ dla wartości, które mogą być określone przez kompilator przed uruchomieniem programu.

Jeśli nie możesz utworzyć stałej zmiennej, ponieważ nie znasz jej wartości w czasie kompilacji, musisz użyć słowa kluczowego `final`, aby uczynić zmienną __stałą czasu wykonania__.

Istnieje wiele powodów, dla których nie możesz znać wartości zmiennej przed uruchomieniem programu. Na przykład musiałbyś pobrać wartość z serwera lub poprosić użytkownika o jej podanie.

---

Oto przykład wartości, którą można uzyskać tylko w czasie wykonania:

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` to funkcja pobierająca bieżącą datę i godzinę wykonania kodu.
Za pomocą pola `hour` uzyskujemy liczbę godzin, które upłynęły od początku dnia.

Ponieważ wartość `hour` jest różna w zależności od tego, kiedy kod jest wykonywany, można to zdefiniować jako wartość _runtime_.

Jeśli spróbujesz zmienić wartość zmiennej `final`, otrzymasz błąd.
