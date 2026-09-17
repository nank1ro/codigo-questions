**Struktura** (od *structure*) to typ, który projektujesz samodzielnie, aby trzymać powiązane wartości razem. Zamiast żonglować osobnym `title` i osobnym `pages`, opisujesz `Book` raz i używasz go wszędzie.

Deklarujesz ją słowem kluczowym `struct`, a zmienne zapisane w jej środku to jej **właściwości przechowywane**:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` jest teraz typem, dokładnie takim samym jak `Int` czy `String`. Do właściwości instancji odwołujesz się kropką:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Nigdy nie napisałeś kodu, który tworzy `Book`, a jednak `Book(title: "Swift", pages: 120)` zadziałało. Swift pisze go za ciebie: każda struktura dostaje za darmo **inicjalizator memberwise**, czyli inicjalizator, którego parametrami są jego właściwości przechowywane, w kolejności ich deklaracji, a każdy z nich używa nazwy właściwości jako swojej etykiety argumentu:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Klasy nie dostają tego za darmo i jest to jeden z powodów, dla których struktury są najszybszym sposobem modelowania wartości.

---

Właściwości przechowywanej można nadać **wartość domyślną** dokładnie w miejscu jej deklaracji. Swift wywnioskuje jej typ z tej wartości, więc możesz pominąć adnotację typu:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
Inicjalizator memberwise zamienia każdą właściwość z wartością domyślną na argument opcjonalny: przekaż go, aby nadpisać wartość domyślną, lub pomiń, aby ją zachować.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Struktura może też zawierać **metody**: funkcje zapisane wewnątrz klamer, które działają na instancji, na której są wywoływane. Wewnątrz metody używasz nazw właściwości bezpośrednio, bez żadnego prefiksu:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
Jeśli parametr metody przesłania nazwę właściwości, napisz `self.width`, aby oznaczyć właściwość instancji.

---

**Właściwość obliczeniowa** wygląda jak właściwość, ale zachowuje się jak metoda: niczego nie przechowuje, oblicza swoją wartość za każdym razem, gdy ją odczytujesz. Piszesz typ, a następnie blok kodu, który zwraca wartość:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, bez nawiasów
```
Właściwości obliczeniowe nie są częścią inicjalizatora memberwise, ponieważ nie ma nic do przechowania. Używaj ich, gdy wartość jest wyliczana z innych, a metodę, gdy praca wymaga parametrów.

---

Struktura to **typ wartościowy**: przypisanie jej do innej zmiennej albo przekazanie do funkcji przekazuje *kopię*. Zmiana kopii pozostawia oryginał nietkniętym.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Klasa to **typ referencyjny**: `b = a` sprawiłoby, że obie nazwy wskazywałyby tę samą instancję, więc `b.x = 99` zmieniłoby też `a.x` na `99`.

To jest prawdziwa różnica między nimi i powód, dla którego Swift modeluje większość danych jako struktury: wartość, którą trzymasz, nie może zostać zmieniona za twoimi plecami przez kod, który ją otrzymał.

---

Ponieważ struktura jest wartością, metoda nie może zmieniać jej właściwości, chyba że powiesz o tym słowem kluczowym `mutating`:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
Metodę mutating można wywołać tylko na instancji przechowywanej w `var`. Na instancji `let` wartość jest zamrożona, więc `c.increase(by: 5)` nie skompilowałoby się.

---

Gdy inicjalizator memberwise nie jest sposobem, w jaki chcesz tworzyć swój typ, napisz własny **inicjalizator**. Deklaruje się go słowem `init`, przyjmuje parametry, które wybierzesz, i musi nadać wartość każdej właściwości przechowywanej przed swoim zakończeniem. Wewnątrz niego `self` to tworzona instancja:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Napisanie `init` wewnątrz klamer struktury zastępuje inicjalizator memberwise, więc od tej chwili `Square(side: 5)` już nie istnieje.

---

Niektóre wartości należą do samego typu, a nie do pojedynczej instancji: kod waluty, wspólna wartość domyślna, fabryka tworząca typowy przypadek. Oznacz je jako `static` i odczytuj przez nazwę typu:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Tutaj `currency` jest zadeklarowane słowem `let`, ponieważ nigdy się nie zmienia, więc jest to stała współdzielona przez cały program. `Money.currency` działa bez tworzenia choćby jednego `Money`, podczas gdy `amount` potrzebuje instancji.

---

Dwie struktury nie mogą być porównywane za pomocą `==`, dopóki typ nie zadeklaruje, że to obsługuje. Robisz to, przyjmując **protokół** `Equatable`, zapisany po dwukropku w deklaracji:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
Nie musisz sam pisać `==`: gdy każda właściwość przechowywana jest już `Equatable`, Swift syntetyzuje go za ciebie, porównując właściwości po kolei. Dwie instancje są równe, gdy wszystkie ich właściwości są równe, i dokładnie tego oczekujesz od wartości.

---

Struktura to typ jak każdy inny, więc można ją przechowywać w tablicy, słowniku lub zbiorze, a każde narzędzie, które już znasz, nadal na niej działa:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Pamiętaj, że tablica przechowuje *kopie*: odczytanie `items[0]` do zmiennej i zmiana jej nie dotyka tablicy.
