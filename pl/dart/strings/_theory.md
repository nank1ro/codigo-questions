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

---

Niektórych znaków nie można wpisać bezpośrednio wewnątrz cudzysłowów. **Sekwencje escape** zaczynają się od ukośnika wstecznego: `\n` to nowa linia, `\t` to tabulator, `\\` to ukośnik wsteczny, a `\$` to dosłowny znak dolara (w przeciwnym razie `$` rozpoczyna interpolację):

```dart
print('one\ntwo');   // wypisuje one i two w osobnych liniach
print('Cost: \$5');  // Cost: $5
```

**Raw string** jest poprzedzony literą `r`: wewnątrz niego ukośniki wsteczne i `$` są zwykłymi znakami, nic nie jest escapowane ani interpolowane:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

Dla tekstu obejmującego kilka linii użyj **ciągu wieloliniowego** ograniczonego potrójnymi cudzysłowami `'''` lub `"""`: podziały linii wewnątrz niego są zachowywane.

```dart
var poem = '''
roses are red
violets are blue''';
```

---

Pod spodem każdy znak ciągu jest przechowywany jako liczba, jego **code unit** (kod UTF-16). `.codeUnitAt(index)` zwraca kod jednego znaku, a `.codeUnits` zwraca całą listę. `String.fromCharCode(code)` robi coś odwrotnego, budując ciąg znaków z kodu:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

Kolejne litery mają kolejne kody: `'A'` to 65, `'B'` to 66 i tak dalej.

---

Dwa ciągi znaków są równe za pomocą `==`, gdy zawierają dokładnie te same znaki w tej samej kolejności. Porównanie **rozróżnia wielkość liter** i liczy każdą spację:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

Aby porównać, ignorując wielkość liter, przekonwertuj najpierw obie strony: `a.toLowerCase() == b.toLowerCase()`. Do porządkowania `.compareTo(other)` zwraca liczbę ujemną, `0` lub liczbę dodatnią, w zależności od tego, czy ciąg znaków jest wcześniejszy, równy czy późniejszy od drugiego.

---

Ponieważ ciągi znaków są niemutowalne, budowanie długiego tekstu za pomocą `+=` w pętli tworzy nowy ciąg znaków przy każdym kroku. **StringBuffer** zbiera fragmenty tekstu w wydajny sposób i tworzy końcowy ciąg znaków dopiero wtedy, gdy o to poprosisz:

- `.write(value)` dołącza wartość (dowolny typ jest konwertowany na tekst)
- `.writeln(value)` dołącza wartość, a po niej znak nowej linii
- `.toString()` zwraca ciąg znaków zbudowany do tej pory

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

Metody ciągów znaków zwracają ciągi znaków, więc można je **łączyć w łańcuch**, jedną po drugiej. W połączeniu z `.split('')`, właściwością list `.reversed` i `.join()` pozwala to odwrócić ciąg znaków w jednym wyrażeniu:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

**Palindrom** to tekst, który czyta się tak samo od przodu i od tyłu, na przykład `level`.
