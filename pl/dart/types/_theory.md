Typy pozwalają kategoryzować różne typy danych używane w kodzie.
W Dart __typ__ to sposób informowania kompilatora, jak zamierzasz używać danego fragmentu danych.
Oto przykłady typów obsługiwanych przez Dart:
- int
- String
- double
- dynamic
- num

Dart obsługuje wiele innych typów. Wymienione powyżej to główne, których będziesz używać.

---

Możesz jawnie zdefiniować typ zmiennej, na przykład:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Zmienne z jawnym typem mogą być również stałymi, wystarczy dodać słowo kluczowe `const` lub `final` przed typem:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Uwaga: Dane mutowalne pozwalają na łatwą zmianę w dowolnym momencie. Jednak wielu doświadczonych programistów docenia zalety danych niezmiennych. Kiedy wartość jest niezmienna, możesz mieć pewność, że nikt nie będzie mógł jej zmienić po jej utworzeniu. Ograniczenie danych w ten sposób zapobiega wielu trudnym do wykrycia błędom i sprawia, że program jest łatwiejszy do przemyślenia i przetestowania.

---

Choć możliwe jest podanie typu zmiennej, jest to zbędne. Wiesz, że `10` jest typu `int`, a `3.14` jest typu `double`. Kompilator Dart jest w stanie to wywnioskować dzięki __wnioskowaniu o typie__. Nie wszystkie języki programowania posiadają _wnioskowanie o typie_, co czyni Dart bardzo potężnym językiem programowania.

Możesz po prostu usunąć typ ze zmiennych, na przykład:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

Gdy typ zmiennej nie jest jawnie podany, Dart spróbuje wywnioskować jej typ.

---

Istnieje programistyczny sposób sprawdzenia typu zmiennej, mianowicie za pomocą słowa kluczowego `is`:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

Jak widać, Dart przypisał typ `double` do zmiennej `number`.

---

Słowo kluczowe `is` pozwala sprawdzić, czy zmienna jest określonego typu. Możesz
 również sprawdzić, czy zmienna nie jest określonego typu za pomocą słowa kluczowego `is!`
```dart
final number = 3.14;
print(number is! int); // true
```

---

Inną opcją sprawdzenia typu zmiennej _runtime_ jest użycie właściwości `runtimeType`, która jest dostępna dla wszystkich typów.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

Czasami znajdziesz się w sytuacji, gdy masz jeden typ, ale musisz go przekonwertować na inny. Możesz być skuszony, aby zrobić:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

Ale Dart zgłosi błąd:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Niektóre języki programowania nie są tak restrykcyjne i będą konwertować cicho. Doświadczenie pokazuje, że tego rodzaju cicha niejawna konwersja jest częstym źródłem błędów i problemów z wydajnością. Dart wyłączył tę funkcję, aby uniknąć tych problemów.

Pamiętaj, że komputery polegają na programistach, aby dowiedzieć się, co robić. W Dart obejmuje to jawne określenie, jakiego typu konwersji chcesz. Oto jak przekonwertować liczbę `double` na `int`:
```dart
var integer = decimal.toInt();
```

Przypisanie jednoznacznie mówi Dart, że chcesz przekonwertować z oryginalnego typu `double` na nowy typ `double`.

> UWAGI: W tym przypadku przypisanie wartości dziesiętnej do liczby całkowitej powoduje utratę precyzji. Zmienna `integer` ma wartość __3__ zamiast __3.14__. Dlatego ważne jest, aby być precyzyjnym. Dart chce mieć pewność, co robisz i informuje, że stracisz informacje podczas konwersji.

---

Do tej pory widzieliśmy operatory używane niezależnie na liczbach całkowitych lub dziesiętnych. Co jeśli masz
liczbę całkowitą i musisz ją pomnożyć przez liczbę dziesiętną? Zobaczmy przykład:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` jest typu `int`, a `pi` jest typu `double`. Jaki będzie typ `circumference`? Dart przypisze typ `double` do zmiennej `circumference`. Jest to bezpieczniejszy wybór, ponieważ gdybym zrobił ją typu `int`, mogłoby to spowodować utratę precyzji.

Jeśli chcesz uzyskać `int` jako wynik, musisz dokonać konwersji jawnie:
```dart
const circumference = (2 * pi * radius).toInt();
```

Nawiasy mówią Dart, aby najpierw pomnożył, a następnie wziął wynik i przekonwertował go na wartość całkowitą. Niestety analizator nie spodoba się ten kod:
 > Const variables must be initialized with a constant value.

Problem polega na tym, że metoda `toInt` jest metodą tylko czasu wykonania. Oznacza to, że zmienna `circumference` nie może zostać określona w czasie kompilacji, więc nie jest możliwe, aby zmienna była stałą. Aby naprawić, zastąp `const` przez `final`:

```dart
final circumference = (2 * pi * radius).toInt();
```

Teraz `circumference` jest zmienną __stałą czasu wykonania__ typu `int`.

---

Czasami możesz mieć zmienną z typem ogólnym, ale potrzebujesz funkcjonalności, która istnieje tylko w podtypie. Jeśli jesteś pewien, że typ zmiennej to potrzebny podtyp, możesz użyć słowa kluczowego `as`, aby zmienić jej typ. Ta procedura jest również znana jako __rzutowanie typów__, oto przykład:

```dart
num number = 3;
```

Powiedzmy, że chcemy sprawdzić, czy liczba jest parzysta, a dana funkcjonalność jest obecna tylko w podtypie `int`.
```dart
print(number.isEven);
```

Powyższy kod powinien zwrócić błąd typu:
> The getter `isEven` isn't defined for the type 'num'.

Typ `num` jest zbyt ogólnym typem, aby wiedzieć, czy liczba jest parzysta, czy nieparzysta. Tylko liczby całkowite mogą być parzyste lub nieparzyste.
Problem pojawia się, gdy `num` zawiera wartość `double`, ponieważ `num` zawiera zarówno typy `double`, jak i `int`. W tym przypadku jesteśmy pewni, że __3__ jest liczbą całkowitą, więc możemy rzutować na `int`

```dart
final integer = number as int;
print(integer.isEven); // false
```

Słowo kluczowe `as` powoduje, że kompilator rozpoznaje zmienną `integer` jako mającą typ `int`. Pozwala to na użycie właściwości `isEven`, która jest obecna w liczbach całkowitych. Ponieważ liczba __3__ nie jest liczbą całkowitą, wynik to false.

Musisz uważać przy rzutowaniu. Jeśli niepoprawnie rzutujesz typ, otrzymasz błąd czasu wykonania:
```dart
num numero = 3;
final decimale = numero as double;
```

Spowoduje to awarię programu z następującym błędem:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

Typ czasu wykonania `number` to `int`, a nie `double`. W Dart nie możesz rzutować między typami tego samego poziomu, takimi jak `int` i `double`. Możesz rzutować tylko podtypy.
