W Swift błąd jest **wartością**, a nie awarią programu. Jako błąd może wystąpić dowolny typ przyjmujący protokół `Error`, a wyliczenie to zwykły wybór, ponieważ jego przypadki nazywają dokładnie to, co może pójść nie tak:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
Funkcję, która może zawieść, oznacza się `throws`, a o niepowodzeniu informuje słowem `throw`:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
Wywołanie takiej funkcji wymaga `try`, a wywołanie musi się znajdować w bloku `do`, po którym następuje blok `catch` określający, co zrobić, gdy operacja się nie powiedzie:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
Gdy wykonuje się `throw`, reszta bloku `do` jest pomijana, a sterowanie przejmuje `catch`. Nic się nie zawiesza: program działa dalej po bloku `catch`.

---

Funkcja zgłaszająca błąd może nadal zwracać wartość. Słowo kluczowe `throws` znajduje się między listą parametrów a strzałką zwracanego typu:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
Czytając to na głos: *square przyjmuje `Int`, może zgłosić błąd i zwraca `Int`*.

W miejscu wywołania wartość istnieje tylko wtedy, gdy nie został zgłoszony żaden błąd, więc przypisanie znajduje się wewnątrz bloku `do`:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
`try` nie jest opcjonalną ozdobą: kompilator odrzuca wywołanie bez niego, więc czytający zawsze widzi, które linie mogą zawieść.

---

Goły `catch` obsługuje każdy błąd tak samo. Najczęściej chcesz zareagować na jedno konkretne niepowodzenie, więc `catch` może nieść **wzorzec**: przypadek, który jest gotów obsłużyć.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift sprawdza klauzule `catch` od góry do dołu i wykonuje pierwszą, której wzorzec pasuje.

Ostatni `catch` nie ma wzorca celowo. `catch` ze wzorcem obejmuje tylko wskazany przypadek, a Swift wymaga, aby każdy błąd był gdzieś obsłużony, więc blok `do` wypisujący wzorce potrzebuje końcowego `catch` bez wzorca, który wyłapie resztę.

---

Kolejność ma znaczenie. Swift porównuje zgłoszoną wartość z każdym wzorcem `catch` w kolejności, w jakiej są zapisane, i zatrzymuje się na pierwszym dopasowaniu, więc `catch` bez wzorca umieszczony na początku pochłonąłby wszystko poniżej. Trzymaj konkretne przypadki na górze, a łapiący wszystko na dole.

Błąd, który nie pasuje do żadnego wzorca, nie jest ignorowany: trafia do końcowego `catch` bez wzorca.

---

Przypadek błędu może nieść dane. Nadaj przypadkowi **wartości skojarzone**, a `throw` je wypełni, dzięki czemu obsługujący dowie się nie tylko *co* zawiodło, ale i *o ile*:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
Pasujący `catch` wiąże te wartości przez `let`:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
Nazwa po `let` zależy od Ciebie; to nowa stała dostępna tylko wewnątrz tego bloku `catch`. Dzięki temu błąd niesie użyteczny komunikat, a Ty nie musisz wstawiać liczb do ciągów znaków w miejscu, gdzie występuje niepowodzenie.

---

Jedno wyliczenie zwykle zawiera każdy sposób, w jaki pojedyncze zadanie może zawieść — jeden przypadek na każdą przyczynę:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
Pisanie jednego `catch` na przypadek staje się powtarzalne. Zamiast tego złap cały typ naraz i użyj `switch` na wartości:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError` oznacza *złap wszystko, co jest `FormError`, i nazwij to `error`*. Wewnątrz bloku `error` ma typ wyliczenia, więc `switch` widzi przypadki i sprawdza, czy pokryłeś je wszystkie. Końcowy `catch` bez wzorca jest nadal wymagany, ponieważ do tego bloku `do` mógłby dotrzeć błąd innego typu.

---

Walidator czyta się najlepiej, gdy odrzucenia przychodzą najpierw, a właściwa praca pozostaje niewcięta na dole. `guard` powstał właśnie do tego: określa warunek, który musi być spełniony, a jego blok `else` wykonuje się, gdy nie jest.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
Blok `else` w `guard` musi opuścić bieżący zasięg, a `throw` to jeden ze sposobów, aby to zrobić, obok `return`, `break` i `continue`. Kilka `guard`ów ułożonych na początku funkcji czyta się jak listę reguł, którym dane wejściowe muszą sprostać.

---

Czasem nie obchodzi Cię *dlaczego* coś zawiodło, tylko to, że zawiodło. `try?` zamienia zgłaszające błąd wywołanie w **opcjonał**: wartość, gdy się powiedzie, `nil`, gdy zgłosi błąd.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
Żadnego `do`, żadnego `catch`: niepowodzenie zostaje wplecione w opcjonał, który już umiesz rozpakować. Ceną jest to, że wartość błędu jest wyrzucana, więc sięgaj po `try?` tylko wtedy, gdy naprawdę nie ma nic do zakomunikowania.

---

Ponieważ `try?` daje w wyniku opcjonał, operator `??` dopełnia reszty, podając wartość zapasową:
```swift
let port = (try? readPort(text)) ?? 8080
```
Nawiasy mają znaczenie. Bez nich `try?` próbowałby objąć całe wyrażenie razem z `??`, a kompilator prosi o wyraźne zaznaczenie, gdzie kończy się zawodzące wywołanie.

Przeczytaj linię jako jedno zdanie: *użyj portu, który udało się odczytać, w przeciwnym razie 8080*. Dwie linie `do`/`catch` zwijają się w jedną, gdy ratunek to naprawdę po prostu wartość domyślna.

---

Jest jeszcze trzecia forma: `try!`. Mówi kompilatorowi *to wywołanie nie może zawieść*, więc żadnego `do`, żadnego `catch` i żadnego opcjonału. Jeśli mimo wszystko zawiedzie, program natychmiast się zatrzymuje.
```swift
let pattern = try! Regex("[0-9]+")
```
To jest sytuacja, w której `try!` da się obronić: argument to literał napisany przez Ciebie, w Twoim własnym kodzie źródłowym, a jeśli jest błędny, program jest zepsuty i powinien zatrzymać się podczas pierwszego uruchomienia testów.

Wszystko, co przychodzi w czasie działania — linia wpisana przez użytkownika, plik, odpowiedź z sieci — może być błędne na sposoby, których nie widać podczas pisania kodu, a `try!` na tym zamienia odwracalne niepowodzenie w awarię na oczach użytkownika. Użyj tam `do`/`catch` albo `try?`.

---

Gdy funkcja zgłasza błąd, wszystko po `throw` jest pomijane — także linia, która miała zamknąć plik albo zwolnić blokadę. `defer` rozwiązuje to: rejestruje blok od razu i wykonuje go, gdy bieżący zasięg się kończy — niezależnie od tego, jak się kończy.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
Wywołanie wypisuje `open`, potem `close`, i dopiero potem błąd wędruje dalej do wywołującego. Gdyby funkcja zwróciła się normalnie, `close` również by się wypisał — o to chodzi. Umieść sprzątanie tuż obok przygotowania i przestań się martwić, którą drogą wyjdzie kod.

---

Zasięg może zarejestrować więcej niż jeden `defer`. Wykonują się w **odwrotnej** kolejności: ostatni zarejestrowany wykonuje się jako pierwszy.

To nie jest dowolna reguła. Sprzątanie zwykle cofa przygotowanie, które zaszło w pewnej kolejności — otwórz plik, potem go zablokuj — a cofanie musi iść w drugą stronę: odblokuj, potem zamknij. Odwrócona kolejność sprawia, że każdy `defer` jest lustrzanym odbiciem linii nad nim.

---

Funkcja przyjmująca domknięcie ma problem: nie może wiedzieć, czy otrzymane domknięcie zgłosi błąd. Oznaczenie funkcji `throws` zmusiłoby każdego wywołującego do pisania `try`, także tych, którzy przekazują nieszkodliwe domknięcie. `rethrows` mówi *zgłaszam błąd tylko wtedy, gdy zgłasza go przekazane mi domknięcie*:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
Wewnątrz ciała nadal piszesz `try`, bo wywołanie naprawdę może zawieść. W miejscu wywołania kompilator patrzy na przekazane domknięcie:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // try nie jest potrzebne
```
Biblioteka standardowa używa tego wszędzie — `map`, `filter` i `sorted(by:)` to wszystko `rethrows` — dlatego nigdy nie piszesz `try` przed zwykłym `map`.

---

Blok `do` nie ogranicza się do jednego typu błędu. Każdy krok może zawieść na swój sposób, a każde niepowodzenie dostaje własny `catch`:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
Pierwsze `try`, które zgłosi błąd, kończy blok, więc późniejsze kroki nigdy się nie wykonają — wartość po prostu nigdy nie istniała. To właśnie sprawia, że ta forma jest czytelna: szczęśliwa ścieżka pozostaje jedną prostą linią na górze, a każdy sposób, w jaki może pójść źle, jest wypisany pod spodem.

---

To, gdzie znajduje się blok `do`, decyduje o tym, ile kosztuje pojedyncza awaria. Umieść go **wewnątrz** pętli, a każdy element dostanie własną próbę, dzięki czemu jedna zła wartość zostanie pominięta, a reszta i tak się wykona:
```swift
for age in [4, -1, 7] {
    do {
        print(try label(age))
    } catch {
        print("skipped")
    }
}
```
Owinięcie całej pętli w jeden `do` zatrzymałoby się natomiast na pierwszym błędzie i nigdy nie dotarłoby do `7`. Żadne z tych podejść nie jest błędne — to różnica między *jednym złym elementem* a *poddaniem się*.

---

Wszystko w tym rozdziale odpowiada na jedno pytanie: kto zajmuje się awarią?

Funkcja zgłaszająca błąd odmawia odpowiedzi na nie. Nazywa to, co poszło nie tak — przypadek wyliczenia `Error`, niosący wszystko, czego będzie potrzebować procedura obsługi — i przekazuje decyzję wyżej. Wywołujący wybiera wtedy narzędzie: `do`/`catch`, by reagować przypadek po przypadku, `try?` i `??`, by cofnąć się do wartości domyślnej, `defer`, by posprzątać przy wyjściu, niezależnie od tego, jak się ono odbędzie.

Właśnie w tym podziale tkwi cały sens. Funkcja, która wykrywa problem, rzadko wie, co powinno stać się dalej, a kod, który to wie, rzadko chce powtarzać sprawdzenie.
