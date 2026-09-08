Wiesz już, jak zadeklarować funkcję z nazwą, np. `void sayHello() { ... }`. Dart pozwala też pisać funkcję **bez nazwy**: **funkcję anonimową**. Ma te same części co funkcja nazwana (parametry w nawiasach okrągłych i ciało w nawiasach klamrowych), ale nie ma typu zwracanego ani nazwy:

```dart
(String name) {
  print('Hello, $name!');
}
```

Ponieważ nie ma nazwy, zwykłym sposobem jej użycia jest zapisanie jej w zmiennej, a następnie wywołanie zmiennej jak funkcji:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Zwróć uwagę na `;` po nawiasie zamykającym: przypisanie jest zwykłą instrukcją.

---

Funkcja anonimowa może przyjmować parametry i zwracać wartość za pomocą `return`, dokładnie jak funkcja nazwana. Typu zwracanego się nie pisze: Dart **wnioskuje** go z instrukcji `return` w ciele funkcji.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Gdy ciało jest pojedynczym wyrażeniem, funkcja anonimowa może użyć **składni strzałki** `=>`, tak jak funkcja nazwana. Strzałka zastępuje nawiasy klamrowe i słowo kluczowe `return`:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Ta krótka forma jest zdecydowanie najczęstszym sposobem pisania funkcji anonimowych w Dart.

---

Funkcje są wartościami, więc mają typ. Typ funkcji zapisuje się jako **typ zwracany**, następnie słowo kluczowe `Function`, a potem **typy parametrów** w nawiasach okrągłych:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Gdy zmienna jest w ten sposób otypowana, typy parametrów można pominąć w funkcji anonimowej, ponieważ Dart wnioskuje je z zadeklarowanego typu:

```dart
int Function(int, int) add = (a, b) => a + b;
```

Sam typ `Function` akceptuje dowolną funkcję, niezależnie od jej parametrów i typu zwracanego, ale nie mówi Dart nic o tym, jak ją wywołać.

---

Ponieważ typ funkcyjny jest zwykłym typem, funkcja może przyjmować **inną funkcję jako parametr**. W ciele funkcji parametr wywołuje się jak każdą inną funkcję:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Tutaj wywołujący decyduje, co robi `apply`, przekazując anonimową funkcję jako drugi argument.

---

Wiele metod kolekcji Dart przyjmuje funkcję jako argument, a funkcje anonimowe to naturalny sposób jej przekazania. Najprostszą jest `forEach`, która wywołuje podaną funkcję raz dla każdego elementu listy:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

Typ parametru jest wnioskowany z listy, więc `fruit` jest `String` bez konieczności jego zapisywania.

---

Dwie inne bardzo częste metody przyjmujące funkcję anonimową to `map` i `where`:

- `map` przekształca każdy element za pomocą funkcji i zwraca nowe wartości
- `where` zachowuje tylko te elementy, dla których funkcja zwraca `true`

Obie zwracają leniwe `Iterable`; wywołaj `toList()`, aby zamienić wynik w `List`:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Ponieważ `map` i `where` zwracają `Iterable`, ich wywołania można **łączyć w łańcuch** jedno po drugim. Każdy krok otrzymuje wynik poprzedniego, a `toList()` jest wywoływane raz na końcu:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` porządkuje listę w miejscu. Domyślnie używa naturalnej kolejności elementów, ale można przekazać funkcję anonimową, która **porównuje dwa elementy** i zwraca liczbę ujemną, zero lub liczbę dodatnią. `compareTo` daje dokładnie taką liczbę, dlatego jest to typowy element składowy:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Zamiana `a` i `b` w porównaniu odwraca kolejność.

---

`reduce` łączy wszystkie elementy listy w jedną wartość. Jej funkcja anonimowa przyjmuje dwa parametry: wartość **dotychczas zakumulowaną** i **następny element**, i zwraca nową zakumulowaną wartość. Pierwszy element jest używany jako punkt startowy:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` zgłasza błąd dla pustej listy, ponieważ nie ma pierwszego elementu, od którego można zacząć.

---

Funkcja może też **zwracać funkcję**. Typ zwracany jest wtedy typem funkcyjnym, a ciało zwraca funkcję anonimową:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Zauważ, że zwrócona funkcja nadal używa `amount`, parametru `makeAdder`, nawet po zakończeniu działania `makeAdder`. Funkcja, która w ten sposób zapamiętuje otaczające ją zmienne, nazywana jest **domknięciem**.

---

Domknięcie nie tylko odczytuje przechwycone zmienne: może je też **modyfikować**, a zmiany są zachowywane między wywołaniami. Dzięki temu można przechowywać prywatny stan bez klasy:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Każde wywołanie `makeTimer()` tworzy zupełnie nową zmienną `seconds`, więc dwa zegary nigdy nie współdzielą swojego licznika.
