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
print(r.area) // 12, no parentheses
```
Właściwości obliczeniowe nie są częścią inicjalizatora memberwise, ponieważ nie ma nic do przechowania. Używaj ich, gdy wartość jest wyliczana z innych, a metodę, gdy praca wymaga parametrów.
