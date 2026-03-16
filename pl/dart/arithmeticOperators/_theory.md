Operator **dodawania** `+` dodaje dwie wartości razem.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Możesz używać `+` z wartościami `int` lub `double`.

---

Operator **odejmowania** `-` odejmuje jedną wartość od drugiej.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

Wynik może być ujemny, jeśli drugi operand jest większy niż pierwszy.

---

Operator **mnożenia** `*` mnoży dwie wartości razem.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Mnożenie `int` przez inny `int` daje `int`. Mnożenie z `double` daje `double`.

---

Operator **dzielenia** `/` dzieli jedną wartość przez drugą. W Dart `/` **zawsze zwraca `double`**, nawet gdy wynik jest liczbą całkowitą.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (nie 5!)
```

Zawsze używaj zmiennej `double` do przechowywania wyniku `/`.

---

Operator **dzielenia całkowitego** `~/` dzieli dwie liczby i **obcina** wynik do liczby całkowitej (odrzuca część dziesiętną).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (nie 3.333...)
```

Używaj `~/` gdy potrzebujesz ilorazu będącego liczbą całkowitą bez reszty.
