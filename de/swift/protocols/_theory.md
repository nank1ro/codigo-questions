Ein **Protokoll** beschreibt, was ein Typ haben muss, ohne zu sagen, wie. Es ist eine Liste von Anforderungen — Eigenschaften und Methoden —, die jeder Typ, der es annimmt, umzusetzen verspricht.

Du deklarierst ein Protokoll mit dem Schlüsselwort `protocol`. Eine Eigenschaftsanforderung wird mit ihrem Typ geschrieben, gefolgt von einem Block, der sagt, wie auf sie zugegriffen werden kann: `{ get }` bedeutet, dass der Typ dich sie zumindest lesen lässt.
```swift
protocol Named {
    var name: String { get }
}
```
Ein Typ **implementiert** das Protokoll konform, indem er seinen Namen nach einem Doppelpunkt schreibt und alles bereitstellt, was das Protokoll verlangt:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
Ein Protokoll enthält selbst keine Daten: Es ist ein Vertrag. Jeder Typ, der ihn erfüllt, kann vom Rest deines Codes auf dieselbe Weise behandelt werden.

---

Ein Protokoll kann auch **Methoden** verlangen. Du schreibst die Signatur — Name, Parameter und Rückgabetyp — und machst dort Schluss, ganz ohne Rumpf:
```swift
protocol Greeter {
    func greet() -> String
}
```
Ein konformer Typ muss eine Methode mit genau dieser Signatur deklarieren und liefert den Rumpf:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
Weicht irgendetwas ab — der Name, ein Parametertyp, der Rückgabetyp —, implementiert der Typ das Protokoll nicht konform, und der Compiler sagt dir, welche Anforderung fehlt.

---

Eine Eigenschaftsanforderung sagt immer, wie die Eigenschaft verwendet werden kann. `{ get }` verlangt nur, dass der Wert gelesen werden kann; `{ get set }` verlangt, dass er gelesen **und** zugewiesen werden kann:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
Ein konformer Typ darf immer mehr bieten, als der Vertrag verlangt: Eine gespeicherte `var`-Eigenschaft erfüllt `{ get }` voll und ganz. Weniger darf er nie bieten — eine `let`-Konstante oder eine schreibgeschützte berechnete Eigenschaft kann `{ get set }` nicht erfüllen.

---

Protokolle beschränken sich nicht auf Structs. Eine **Klasse** implementiert auf genau dieselbe Weise konform, indem sie das Protokoll nach einem Doppelpunkt auflistet:
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
Erbt die Klasse außerdem von einer anderen Klasse, steht die Oberklasse zuerst in der Liste und die Protokolle folgen darauf. Ein Typ kann mehrere Protokolle gleichzeitig annehmen, getrennt durch Kommas.

---

Auch ein **Enum** kann konform implementieren. Es hat keine gespeicherten Eigenschaften, daher erfüllt man eine Eigenschaftsanforderung üblicherweise mit einer berechneten Eigenschaft, die über die Fälle schaltet:
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
Structs, Klassen und Enums: Alle drei nehmen Protokolle auf dieselbe Weise an, und Code, der gegen das Protokoll geschrieben ist, funktioniert mit allen dreien.

---

Ein Protokoll sammelt meist mehr als eine Anforderung, und ein konformer Typ muss jede einzelne davon erfüllen:
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
Die Reihenfolge der Anforderungen innerhalb der geschweiften Klammern spielt keine Rolle, und ebenso wenig die Reihenfolge, in der der konforme Typ sie bereitstellt: Der Compiler prüft nur, dass nichts fehlt.

---

Ein Struct ist ein Werttyp, daher muss eine Methode, die eine seiner gespeicherten Eigenschaften ändert, mit `mutating` markiert sein. Ist diese Methode eine Protokollanforderung, muss das auch das Protokoll sagen:
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
Ohne `mutating` im Protokoll könnte ein Struct die Anforderung nie erfüllen. Klassen sind Referenztypen und brauchen das Schlüsselwort nie: Eine Klasse erfüllt eine `mutating`-Anforderung mit einer gewöhnlichen Methode. Der Aufruf einer mutating-Methode braucht ein `var` — bei einem `let` ist es ein Kompilierfehler.

---

Die Konformität muss nicht direkt beim Typ deklariert werden. Eine **Extension** kann sie später hinzufügen, sodass die Deklaration des Typs selbst auf seine Daten fokussiert bleibt:
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
Das funktioniert auch bei Typen, die du nicht geschrieben hast: Du kannst einen Standardbibliothekstyp eines deiner Protokolle konform implementieren lassen, ohne seinen Quellcode anzufassen.

---

Eine Extension eines **Protokolls** ist ein anderes Werkzeug: Sie fügt Member zu jedem konformen Typ hinzu, bestehenden und zukünftigen. So gibst du einer Anforderung eine **Standardimplementierung**:
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
`Person` schreibt `greet()` nie und implementiert trotzdem konform. Innerhalb der Protokoll-Extension kannst du jede Anforderung des Protokolls verwenden — hier `name` —, denn jeder konforme Typ hat sie garantiert.

---

Eine Protokoll-Extension kann auch Member hinzufügen, die das Protokoll nie als Anforderungen gelistet hat. Sie sind zusätzliche Annehmlichkeiten, die jeder konforme Typ erhält:
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
`isEmpty` ist keine Anforderung, also muss ein konformer Typ sie nicht bereitstellen — er bekommt sie einfach.

---

Ein Protokoll kann auf einem anderen aufbauen. Schreibt man einen Protokollnamen nach den Doppelpunkt, **erbt** das neue Protokoll jede Anforderung des alten:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
Ein Typ, der `Aged` konform implementiert, muss `age` *und* `name` bereitstellen, und er gilt überall als `Named`-Typ. Ein Protokoll kann gleichzeitig von mehreren Protokollen erben, getrennt durch Kommas.

---

Eine Standardimplementierung ist ein Fallback, keine Regel. Stellt ein konformer Typ seine eigene Version einer Anforderung bereit, läuft seine Version:
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

print(Ticket().price) // 12, nicht 0
```
Die Standardimplementierung füllt nur die Lücken, die der Typ offenlässt.

---

Die Standardbibliothek ist aus Protokollen aufgebaut, und deine eigenen Typen können sie annehmen.

`Equatable` gibt einem Typ den `==`-Operator. Bei einem Struct, dessen gespeicherte Eigenschaften alle `Equatable` sind, genügt es, die Konformität zu deklarieren — Swift schreibt `==` für dich:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable` erbt von `Equatable` und fügt eine Ordnung hinzu. Du implementierst einen einzigen Operator, `<`, geschrieben als `static func`, die die beiden Werte nimmt, und bekommst `>`, `<=`, `>=` sowie `sorted()`, `min()` und `max()` auf Sammlungen gratis dazu:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible` entscheidet, was `print` für deinen Typ anzeigt. Seine einzige Anforderung ist eine `description`-Eigenschaft:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
Ohne die Konformität fällt das Ausgeben eines Structs auf eine Standardausgabe wie `Coin(value: 25)` zurück, und eine `description`-Eigenschaft allein ändert nichts — `print` sucht nach dem Protokoll. Auch die String-Interpolation verwendet `description`.

---

Ein Protokollname allein ist kein Typ, sondern eine Einschränkung, daher verlangt Swift von dir zu sagen, welches von zwei Dingen du meinst.

`some Shape` bedeutet *einen bestimmten konformen Typ*, festgelegt zur Kompilierzeit. Der Aufrufer erfährt nie, welcher es ist, aber es ist immer derselbe:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape` bedeutet *eine Box, die jeden konformen Typ aufnehmen kann*, und zwei Werte dieses Typs dürfen verschiedene Typen enthalten. Du brauchst ihn, wann immer der konkrete Typ variieren kann, etwa in einem gemischten Array:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
Beide lassen dich die Anforderungen des Protokolls aufrufen. Bevorzuge `some`, wenn ein einziger Typ genügt, weil er zur Laufzeit nichts kostet; greife zu `any`, wenn du wirklich Typen mischen musst.
