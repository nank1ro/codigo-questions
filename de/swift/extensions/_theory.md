Eine **Extension** fügt einem bestehenden Typ neue Funktionalität hinzu: einem Standardbibliothekstyp wie `Int` oder `String`, oder einem Struct oder einer Klasse, die du selbst geschrieben hast.
Du schreibst das Schlüsselwort `extension`, gefolgt vom Namen des Typs, und setzt die neuen Member zwischen geschweifte Klammern:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
Innerhalb der Extension ist `self` der Wert, auf dem die Methode aufgerufen wird: in `4.squared()` ist es `4`. Sobald die Extension existiert, hat jeder `Int` im Programm die neue Methode, genau so, als wäre sie von Anfang an Teil von `Int` gewesen.

---

Extensions funktionieren mit jedem Typ, sogar mit denen, deren Quellcode du nicht hast. `String` kommt aus der Standardbibliothek, aber du kannst ihm trotzdem neue Methoden geben:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
Innerhalb einer Extension kannst du `self.` beim Aufruf anderer Member des Typs weglassen: `lowercased()` allein bedeutet `self.lowercased()`.

---

Eine Extension erstellt keinen neuen Typ und kopiert den alten nicht: Sie fügt dem Typ selbst Member hinzu, sodass jeder bestehende und zukünftige Wert dieses Typs sie erhält.
Deshalb sind Extensions so nützlich bei Typen, die du nicht bearbeiten kannst, wie denen aus der Standardbibliothek oder aus einem Framework: Du kannst die Datei, in der `Int` definiert ist, nicht öffnen, aber du kannst ihn aus jeder Datei deines Programms erweitern.
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

Neben Methoden kann eine Extension **berechnete Eigenschaften** hinzufügen: Eigenschaften, die keinen Wert speichern, sondern ihn jedes Mal berechnen, wenn sie gelesen werden.
Eine berechnete Eigenschaft wird mit `var`, einer Typannotation und einem Rumpf zwischen geschweiften Klammern deklariert, der den Wert zurückgibt:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
Sie wird wie jede Eigenschaft gelesen, ohne Klammern: `7.isNegative`, nicht `7.isNegative()`.

---

Berechnete Eigenschaften in Extensions passen auch natürlich zu `String`. Die Methode `reversed()` gibt die Zeichen in umgekehrter Reihenfolge zurück, und `String(...)` macht daraus wieder einen String:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
Wie bei Methoden bedeutet `reversed()` innerhalb der Extension `self.reversed()`.

---

Extensions können berechnete Eigenschaften hinzufügen, aber **keine gespeicherten Eigenschaften**: Dies kompiliert nicht:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
Eine gespeicherte Eigenschaft braucht Platz in jeder Instanz des Typs. `Int`-Werte existieren bereits überall in deinem Programm, und zwar sogar in Code, der lange vor deiner Extension kompiliert wurde, sodass sich ihr Speicherlayout nicht ändern kann. Eine berechnete Eigenschaft braucht keinen Platz, weil sie einfach Code ist, der ausgeführt wird, wenn die Eigenschaft gelesen wird.

---

`Int`, `String`, Arrays und Structs sind **Werttypen**: Eine Methode kann den Wert, auf dem sie aufgerufen wird, nicht ändern, es sei denn, sie ist als `mutating` markiert. Extensions können auch `mutating`-Methoden hinzufügen:
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
Innerhalb einer `mutating`-Methode kannst du `self` etwas zuweisen. Der Wert muss in einer `var` gespeichert sein: `increment()` auf einer `let`-Konstante aufzurufen ist ein Kompilierfehler.

---

Eine `mutating`-Methode kann Parameter wie jede andere Methode entgegennehmen und kann `self` vollständig ersetzen, statt es an Ort und Stelle zu aktualisieren:
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

Eine Extension kann einem Typ neue **Initialisierer** hinzufügen. Bei einem Struct ist das der beste Ort dafür: Ein innerhalb des Struct-Rumpfs geschriebenes `init` ersetzt den automatischen Memberwise-Initialisierer, während ein in einer Extension hinzugefügter ihn beibehält.
Der neue Initialisierer delegiert üblicherweise mit `self.init(...)` an einen bestehenden:
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

Extensions sind nicht nur für die Typen anderer. Eine übliche Art, deinen eigenen Code zu organisieren, ist, die gespeicherten Eigenschaften im Struct- oder Klassenrumpf zu behalten und das Verhalten in einer oder mehreren Extensions hinzuzufügen, die jeweils verwandte Member gruppieren:
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
Member, die in einer Extension hinzugefügt wurden, können die gespeicherten Eigenschaften direkt verwenden, genau so, als wären sie innerhalb des Typs geschrieben.

---

Eine Extension kann einen Typ auch ein **Protokoll** konform implementieren lassen, eine Liste von Anforderungen, die der Typ umzusetzen verspricht. Schreibe den Namen des Protokolls hinter den Typnamen, getrennt durch einen Doppelpunkt, und füge die geforderten Member im Rumpf hinzu.
`CustomStringConvertible` ist ein Standardprotokoll mit einer einzigen Anforderung, einer berechneten Eigenschaft `description` vom Typ `String`, das `print` verwendet, um den Wert anzuzeigen:
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
Jede Protokoll-Konformität in ihrer eigenen Extension zu halten, ist die übliche Art, einen Swift-Typ zu organisieren.

---

`Array` ist ein generischer Typ: `[Int]` und `[String]` sind beide Arrays, mit einem unterschiedlichen **`Element`**-Typ. Eine Extension von `Array` gilt für alle davon, was ein Problem ist, wenn das neue Member nur für einige Elemente Sinn ergibt: Du kannst keine Zahlen hinzufügen, die Strings sind.
Eine `where`-Klausel beschränkt die Extension auf die Arrays, deren `Element` ein gegebener Typ ist:
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
`[3, 9, 2].largest` funktioniert, während `["a", "b"].largest` ein Kompilierfehler ist: Die Eigenschaft existiert nicht auf `[String]`.

---

Extensions können **statische** Member hinzufügen: Eigenschaften und Methoden, die zum Typ selbst gehören statt zu einem einzelnen Wert, markiert mit dem Schlüsselwort `static` und aufgerufen über den Typnamen.
Ein `static let` ist erlaubt, obwohl es einen Wert speichert, weil es nur eine Kopie für den ganzen Typ gibt, nicht eine pro Instanz:
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
Ein statisches Member hat keinen `self`-Wert, auf dem es arbeitet: `Int.answer` wird auf dem Typ gelesen, nicht auf einer Zahl.

---

Statische Methoden in Extensions sind ein guter Ort für kleine Factory-Funktionen, die einen Wert des Typs erstellen. `String(repeating:count:)` ist der Standardinitialisierer, der ein Stück Text eine bestimmte Anzahl von Malen wiederholt:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

Extensions können Member nur **hinzufügen**, niemals bestehende ersetzen oder überschreiben. `override` gehört zu Subklassen, die einen anderen Typ als ihre Elternklasse sind; eine Extension ist derselbe Typ, daher ist das Deklarieren einer Methode, die bereits existiert, ein Redeklarationsfehler:
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
Wenn du ein anderes Verhalten brauchst, füge eine Methode mit einem neuen Namen hinzu oder schreibe eine Subklasse, wenn der Typ eine Klasse ist.
