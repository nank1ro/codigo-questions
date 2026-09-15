Część pracy nie kończy się od razu: pobieranie pliku, odczyt z bazy danych, oczekiwanie na minutnik. Gdyby program po prostu zatrzymał się i czekał, nic innego nie mogłoby się wydarzyć w międzyczasie. Swift rozwiązuje to za pomocą **funkcji asynchronicznych**.

Funkcja oznaczona **`async`** może wstrzymać się w połowie i wznowić później. Słowo kluczowe stoi za listą parametrów, przed strzałką:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Wywoływanie też wygląda inaczej: musisz napisać **`await`** przed wywołaniem. `await` oznacza dokładne miejsce, w którym program może się wstrzymać, i daje zwykłą wartość, gdy tylko funkcja się zakończy:
```swift
let n = await fetchNumber()
print(n)
// wypisuje 42
```
W skrypcie Swift najwyższy poziom już obsługuje `await`, więc możesz wywoływać funkcje asynchroniczne bezpośrednio, bez żadnej dodatkowej konfiguracji. Zapomnienie `async` lub `await` to błąd kompilacji, a nie cichy błąd.

---

Funkcja asynchroniczna to wciąż zwykła funkcja: może przyjmować parametry i zwracać wartość dowolnego typu. Zmieniają się tylko dwie rzeczy: słowo kluczowe `async` w sygnaturze i `await` w każdym miejscu wywołania:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// wypisuje 10.0
```
Zwracana wartość to zwykły `Double`, a nie opakowanie: gdy `await` się zakończy, pracujesz z nią dokładnie jak zwykle.

---

Funkcje asynchroniczne są zwykle budowane jedna na drugiej. Wewnątrz funkcji `async` możesz użyć `await` na dowolnej innej funkcji `async`, a wynik jest używany jak każda normalna wartość:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// wypisuje 15
```
`await` jest dozwolony tylko wewnątrz kontekstu asynchronicznego: funkcji `async` albo najwyższego poziomu skryptu. Zwykła funkcja bez `async` nie może używać `await`.

---

Praca rozłożona w czasie często kończy się niepowodzeniem: serwer nie działa, plik nie istnieje, dane wejściowe są błędne. Taka funkcja jest oznaczona **`async throws`** i jest wywoływana z **`try await`**:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
Aby obsłużyć błąd, owijasz wywołanie w blok `do` i łapiesz go:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// wypisuje could not load
```
Kolejność słów kluczowych jest ustalona: najpierw `try`, potem `await`.

---

Kiedy nie obchodzi cię *dlaczego* wywołanie się nie powiodło, `try?` jest krótsze niż blok `do`. Zamienia wywołanie rzucające w **opcjonał**: wartość w razie sukcesu, `nil` w razie niepowodzenia. W połączeniu z `await` zapisuje się to jako `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Ponieważ wynik jest opcjonałem, pasuje wprost do `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Używaj `try? await` do szybkiego obejścia, a `do` / `catch`, gdy sam błąd ma znaczenie.

---

Kilka wywołań `await` zapisanych jedno po drugim działa **sekwencyjnie**: drugie wywołanie w ogóle się nie zaczyna, dopóki pierwsze nie zwróci wyniku. Kod czyta się od góry do dołu, dokładnie jak zwykły kod:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
Tego chcesz, gdy drugie wywołanie potrzebuje wyniku pierwszego. Gdy wywołania są niezależne, czekanie na jedno przed rozpoczęciem drugiego to strata czasu, a kolejne ćwiczenia pokazują, jak tego uniknąć.

---

Aby uruchomić dwa niezależne wywołania jednocześnie, zadeklaruj je za pomocą **`async let`**. Praca zaczyna się natychmiast, a program działa dalej bez czekania:
```swift
async let left = step("A")
async let right = step("B")
```
Wartość nie jest jeszcze dostępna, więc nie możesz użyć wiązania bezpośrednio: musisz użyć `await` w miejscu, w którym naprawdę jej potrzebujesz. Jedno `await` przed wyrażeniem obejmuje każde `async let` wewnątrz niego:
```swift
let both = await left + right
```
Jeśli każde wywołanie trwa jedną sekundę, wersja sekwencyjna potrzebuje dwóch sekund, a wersja z `async let` około jednej, ponieważ oba wywołania nakładają się na siebie.

---

Kiedy potrzebujesz wyników osobno, zbierz kilka wiązań `async let` w krotkę i użyj `await` na całej krotce naraz:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
Oba wywołania już działały; pojedyncze `await` czeka, aż wolniejsze z nich się zakończy. Pamiętaj, że `async let` tylko rozpoczyna pracę: `async let`, na którym nigdy nie użyjesz `await`, jest anulowane i niejawnie awaitowane, gdy zasięg się kończy.

---

`async let` jest związane z zasięgiem, w którym zostało zapisane. Aby rozpocząć pracę współbieżną i zachować do niej uchwyt, użyj **`Task`**. Domknięcie przekazane do `Task { }` działa na własną rękę, a zadanie może być przechowywane, przekazywane dalej lub zwracane:
```swift
let job = Task {
    return await double(21)
}
```
Wynik odczytuje się później za pomocą **`.value`**, które jest awaitowane:
```swift
print(await job.value)
// wypisuje 42
```
Typ uchwytu mówi, co on produkuje i co może zgłosić: `Task<Int, Never>` to zadanie, które zwraca `Int` i nigdy nie zgłasza błędu. W przeciwieństwie do `async let`, `Task` można utworzyć ze zwykłego, nieasynchronicznego kodu.

---

`Task.sleep` wstrzymuje bieżące zadanie na chwilę, nie blokując niczego innego. Może zostać przerwane, więc jest to rzucające wywołanie asynchroniczne i wymaga `try await`. Czas trwania podaje się za pomocą metod pomocniczych, takich jak `.seconds`, `.milliseconds` czy `.nanoseconds`:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
To standardowy sposób symulowania powolnej pracy w przykładzie zamiast prawdziwego wywołania sieciowego. Zauważ, że nie zamraża programu: podczas gdy jedno zadanie śpi, pozostałe działają dalej.

---

Teraz różnica między sekwencyjnym a współbieżnym staje się mierzalna. Załóżmy, że `work` śpi jedną sekundę przed zwróceniem wyniku:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Czekanie z `await` na wywołania jedno po drugim zajmuje około **dwóch** sekund, ponieważ drugie uśpienie zaczyna się dopiero, gdy pierwsze się skończy:
```swift
let a = await work(1)
let b = await work(2)
```
Rozpoczęcie ich za pomocą `async let` zajmuje około **jednej** sekundy, ponieważ oba uśpienia nakładają się na siebie:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Zapisanie `await work(1) + await work(2)` w jednej linii nic nie zmienia: oba wywołania są nadal obliczane jedno po drugim. Współbieżność pochodzi z `async let` albo z zadań, nigdy z tego, jak sformatowana jest linia.

---

`async let` działa, gdy podczas pisania kodu wiesz, ile jest wywołań. Dla listy, której rozmiar jest znany dopiero w czasie działania, użyj **grupy zadań**.

`withTaskGroup(of:)` otwiera grupę, `addTask` uruchamia jedno zadanie podrzędne na element, a grupę czyta się następnie za pomocą `for await`, które dostarcza wyniki w miarę ich kończenia:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` deklaruje, co zwraca każde zadanie podrzędne. Całe wywołanie `withTaskGroup` to jedno wyrażenie, więc potrzebuje pojedynczego `await` przed sobą i nie zwraca wyniku, dopóki każde zadanie podrzędne się nie zakończy.

---

Grupa zadań przekazuje wyniki w **kolejności ukończenia**, a nie w kolejności, w jakiej dodano zadania. Najszybsze zadanie podrzędne przychodzi pierwsze, więc zbieranie wartości do tablicy daje nieprzewidywalną kolejność.

Gdy kolejność ma znaczenie, są dwa rozwiązania. Jeśli wartości można po prostu przetasować, posortuj je na końcu:
```swift
return values.sorted()
```
Jeśli każdy wynik należy do pozycji, każ zadaniu zwracać parę `(index, value)` i zapisz ją do przygotowanej tablicy:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
Suma, maksimum ani licznik nie potrzebują żadnego z tych rozwiązań, ponieważ kolejność wartości nie zmienia odpowiedzi.
