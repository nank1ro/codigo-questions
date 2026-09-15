**Wyrażenie regularne** (regex) to mały wzorzec, który opisuje kształt tekstu: „ciąg cyfr", „słowo, po którym następuje znak równości", „trzy wielkie litery". Zamiast pisać pętle po znakach, opisujesz kształt raz i pozwolasz Swiftowi go znaleźć.

Swift zapisuje wyrażenie regularne między `#/` i `/#`:
```swift
let digits = #/\d+/#
```
We wzorcu `\d` oznacza „dowolną cyfrę", a `+` oznacza „jedną lub więcej wystąpień poprzedniego elementu", więc `\d+` oznacza „ciąg jednej lub więcej cyfr".

Najprostsze pytanie, jakie możesz zadać, brzmi: czy tekst zawiera dopasowanie. `contains(_:)` przyjmuje wyrażenie regularne i zwraca `Bool`:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
Zawsze używaj pokazanej tutaj postaci `#/ ... /#`: krótszy zapis `/ ... /` myli kompilator, gdy wzorzec jest zapisany bezpośrednio wewnątrz wywołania metody.

---

Kilka skrótów pokrywa większość wzorców. Każdy z nich dopasowuje dokładnie **jeden** znak:
- `\d` to jedna cyfra
- `\w` to jedna litera, cyfra lub podkreślnik
- `\s` to jedna spacja, tabulator lub znak nowej linii
- `.` to dowolny pojedynczy znak

Aby dopasować więcej niż jeden znak, dodaj **kwantyfikator** bezpośrednio po wzorcu:
- `+` oznacza jedną lub więcej
- `*` oznacza zero lub więcej
- `?` oznacza zero lub jedną

Więc `\w+` to słowo, `\s*` to opcjonalne odstępy, a `\d?` to opcjonalna cyfra:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
Znak bez specjalnego znaczenia po prostu dopasowuje sam siebie, więc `#/cat/#` dopasowuje trzy litery `cat`.

---

Domyślnie wzorzec może pasować gdziekolwiek wewnątrz tekstu. **Kotwice** wiążą go zamiast tego z pozycją:
- `^` oznacza „początek tekstu"
- `$` oznacza „koniec tekstu"

```swift
print("swift".contains(#/^sw/#))  // true, tekst zaczyna się od sw
print("myswift".contains(#/^sw/#)) // false, sw nie znajduje się na początku
print("swift".contains(#/ft$/#))  // true, tekst kończy się na ft
```
Kotwice dopasowują pozycję, a nie znak, więc nic nie dodają do zawartości dopasowania.

---

Gdy żaden ze skrótów nie pasuje, wypisz akceptowane znaki w nawiasach kwadratowych. `[abc]` dopasowuje jedno `a`, jedno `b` lub jedno `c`, a myślnik zapisuje zakres:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
Liczba w nawiasach klamrowych mówi dokładnie, ile razy powtarza się poprzedni wzorzec: `{3}` oznacza trzy razy, `{2,4}` oznacza od dwóch do czterech razy:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
Otaczanie wzorca w `^` i `$` z licznikiem to zwykły sposób sprawdzenia, czy cały tekst ma dany kształt.

---

`contains(_:)` odpowiada tylko tak lub nie. Aby otrzymać dopasowany tekst, użyj `firstMatch(of:)`. Zwraca ono **opcjonalne dopasowanie**: `nil`, gdy nic nie pasowało, więc naturalnie łączy się z `if let`.

Dopasowany tekst jest przechowywany we właściwości `0` dopasowania, zapisywanej jako `m.0`:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)` zatrzymuje się na pierwszym dopasowaniu, nawet gdy tekst zawiera więcej.

---

`m.0` nie jest `String`, lecz `Substring`: widokiem oryginalnego tekstu, a nie kopią. Wypisuje się dokładnie jak ciąg znaków, ale tam, gdzie wymagany jest `String`, musisz go przekonwertować:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
Inicjalizatory liczb przyjmują `Substring` bezpośrednio, więc `Int(m.0)` działa bez tej dodatkowej czynności.

---

`matches(of:)` zwraca **wszystkie** dopasowania zamiast pierwszego, w postaci tablicy. Ta tablica nigdy nie jest `nil`: gdy nic nie pasuje, jest po prostu pusta, więc można od razu po niej iterować lub ją przekształcać:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
Każdy element to dopasowanie, więc `$0.0` wewnątrz `map` to dopasowany tekst:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

Ponieważ `Int(_:)` przyjmuje `Substring`, zamiana znalezionego tekstu na liczby to jeden krok. `compactMap` sprawdza się tutaj doskonale: odrzuca wartości, które wychodzą jako `nil`:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
Używaj `map`, gdy każdy element da się przekonwertować, a `compactMap`, gdy niektóre mogą się nie udać.

---

Okrągłe nawiasy wokół części wzorca tworzą **grupę przechwytującą**: całe dopasowanie to nadal `m.0`, a część wewnątrz nawiasów staje się `m.1`:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
W ten sposób zachowujesz interesujący fragment i wyrzucasz otaczający go tekst. Bez nawiasów nie ma w ogóle `m.1`, a kod się nie kompiluje.

---

Wzorzec może zawierać kilka grup. Są numerowane od lewej do prawej według ich nawiasu otwierającego, więc druga to `m.2`, trzecia `m.3` i tak dalej:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
`m.0` zawsze pozostaje całym dopasowaniem, niezależnie od liczby grup.

---

Liczenie nawiasów staje się kruche, gdy tylko wzorzec urośnie. Nadaj grupie zamiast tego **nazwę**, pisząc `?<name>` zaraz po jej nawiasie otwierającym, i odczytuj ją jako właściwość dopasowania:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
Grupy nazwane nadal mają numery, więc `m.1` dalej działa, ale `m.key` mówi, co przechowuje, i przetrwa zmianę wzorca.

---

`replacing(_:with:)` zamienia każde dopasowanie na ustalony tekst i zwraca nowy `String`, zostawiając oryginał nietknięty:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
Zwróć uwagę, że `\d+` zamienia cały ciąg cyfr na jeden `#`, podczas gdy `\d` zamieniałoby po jednej cyfrze naraz. To wzorzec decyduje, jak dużo znika.

---

`split(separator:)` przyjmuje również wyrażenie regularne, dzięki czemu jedno wywołanie obsłuży separatory, które nie zawsze są zapisane tak samo:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
Wzorzec `[,;]\s*` oznacza "przecinek lub średnik, po którym następuje dowolna liczba znaków odstępu", więc każdy separator jest pochłaniany w całości i nie powstaje puste pole. Wynikiem jest tablica `Substring`.

---

Sprawdzanie całego tekstu za pomocą `^` i `$` działa, ale `wholeMatch(of:)` mówi to wprost: zwraca dopasowanie tylko wtedy, gdy wzorzec pokrywa tekst od pierwszego do ostatniego znaku, a w przeciwnym razie `nil`:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
Używaj `firstMatch(of:)`, aby znaleźć coś wewnątrz tekstu, a `wholeMatch(of:)`, aby sprawdzić, czy tekst ma dokładnie jeden konkretny kształt.

---

Literał `#/ ... /#` jest ustalony w chwili kompilacji. Gdy wzorzec poznajesz dopiero w trakcie działania programu, na przykład dlatego, że wpisał go użytkownik, zbuduj go za pomocą `Regex(_:)`:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
Ten inicjalizator **rzuca wyjątek**: nieprawidłowy wzorzec taki jak `"["` zostaje wykryty dopiero podczas działania programu, więc wywołanie wymaga `try`, a błąd trzeba albo obsłużyć przez `do`/`catch` (lub `try?`), albo przekazać dalej, oznaczając otaczającą funkcję jako `throws`, tak jak robi to to ćwiczenie. Wyrażenie regularne zbudowane w ten sposób nie ma numerowanych właściwości znanych w czasie kompilacji, ale `contains`, `matches(of:)` i `replacing` działają dokładnie tak samo jak wcześniej.
