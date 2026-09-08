Każda wartość w Swift ma **typ**, który mówi kompilatorowi, jakiego rodzaju są to dane i co można z nimi robić.
Podstawowe typy to:
- `Int`: liczba całkowita, jak `42` czy `-7`
- `Double`: liczba z częścią dziesiętną, jak `3.14`
- `String`: fragment tekstu, jak `"Hello"`
- `Character`: pojedynczy znak, jak `"a"`
- `Bool`: `true` albo `false`

Typ stałej lub zmiennej można zadeklarować za pomocą **adnotacji typu**: dwukropka i nazwy typu po nazwie:
```swift
let age: Int = 36
let name: String = "Ada"
```
Wartości jednego typu nie można przechować w stałej innego typu: `let age: Int = "36"` to błąd kompilacji.

---

Przez większość czasu nie piszesz adnotacji typu: Swift **wnioskuje** typ na podstawie przypisywanej wartości, zgodnie z kilkoma regułami dotyczącymi literalów:
- liczba bez kropki dziesiętnej, jak `42`, to `Int`
- liczba z kropką dziesiętną, jak `3.14`, to `Double`
- tekst w cudzysłowach to `String`
- `true` i `false` to `Bool`
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift ma też `Float`, liczbę dziesiętną, która używa połowy pamięci `Double`, ale jest mniej precyzyjna, dlatego literal dziesiętny nigdy nie zostanie wnioskowany jako `Float`: trzeba o niego poprosić adnotacją.
Analogicznie `"a"` jest wnioskowane jako `String`, więc `Character` zawsze wymaga adnotacji.

---

Funkcja `type(of:)` zwraca typ wartości, co przydaje się do sprawdzenia, co Swift wnioskował:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
Gdy chcesz typ inny niż wnioskowany, dodaj adnotację. Literal liczby całkowitej może być przechowany w stałej `Double` lub `Float`, a literal jednego znaku w stałej `Character`:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift nigdy nie konwertuje typów liczbowych sam z siebie: dodanie `Int` do `Double` to błąd kompilacji, mimo że oba są liczbami.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
Aby je połączyć, tworzysz nową wartość potrzebnego typu, przekazując wartość do inicjalizatora tego typu:
```swift
let total = Double(apples) * price // 4.5
```
To samo działa w drugą stronę: `Int(4.5)` daje `Int`, zachowując tylko część całkowitą liczby.

---

`Int(x)` nie zaokrągla: **obcina**, po prostu odrzucając część dziesiętną, więc `Int(3.99)` to `3`, a `Int(-3.99)` to `-3`.
Aby zaokrąglić do najbliższej liczby całkowitej, najpierw wywołaj `rounded()` na `Double`, a potem skonwertuj:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
Wartości połówkowe, jak `2.5`, są zaokrąglane w stronę oddalania się od zera: `2.5` staje się `3.0`, a `-2.5` staje się `-3.0`.

---

Typ operandów decyduje o tym, jak działa dzielenie. Gdy oba są `Int`, operator `/` wykonuje **dzielenie całkowite**: wynikiem jest `Int`, a reszta jest odrzucana.
Gdy co najmniej jeden operand jest `Double`, `/` wykonuje dzielenie zmiennoprzecinkowe i zachowuje część dziesiętną:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
Aby więc uzyskać wynik dziesiętny z dwóch wartości `Int`, musisz skonwertować co najmniej jedną z nich do `Double` **przed** dzieleniem: `Double(7 / 2)` to `3.0`, ponieważ dzielenie całkowite zdążyło już zajść.

---

Gdy funkcja musi zwrócić wynik dziesiętny obliczony z liczb całkowitych, skonwertuj operandy do `Double` przed dzieleniem i zadeklaruj typ zwracany jako `Double`:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
Pamiętaj, że `count` tablicy też jest `Int`, więc wymaga tej samej konwersji.

---

Liczby i ciągi znaków konwertuje się tą samą składnią inicjalizatora. `String(42)` zamienia liczbę na tekst `"42"`, dokładnie tak, jak jej interpolacja za pomocą `"\(42)"`.
Odwrotny kierunek może się nie powieść, ponieważ nie każdy tekst jest liczbą, więc `Int("42")` zwraca **opcjonalny** `Int?`: tutaj zawiera `42`, ale `Int("hello")` to `nil`.
Jak wiesz z lekcji o opcjonałach, możesz zapewnić wartość zastępczą za pomocą `??` albo rozpakować go przez `if let`:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)` udaje się tylko wtedy, gdy cały tekst jest poprawną liczbą całkowitą, z opcjonalnym znakiem:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
Dla tekstu dziesiętnego użyj `Double(text)`, który w ten sam sposób zwraca `Double?`: `Double("3.5")` to `Optional(3.5)`.

---

**Alias typu** nadaje istniejącemu typowi nową nazwę, za pomocą słowa kluczowego `typealias`:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score` i `Int` to ten sam typ, więc można je swobodnie mieszać. Alias nie dodaje żadnego bezpieczeństwa: sprawia jedynie, że kod czyta się lepiej, gdy zwykły typ ma konkretne znaczenie w twoim programie.

---

`Int` używa 64 bitów, więc może reprezentować tylko liczby z ustalonego zakresu. Największa i najmniejsza wartość są dostępne jako `Int.max` i `Int.min`:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
Przekroczenie tych granic nazywa się **przepełnieniem** (overflow). W przeciwieństwie do wielu innych języków Swift nie zawija po cichu wyniku do drugiego końca zakresu: operacja z przepełnieniem to **błąd wykonania**, który zatrzymuje program.

---

`Int.max` i `Int.min` przydają się jako wartości początkowe przy szukaniu ekstremum: każda rzeczywista liczba jest mniejsza niż `Int.max`, więc to bezpieczna wartość początkowa dla „najmniejszej dotąd znalezionej":
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

Jak widać w lekcjach o ciągach znaków, iterowanie po `String` daje po jednym `Character` na raz. `Character` nie jest `String`, więc aby użyć go jako tekstu, konwertujesz go za pomocą `String(c)`.
Gdy znak jest cyfrą, właściwość `wholeNumberValue` daje jego wartość liczbową jako `Int?`: jest `nil` dla znaków, które nie są cyframi.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

Ponieważ `Int(text)` i `Double(text)` zwracają `nil` w razie niepowodzenia, porównanie wyniku z `nil` mówi ci, czy tekst jest liczbą danego rodzaju:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
Zwróć uwagę na ostatnią linię: każdy tekst zaakceptowany przez `Int` jest też akceptowany przez `Double`, więc sprawdź najpierw `Int`, gdy chcesz je odróżnić.

---

Czasem potrzebujesz przechowywać wartości różnych typów razem. Specjalny typ `Any` może przechowywać wartość **dowolnego** typu, więc tablica zadeklarowana jako `[Any]` może mieszać liczby, ciągi znaków i wartości logiczne:
```swift
let items: [Any] = [1, "two", true]
```
Każdy element nadal pamięta swój rzeczywisty typ, który ujawnia `type(of:)`. Aby pracować z wartością jako jej rzeczywistym typem, używasz **rzutowania warunkowego** z `as?`, które zwraca opcjonał: zawiera wartość, gdy typ się zgadza, a `nil` w przeciwnym razie:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any` to ostateczność: tablica jednego konkretnego typu jest bezpieczniejsza i łatwiejsza w użyciu, więc preferuj ją, gdy tylko możesz.

---

Rzutowania warunkowe łączą się naturalnie z `else if`, aby obsłużyć kilka możliwych typów, konwertując każdy z nich na typ potrzebny do wyniku:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
`Int` przechowany w `Any` nadal jest `Int`: `as? Double` na nim zwraca `nil`, ponieważ `as?` sprawdza typ, a nie konwertuje liczb.
