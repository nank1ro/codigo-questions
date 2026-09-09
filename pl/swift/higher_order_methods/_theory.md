**Funkcja wyższego rzędu** to funkcja, która przyjmuje inną funkcję jako argument, zwraca inną funkcję lub robi jedno i drugie. Już znasz `map`, `filter`, `reduce` i `sorted(by:)`: przyjmują one domknięcie i stosują je do elementów kolekcji. Swift ma ich znacznie więcej, a ich znajomość pozwala zastąpić długie pętle jedną czytelną linią.
`compactMap` działa jak `map`, ale domknięcie zwraca opcjonał, a wyniki `nil` są odrzucane:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` to `nil`, więc ten element znika, a wynikiem jest `[Int]`, a nie `[Int?]`.

---

`flatMap` jest przeznaczony dla domknięć, które zwracają **tablicę**: zamiast budować tablicę tablic, łączy wszystkie zwrócone tablice w jeden płaski wynik:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
Domknięcie może też przekształcić każdą wewnętrzną tablicę przed jej spłaszczeniem, na przykład `teams.flatMap { $0.reversed() }` daje `["Bob", "Ann", "Cid"]`.

---

Trzy warianty `map` różnią się tylko tym, co zwraca domknięcie:
- `map`: dowolną wartość, jeden wynik na element
- `compactMap`: opcjonał, wyniki `nil` są odrzucane
- `flatMap`: tablicę, wszystkie wyniki są łączone w jedną tablicę

Domknięcie przekazane do `flatMap` może samo wywołać `map` na wewnętrznej tablicy, zagnieżdżając jedną transformację w drugiej:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` buduje nową skumulowaną wartość w każdym kroku, co jest marnotrawstwem, gdy wynikiem jest tablica lub słownik. `reduce(into:)` przekazuje domknięciu akumulator jako parametr `inout`, więc może być modyfikowany w miejscu bez `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` tworzy pusty słownik, a `result[word, default: 0]` odczytuje bieżącą liczbę lub `0`, gdy klucz nie istnieje.

---

Niektóre funkcje wyższego rzędu odpowiadają na pytanie o kolekcję, zamiast ją przekształcać. Wszystkie przyjmują domknięcie zwracające `Bool`:
- `first(where:)` zwraca pierwszy element spełniający domknięcie lub `nil`, jeśli takiego nie ma
- `contains(where:)` zwraca `true`, jeśli co najmniej jeden element go spełnia
- `allSatisfy` zwraca `true`, jeśli każdy element go spełnia

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
W przeciwieństwie do `filter`, `first(where:)` zatrzymuje się przy pierwszym dopasowaniu i nie buduje nowej tablicy.

---

`contains(where:)` i `allSatisfy` zastępują częsty wzorzec pętli ze zmienną flagową. Obie zatrzymują się, gdy tylko odpowiedź jest znana: `contains(where:)` przy pierwszym dopasowaniu, `allSatisfy` przy pierwszym elemencie, który go nie spełnia.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` to forma trailing closure dla `contains(where:)`, nie należy jej mylić z `contains(_:)`, która szuka konkretnej wartości.

---

Funkcje wyższego rzędu działają na dowolnych tablicach, także na tablicach twoich własnych struktur. Typowym sposobem wybrania niektórych elementów i wyodrębnienia z każdego z nich wartości jest połączenie w łańcuch `filter`, a następnie `map`:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
Zrobienie tego w odwrotnej kolejności, najpierw `map`, potem `filter`, straciłoby własność `pages`, zanim sprawdzenie mogłoby jej użyć.

---

Gdy domknięcie tylko odczytuje jedną własność, możesz zamiast tego przekazać **key path**: `\.name` oznacza "własność `name` elementu", a `map(\.name)` to to samo co `map { $0.name }`.
Sortowanie według własności używa zwykłego domknięcia dwuargumentowego, porównującego tę własność na obu elementach:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Aby sortować według **więcej niż jednego kryterium**, porównaj pierwszą własność i dopiero gdy pierwsze wartości są równe, sięgnij po drugą:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Tutaj osoby są uporządkowane według wieku, a osoby w tym samym wieku według imienia. Domknięcie musi zwracać `true` tylko wtedy, gdy pierwszy element powinien znaleźć się przed drugim, więc przypadek równości przechodzi do następnego porównania.

---

`enumerated()` zamienia tablicę w sekwencję par `(offset, element)`, dzięki czemu domknięcie może używać pozycji każdego elementu razem z jego wartością:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Ponieważ każda para to krotka, domknięcie może ją również zdestrukturyzować: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` paruje elementy dwóch sekwencji pozycja po pozycji, tworząc sekwencję krotek. Zatrzymuje się na końcu krótszej z nich:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Wewnątrz domknięcia `$0` to element z pierwszej sekwencji, a `$1` ten z drugiej. `zip` to wolna funkcja, a nie metoda: piszesz `zip(a, b)`, a nie `a.zip(b)`.

---

`forEach` to odpowiednik pętli `for-in` wśród funkcji wyższego rzędu: wywołuje domknięcie raz na każdy element, w kolejności. Różnica polega na tym, jak opuszczasz pętlę. W `for-in` możesz użyć `break` lub `continue`; wewnątrz domknięcia `forEach` instrukcje `break` i `continue` nie są dozwolone, a `return` kończy tylko **bieżące wywołanie** domknięcia, po czym następny element jest przetwarzany jak zwykle:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Używaj `forEach` do krótkiego efektu ubocznego na każdym elemencie, a `for-in`, gdy musisz zatrzymać się wcześniej.

---

`Dictionary(grouping:by:)` dzieli kolekcję na słownik tablic. Domknięcie oblicza **klucz** każdego elementu, a wszystkie elementy o tym samym kluczu trafiają do tej samej tablicy:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` przekształca każdą wartość słownika, zachowując przy tym klucze, więc jest naturalnym kolejnym krokiem po grupowaniu:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` pobiera elementy od początku **dopóki** domknięcie zwraca `true` i zatrzymuje się na pierwszym elemencie, który go zawodzi, nawet jeśli późniejsze elementy przeszłyby ponownie. `drop(while:)` jest jego uzupełnieniem: pomija dokładnie ten początkowy ciąg i zwraca całą resztę:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Obie zwracają `ArraySlice`, widok na oryginalną tablicę, który wypisuje się jak tablica i można go zamienić w tablicę za pomocą `Array(...)`.

---

Możesz pisać własne funkcje wyższego rzędu. Funkcja, która przyjmuje domknięcie i **zwraca nowe domknięcie** zbudowane na jego podstawie, to częsty wzorzec: zwrócone domknięcie przechwytuje oryginalne, więc parametr musi być `@escaping`.
Na przykład `negate` zamienia predykat w jego przeciwieństwo, gotowy do przekazania do `filter`:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Zauważ, że `filter(negate(isEven))` przekazuje domknięcie jako zwykły argument, bez składni trailing closure.

---

`map` i `filter` na tablicy są **gorliwe**: każda z nich przetwarza całą tablicę i buduje nową, zanim uruchomi się kolejny krok. Na dużej kolekcji, albo gdy potrzebujesz tylko pierwszego wyniku, to zmarnowana praca.
Własność `lazy` zwraca widok, którego operacje działają dopiero wtedy, gdy element jest faktycznie żądany, po jednym elemencie w całym łańcuchu:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Tutaj tylko `1, 2, ..., 8` zostają podniesione do kwadratu: `first(where:)` żąda elementów, dopóki jeden nie spełni warunku, i tam łańcuch się zatrzymuje. Bez `lazy` `map` podniosłaby najpierw do kwadratu wszystkie 1000 liczb.
