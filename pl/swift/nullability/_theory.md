Czasami wartość po prostu nie istnieje: użytkownik bez drugiego imienia, wyszukiwanie, które niczego nie znajduje, tekst, którego nie da się zamienić na liczbę.
Swift reprezentuje brakującą wartość za pomocą `nil`, ale zwykła zmienna nigdy nie może jej przechowywać:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
Aby dopuścić brakującą wartość, deklarujesz typ **opcjonalny**, dodając znak zapytania `?` po typie.
`Int?` przechowuje albo `Int`, albo `nil`:
```swift
var age: Int? = 30
age = nil // dozwolone
```
Zmienna opcjonalna zadeklarowana bez wartości zaczyna jako `nil`.

---

Możesz porównać opcjonał z `nil` za pomocą `==` i `!=`, a także porównać go bezpośrednio ze zwykłą wartością opakowanego typu:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
Pamiętaj, że `Int?` i `Int` to dwa różne typy: `Int?` może być pusty, `Int` nigdy nie jest.

---

Opcjonał jest jak pudełko: zanim użyjesz wartości znajdującej się w środku, musisz je otworzyć, co Swift nazywa **rozpakowaniem**.
Najszybszym sposobem jest **wymuszone rozpakowanie** za pomocą wykrzyknika `!`:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
`!` mówi Swiftowi "jestem pewien, że tu jest wartość". Jeśli się mylisz, a opcjonał jest `nil`, program natychmiast się zatrzymuje z awarią w czasie wykonywania:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
Dlatego wymuszone rozpakowanie jest uznawane za niebezpieczne: używaj go tylko wtedy, gdy masz pewność, że wartość istnieje.

---

Wymuszone rozpakowanie jest bezpieczne tylko wtedy, gdy wcześniej sprawdziłeś, że opcjonał nie jest `nil`:
```swift
if score != nil {
    print(score! * 2)
}
```

---

Sprawdzanie `nil`, a potem wymuszone rozpakowanie jest rozwlekłe. Swift oferuje **wiązanie opcjonalne** za pomocą `if let`, które rozpakowuje opcjonał i zapisuje wartość w nowej stałej w jednym kroku:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value jest typu Int, a nie Int?
} else {
    print("No score")
}
```
Ciało `if` wykonuje się tylko wtedy, gdy opcjonał zawiera wartość; wewnątrz niego `value` jest zwykłym `Int` i nie wymaga `!`.

---

Gdy brakująca wartość oznacza "zatrzymaj się tutaj", `guard let` jest bardziej czytelny niż `if let`.
Rozpakowuje opcjonał, a jeśli to się nie powiedzie, wykonuje blok `else`, który musi opuścić bieżący zakres (za pomocą `return`, `break`, `continue` lub `throw`):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // od tego miejsca name jest typu String
}
```
W przeciwieństwie do `if let`, rozpakowana stała pozostaje dostępna do końca funkcji, więc główna ścieżka nie jest zagnieżdżona wewnątrz `if`.

---

Typowym zastosowaniem `guard let` jest walidacja danych wejściowych funkcji na samym początku i zwrócenie wartości domyślnej, gdy jej brakuje:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

Bardzo często wszystko, czego potrzebujesz od opcjonału, to jego wartość albo wartość domyślna.
**Operator łączenia z nil** `??` robi dokładnie to: rozpakowuje opcjonał, jeśli ma wartość, a w przeciwnym razie zwraca wartość po jego prawej stronie:
```swift
let score: Int? = nil
let points = score ?? 0 // points jest typu Int i wynosi 0
```
Wartość domyślna musi mieć ten sam typ co opakowana wartość.
Możesz łączyć kilka `??` w łańcuch: wygrywa pierwsza wartość różna od `nil`.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??` to najkrótszy sposób na zamianę opcjonału na zwykłą wartość, gdy istnieje sensowna wartość domyślna:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

Przy łączeniu `??` Swift ocenia od lewej do prawej i zatrzymuje się na pierwszej wartości różnej od `nil`; ostatnia wartość domyślna jest używana tylko wtedy, gdy każdy wcześniejszy opcjonał jest `nil`.

---

Dostęp do właściwości lub wywołanie metody na opcjonale wymagałoby najpierw jego rozpakowania.
**Łańcuchowanie opcjonalne** za pomocą `?.` robi to za ciebie: jeśli opcjonał jest `nil`, całe wyrażenie staje się `nil`, w przeciwnym razie dostęp przechodzi dalej:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // String? zawierający "SWIFT"
```
Wynik jest zawsze opcjonalny, nawet gdy sama właściwość nie jest.
Łańcuchy mogą być tak długie, jak potrzebujesz, i dobrze łączą się z `??`:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

Łańcuchowanie opcjonalne błyszczy, gdy dane mogą brakować na kilku poziomach: obiekt może być `nil`, a jedna z jego właściwości też może być `nil`.
Pojedynczy łańcuch `?.` obsługuje oba przypadki bez żadnego `if`.

---

Pojedyncze `if let` lub `guard let` może rozpakować kilka opcjonałów naraz: wystarczy oddzielić wiązania przecinkami.
Ciało wykonuje się tylko wtedy, gdy każdy opcjonał ma wartość:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
Możesz też dodać warunek logiczny po wiązaniach, na przykład `if let n = number, n > 0`.

---

Wiązanie kilku opcjonałów w jednym `if let` sprawia, że kod pozostaje płaski: jeden blok `else` obejmuje wszystkie brakujące wartości.

---

Wiele operacji może się nie powieść, a Swift zgłasza niepowodzenie, zwracając opcjonał.
Konwersja tekstu na liczbę to klasyczny przykład: `Int("42")` zwraca `Int?` z wartością `42`, natomiast `Int("abc")` zwraca `nil`.
`Int("3.5")` też jest `nil`, ponieważ tekst nie jest liczbą całkowitą; użyj `Double("3.5")` dla liczb dziesiętnych.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
Innymi przykładami są `array.first` (`nil` dla pustej tablicy) i `dictionary[key]` (`nil`, gdy brakuje klucza).

---

Ponieważ konwersja może się nie powieść, jej wynik jest zawsze opcjonalny i musi zostać rozpakowany przed użyciem, nawet gdy jesteś pewien, że tekst jest poprawną liczbą.

---

Konwersje, które mogą się nie powieść, naturalnie łączą się z `guard let`: przekonwertuj, wyjdź, gdy wynik jest `nil`, a następnie pracuj ze zwykłą wartością.

---

Czasami chcesz przekształcić wartość znajdującą się wewnątrz opcjonału i zachować wynik jako opcjonalny, bez ręcznego rozpakowywania i ponownego pakowania.
Opcjonały mają metodę `map`: stosuje domknięcie do wartości, jeśli taka istnieje, a w przeciwnym razie zwraca `nil`.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // Int? zawierający 20
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
Połączona z konwersją, która może się nie powieść, tworzy zwięzły potok: `Int(text).map { $0 + 1 }`.
