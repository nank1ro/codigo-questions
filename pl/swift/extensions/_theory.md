**Rozszerzenie** dodaje nową funkcjonalność do istniejącego typu: typu z biblioteki standardowej, takiego jak `Int` czy `String`, albo struktury lub klasy napisanej samodzielnie.
Piszesz słowo kluczowe `extension`, następnie nazwę typu, a nowe składowe umieszczasz między klamrami:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Wewnątrz rozszerzenia `self` to wartość, na której wywoływana jest metoda: w `4.squared()` jest nią `4`. Gdy rozszerzenie już istnieje, każdy `Int` w programie ma nową metodę, dokładnie tak, jakby była ona częścią `Int` od początku.

---

Rozszerzenia działają na dowolnym typie, nawet na takich, do których nie masz kodu źródłowego. `String` pochodzi z biblioteki standardowej, ale nadal możesz nadać mu nowe metody:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Wewnątrz rozszerzenia możesz pominąć `self.` przy wywoływaniu innych składowych typu: samo `lowercased()` oznacza `self.lowercased()`.

---

Rozszerzenie nie tworzy nowego typu i nie kopiuje starego: dodaje składowe do samego typu, dzięki czemu otrzymuje je każda istniejąca i przyszła wartość tego typu.
Dlatego rozszerzenia są tak przydatne przy typach, których nie możesz edytować, jak te z biblioteki standardowej czy z frameworka: nie możesz otworzyć pliku, w którym zdefiniowano `Int`, ale możesz go rozszerzyć z dowolnego pliku swojego programu.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

Oprócz metod rozszerzenie może dodawać **właściwości obliczeniowe**: właściwości, które nie przechowują wartości, lecz obliczają ją za każdym razem, gdy są odczytywane.
Właściwość obliczeniową deklaruje się za pomocą `var`, adnotacji typu oraz ciała między klamrami, które zwraca wartość:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Odczytuje się ją jak każdą właściwość, bez nawiasów: `7.isNegative`, a nie `7.isNegative()`.

---

Właściwości obliczeniowe w rozszerzeniach naturalnie pasują także do `String`. Metoda `reversed()` zwraca znaki w odwrotnej kolejności, a `String(...)` zamienia je z powrotem w ciąg znaków:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Tak jak w przypadku metod, `reversed()` wewnątrz rozszerzenia oznacza `self.reversed()`.

---

Rozszerzenia mogą dodawać właściwości obliczeniowe, ale **nie właściwości przechowywane**: poniższy kod się nie skompiluje:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Właściwość przechowywana wymaga miejsca wewnątrz każdej instancji typu. Wartości `Int` istnieją już w całym twoim programie, a nawet w kodzie skompilowanym na długo przed twoim rozszerzeniem, więc ich układ pamięci nie może się zmienić. Właściwość obliczeniowa nie potrzebuje miejsca, bo to po prostu kod wykonywany w momencie odczytu właściwości.

---

`Int`, `String`, tablice i struktury to **typy wartościowe**: metoda nie może zmienić wartości, na której jest wywołana, chyba że jest oznaczona jako `mutating`. Rozszerzenia też mogą dodawać metody mutating:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
Wewnątrz metody mutating możesz przypisywać wartość do `self`. Wartość musi być przechowywana w `var`: wywołanie `increment()` na stałej `let` to błąd kompilacji.

---

Metoda mutating może przyjmować parametry jak każda inna metoda i może całkowicie zastąpić `self`, zamiast aktualizować go w miejscu:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

Rozszerzenie może dodawać do typu nowe **inicjalizatory**. W przypadku struktury jest to najlepsze miejsce na ich umieszczenie: `init` zapisany wewnątrz ciała struktury zastępuje automatyczny inicjalizator memberwise, natomiast ten dodany w rozszerzeniu go zachowuje.
Nowy inicjalizator zwykle deleguje do istniejącego za pomocą `self.init(...)`:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

Rozszerzenia nie służą tylko do typów innych osób. Częstym sposobem organizowania własnego kodu jest trzymanie właściwości przechowywanych w ciele struktury lub klasy i dodawanie zachowań w jednym lub kilku rozszerzeniach, z których każde grupuje powiązane składowe:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
Składowe dodane w rozszerzeniu mogą korzystać z właściwości przechowywanych bezpośrednio, dokładnie tak, jakby były zapisane wewnątrz typu.

---

Rozszerzenie może też sprawić, że typ będzie zgodny z **protokołem**, czyli listą wymagań, które typ obiecuje zaimplementować. Piszesz nazwę protokołu po nazwie typu, oddzieloną dwukropkiem, i dodajesz wymagane składowe w ciele.
`CustomStringConvertible` to standardowy protokół z jednym wymaganiem, właściwością obliczeniową `description` typu `String`, z której `print` korzysta, aby wyświetlić wartość:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
Przechowywanie każdej zgodności z protokołem w osobnym rozszerzeniu to zwykły sposób organizowania typu w Swift.

---

`Array` jest typem generycznym: `[Int]` i `[String]` to tablice z różnym typem **`Element`**. Rozszerzenie `Array` dotyczy ich wszystkich, co stanowi problem, gdy nowa składowa ma sens tylko dla niektórych elementów: nie można dodać do siebie liczb, które są ciągami znaków.
Klauzula `where` ogranicza rozszerzenie do tablic, których `Element` jest danym typem:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest` działa, natomiast `["a", "b"].largest` to błąd kompilacji: właściwość nie istnieje dla `[String]`.

---

Rozszerzenia mogą dodawać składowe **static**: właściwości i metody należące do samego typu, a nie do pojedynczej wartości, oznaczone słowem kluczowym `static` i dostępne poprzez nazwę typu.
`static let` jest dozwolone, mimo że przechowuje wartość, ponieważ istnieje tylko jedna kopia dla całego typu, a nie jedna na instancję:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
Składowa statyczna nie ma wartości `self`, na której mogłaby pracować: `Int.answer` jest odczytywane na typie, a nie na liczbie.

---

Statyczne metody w rozszerzeniach to dobre miejsce dla małych funkcji fabrycznych budujących wartość typu. `String(repeating:count:)` to standardowy inicjalizator powtarzający fragment tekstu określoną liczbę razy:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Rozszerzenia mogą tylko **dodawać** składowe, nigdy zastępować ani nadpisywać istniejących. `override` należy do podklas, które są innym typem niż ich nadklasa; rozszerzenie to ten sam typ, więc zadeklarowanie metody, która już istnieje, to błąd ponownej deklaracji:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
Jeśli potrzebujesz innego zachowania, dodaj metodę o nowej nazwie albo napisz podklasę, gdy typ jest klasą.
