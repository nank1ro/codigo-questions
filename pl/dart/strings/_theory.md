**String** to fragment tekstu: ciąg znaków ujęty w cudzysłowy. W Dart możesz używać pojedynczych cudzysłowów `'...'` lub podwójnych `"..."`, działają one dokładnie tak samo:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Wybranie jednego rodzaju cudzysłowu pozwala używać drugiego rodzaju wewnątrz tekstu bez żadnego escapowania:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Jeśli potrzebujesz tego samego cudzysłowu wewnątrz tekstu, poprzedź go ukośnikiem wstecznym: `'It\'s sunny'`.

---

Dwa ciągi znaków można połączyć w nowy za pomocą operatora `+`, zwanego **konkatenacją**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart łączy też dwa **literały** ciągu znaków zapisane obok siebie, bez żadnego operatora. Jest to przydatne przy dzieleniu długiego tekstu na kilka linii:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Tylko ciągi znaków mogą być łączone za pomocą `+`: `'Age: ' + 30` to błąd kompilacji, ponieważ `30` jest typu `int`.

---

Zamiast konkatenacji, możesz wstawiać wartości bezpośrednio do ciągu znaków za pomocą **interpolacji**. Napisz `$name`, aby wstawić wartość zmiennej, oraz `${expression}`, aby wstawić wynik dowolnego wyrażenia:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

Interpolacja działa z każdym typem: liczby, wartości logiczne i listy są automatycznie konwertowane na tekst, więc `'Age: $age'` jest poprawne, mimo że `age` jest typu `int`.

---

Każdy ciąg znaków wie, ile znaków zawiera, dzięki właściwości `.length`. Spacje i znaki interpunkcyjne również liczą się jako znaki:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Możesz odczytać pojedynczy znak za pomocą nawiasów kwadratowych i jego **indeksu**, zaczynając od `0`. Wynikiem jest jednoznakowy `String`:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Odczytanie indeksu spoza ciągu znaków (jak `word[5]`) zgłasza błąd.

---

Ciągi znaków w Dart są **niemutowalne**: raz utworzony ciąg znaków nigdy się nie zmienia. Metody takie jak `.toUpperCase()` i `.toLowerCase()` nie modyfikują oryginalnego ciągu znaków, **zwracają nowy**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Jeśli chcesz, aby zmienna przechowywała nową wartość, przypisz wynik z powrotem do niej: `word = word.toUpperCase();`.

---

Tekst wpisywany przez użytkownika często ma dodatkowe spacje wokół siebie. Metoda `.trim()` zwraca kopię ciągu znaków bez początkowych i końcowych białych znaków (spacji, tabulacji i znaków nowej linii). `.trimLeft()` i `.trimRight()` usuwają je tylko z jednej strony:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

Metoda `.substring(start, end)` zwraca fragment ciągu znaków od indeksu `start` do indeksu `end`, **bez jego uwzględnienia**. Jeśli pominiesz `end`, zwrócony zostanie fragment aż do końca ciągu:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Kilka metod pozwala wyszukiwać wewnątrz ciągu znaków:

- `.contains(other)` zwraca `true`, jeśli `other` występuje gdziekolwiek w ciągu znaków
- `.startsWith(other)` i `.endsWith(other)` sprawdzają początek i koniec
- `.indexOf(other)` zwraca indeks pierwszego wystąpienia lub `-1`, jeśli nie zostanie znalezione

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Wszystkie z nich rozróżniają wielkość liter: `'Dart'.contains('dart')` to `false`.

---

Metoda `.replaceAll(from, to)` zwraca nowy ciąg znaków, w którym **każde** wystąpienie `from` jest zastąpione przez `to`. `.replaceFirst(from, to)` zastępuje tylko pierwsze wystąpienie:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

Metoda `.split(separator)` dzieli ciąg znaków na `List<String>` przy każdym wystąpieniu separatora. Odwrotnością jest `.join(separator)`, metoda list, która skleja elementy w jeden ciąg znaków:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Wywołanie `.split('')` z pustym separatorem zwraca listę z każdym pojedynczym znakiem.
