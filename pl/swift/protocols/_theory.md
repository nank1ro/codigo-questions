**Protokół** opisuje, co dany typ musi mieć, nie mówiąc jak. Jest to lista wymagań — właściwości i metod — które każdy typ go przyjmujący obiecuje spełnić.

Deklarujesz go słowem kluczowym `protocol`. Wymaganie dotyczące właściwości zapisuje się z jej typem, po którym następuje blok określający, jak można się do niej dostać: `{ get }` oznacza, że typ musi ci przynajmniej pozwolić na jej odczyt.
```swift
protocol Named {
    var name: String { get }
}
```
Typ jest **zgodny** z protokołem, jeśli zapisuje jego nazwę po dwukropku i zapewnia wszystko, o co prosi protokół:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Protokół sam nie przechowuje żadnych danych: jest kontraktem. Każdy typ, który go spełnia, może być traktowany w ten sam sposób przez resztę twojego kodu.

---

Protokół może też wymagać **metod**. Piszesz sygnaturę — nazwę, parametry i typ zwracany — i na tym kończysz, bez ciała:
```swift
protocol Greeter {
    func greet() -> String
}
```
Zgodny typ musi zadeklarować metodę o dokładnie tej sygnaturze i to on dostarcza ciało:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Jeśli cokolwiek się różni — nazwa, typ parametru, typ zwracany — typ nie jest zgodny, a kompilator powie ci, którego wymagania brakuje.

---

Wymaganie dotyczące właściwości zawsze określa, jak właściwość może być używana. `{ get }` prosi tylko o to, aby wartość można było odczytać; `{ get set }` prosi o to, aby można ją było odczytać **i** przypisać:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Zgodny typ może zawsze dać więcej, niż prosi kontrakt: właściwość przechowywana `var` doskonale spełnia `{ get }`. Nigdy nie może dać mniej — stała `let` ani obliczeniowa właściwość tylko do odczytu nie mogą spełnić `{ get set }`.

---

Protokoły nie ograniczają się do struktur. **Klasa** jest zgodna dokładnie w ten sam sposób, wymieniając protokół po dwukropku:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
Jeśli klasa dziedziczy też po innej klasie, nadklasa stoi pierwsza na liście, a protokoły następują po niej. Typ może przyjąć kilka protokołów naraz, oddzielonych przecinkami.

---

**Wyliczenie** też może być zgodne. Nie ma właściwości przechowywanych, więc wymaganie dotyczące właściwości spełnia się zwykle właściwością obliczeniową, która przełącza się po przypadkach:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
Struktury, klasy i wyliczenia: wszystkie trzy przyjmują protokoły w ten sam sposób, a kod napisany w oparciu o protokół działa ze wszystkimi z nich.

---

Protokół zwykle zbiera więcej niż jedno wymaganie, a zgodny typ musi spełnić każde z nich:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
Kolejność wymagań wewnątrz klamer nie ma znaczenia, podobnie jak kolejność, w jakiej zgodny typ je zapewnia: kompilator sprawdza tylko, czy niczego nie brakuje.

---

Struktura to typ wartościowy, więc metoda zmieniająca którąś z jej właściwości przechowywanych musi być oznaczona jako `mutating`. Gdy ta metoda jest wymaganiem protokołu, protokół też musi to powiedzieć:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
Bez `mutating` w protokole struktura nigdy nie mogłaby spełnić wymagania. Klasy to typy referencyjne i nigdy nie potrzebują tego słowa kluczowego: klasa spełnia wymaganie `mutating` zwykłą metodą. Wywołanie metody mutating wymaga `var` — na `let` jest to błąd kompilacji.

---

Zgodności nie trzeba deklarować obok typu. **Rozszerzenie** może dodać ją później, dzięki czemu deklaracja samego typu pozostaje skupiona na swoich danych:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
To działa też dla typów, których nie napisałeś: możesz sprawić, aby typ z biblioteki standardowej był zgodny z jednym z twoich protokołów, nie dotykając jego kodu źródłowego.

---

Rozszerzenie **protokołu** to inne narzędzie: dodaje składowe do każdego zgodnego typu, obecnego i przyszłego. Tak nadajesz wymaganiu **domyślną implementację**:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person` nigdy nie pisze `greet()`, a mimo to jest zgodny. Wewnątrz rozszerzenia protokołu możesz użyć każdego wymagania protokołu — tutaj `name` — ponieważ każdy zgodny typ ma gwarancję, że je posiada.

---

Rozszerzenie protokołu może też dodawać składowe, których protokół nigdy nie wymienił jako wymagań. Są to dodatkowe udogodnienia, dostępne w każdym zgodnym typie:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty` nie jest wymaganiem, więc zgodny typ nie musi go zapewniać — po prostu je dostaje.

---

Protokół może budować na innym. Zapisanie nazwy protokołu po dwukropku sprawia, że nowy protokół **dziedziczy** każde wymaganie starego:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Typ zgodny z `Aged` musi zapewniać `age` *i* `name`, i wszędzie liczy się jako typ `Named`. Protokół może dziedziczyć po kilku protokołach naraz, oddzielonych przecinkami.

---

Domyślna implementacja to rozwiązanie zapasowe, nie reguła. Jeśli zgodny typ zapewnia własną wersję wymagania, to właśnie jej wersja jest wykonywana:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, nie 0
```
Domyślna wersja wypełnia tylko luki, które typ pozostawia otwarte.

---

Biblioteka standardowa jest zbudowana z protokołów, a twoje własne typy mogą je przyjmować.

`Equatable` daje typowi operator `==`. Dla struktury, której wszystkie właściwości przechowywane są `Equatable`, wystarczy zadeklarować zgodność — Swift pisze `==` za ciebie:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` dziedziczy po `Equatable` i dodaje porządkowanie. Implementujesz jeden operator, `<`, zapisany jako `static func` przyjmujący obie wartości, a dostajesz `>`, `<=`, `>=`, a do tego `sorted()`, `min()` i `max()` na kolekcjach za darmo:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` decyduje, co `print` pokazuje dla twojego typu. Jego jedyne wymaganie to właściwość `description`:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Bez zgodności wypisanie struktury wraca do domyślnego zrzutu, takiego jak `Coin(value: 25)`, a sama właściwość `description` nic nie zmienia — `print` szuka protokołu. Interpolacja ciągów znaków też korzysta z `description`.

---

Nazwa protokołu sama w sobie nie jest typem, jest ograniczeniem, więc Swift każe ci powiedzieć, którą z dwóch rzeczy masz na myśli.

`some Shape` oznacza *jeden konkretny zgodny typ*, ustalony w czasie kompilacji. Wywołujący nigdy nie dowiaduje się, który to, ale zawsze jest to ten sam:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` oznacza *pudełko, które może pomieścić dowolny zgodny typ*, a dwie wartości tego typu mogą przechowywać różne typy. Potrzebujesz go zawsze, gdy konkretny typ może się różnić, na przykład wewnątrz wymieszanej tablicy:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Oba pozwalają wywoływać wymagania protokołu. Wybieraj `some`, gdy wystarczy jeden typ, bo nic nie kosztuje w czasie działania; sięgaj po `any`, gdy naprawdę potrzebujesz mieszać typy.
